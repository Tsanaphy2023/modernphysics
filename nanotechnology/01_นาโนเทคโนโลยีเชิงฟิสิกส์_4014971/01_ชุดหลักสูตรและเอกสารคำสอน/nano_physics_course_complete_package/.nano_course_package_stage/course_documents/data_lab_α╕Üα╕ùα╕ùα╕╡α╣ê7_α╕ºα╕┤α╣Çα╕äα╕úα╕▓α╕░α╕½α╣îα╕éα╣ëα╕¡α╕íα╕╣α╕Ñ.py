#!/usr/bin/env python3
"""
Data Lab บทที่ 7: การประยุกต์ใช้และการตัดสินใจอย่างรับผิดชอบ

สคริปต์นี้มี 2 โหมด
1) experiment: วิเคราะห์ข้อมูลทดลองจริงจากไฟล์ CSV และเปรียบเทียบ control กับ treatment
2) decision: สร้าง decision matrix ที่เปิดเผยน้ำหนัก คุณภาพหลักฐาน และความไม่แน่นอน

ข้อสำคัญ
- สคริปต์นี้ไม่สร้างหรือแทนที่ข้อมูลทดลองจริง
- ผลวิเคราะห์เป็นเครื่องมือช่วยอภิปรายหลักฐาน ไม่ใช่หลักฐานเพียงพอสำหรับรับรองความปลอดภัย
- ก่อนสรุปผล ให้ตรวจ SOP, metadata, control, หน่วย และบริบทการวัดทุกครั้ง

ความต้องการไลบรารี: pandas, numpy, matplotlib
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import textwrap

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------
# ส่วนที่ 1: เครื่องมือร่วม
# ------------------------------

def make_output_dir(output_dir: str) -> Path:
    """สร้างโฟลเดอร์ผลลัพธ์ หากยังไม่มี"""
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_csv_or_stop(path: str) -> pd.DataFrame:
    """อ่าน CSV พร้อมรายงาน error ที่ผู้เรียนแก้ไขได้"""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise SystemExit(f"ไม่พบไฟล์: {path}")
    except UnicodeDecodeError:
        raise SystemExit("อ่านไฟล์ไม่สำเร็จ: ให้บันทึก CSV เป็น UTF-8 แล้วลองใหม่")
    except Exception as exc:
        raise SystemExit(f"อ่าน CSV ไม่สำเร็จ: {exc}")

    if df.empty:
        raise SystemExit("ไฟล์ CSV ไม่มีข้อมูล")
    return df


def require_columns(df: pd.DataFrame, columns: list[str], context: str) -> None:
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise SystemExit(
            f"{context} ขาดคอลัมน์: {', '.join(missing)}\n"
            f"คอลัมน์ที่พบ: {', '.join(map(str, df.columns))}"
        )


def save_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


# ------------------------------
# ส่วนที่ 2: วิเคราะห์ข้อมูลทดลอง
# ------------------------------

def validate_experiment_data(df: pd.DataFrame, group_col: str, response_col: str) -> pd.DataFrame:
    """ตรวจชนิดข้อมูล ตัดเฉพาะแถวที่ response หาย และบันทึกสถานะก่อนวิเคราะห์"""
    require_columns(df, [group_col, response_col], "ข้อมูลทดลอง")
    clean = df.copy()
    clean[response_col] = pd.to_numeric(clean[response_col], errors="coerce")

    missing_response = int(clean[response_col].isna().sum())
    if missing_response:
        print(f"คำเตือน: ตัด {missing_response} แถวที่ค่า {response_col} ไม่ใช่ตัวเลขหรือหายไป")
        clean = clean.dropna(subset=[response_col])

    clean[group_col] = clean[group_col].astype(str).str.strip()
    clean = clean.loc[clean[group_col] != ""].copy()
    if clean.empty:
        raise SystemExit("ไม่มีแถวข้อมูลที่ใช้วิเคราะห์ได้หลังตรวจค่า group/response")

    return clean


def descriptive_summary(df: pd.DataFrame, group_col: str, response_col: str) -> pd.DataFrame:
    """คำนวณสถิติพรรณนารายกลุ่มและช่วงความเชื่อมั่นแบบ normal approximation"""
    rows = []
    for group_name, group in df.groupby(group_col, dropna=False):
        x = group[response_col].dropna().to_numpy(dtype=float)
        n = len(x)
        mean = float(np.mean(x))
        sd = float(np.std(x, ddof=1)) if n > 1 else np.nan
        sem = sd / np.sqrt(n) if n > 1 else np.nan
        ci_low = mean - 1.96 * sem if n > 1 else np.nan
        ci_high = mean + 1.96 * sem if n > 1 else np.nan
        rows.append(
            {
                group_col: group_name,
                "n": n,
                "mean": mean,
                "median": float(np.median(x)),
                "sd": sd,
                "sem": sem,
                "ci95_low": ci_low,
                "ci95_high": ci_high,
                "min": float(np.min(x)),
                "max": float(np.max(x)),
            }
        )
    return pd.DataFrame(rows)


def bootstrap_mean_difference(
    control: np.ndarray,
    treatment: np.ndarray,
    draws: int = 10_000,
    seed: int = 2026,
) -> dict[str, float]:
    """ประมาณช่วงความเชื่อมั่นของผลต่างค่าเฉลี่ยด้วย bootstrap แบบทำซ้ำได้"""
    if len(control) < 2 or len(treatment) < 2:
        return {
            "mean_difference": float(np.mean(treatment) - np.mean(control)),
            "ci95_low": np.nan,
            "ci95_high": np.nan,
            "draws": 0,
        }

    rng = np.random.default_rng(seed)
    control_means = rng.choice(control, size=(draws, len(control)), replace=True).mean(axis=1)
    treatment_means = rng.choice(treatment, size=(draws, len(treatment)), replace=True).mean(axis=1)
    differences = treatment_means - control_means
    return {
        "mean_difference": float(np.mean(treatment) - np.mean(control)),
        "ci95_low": float(np.percentile(differences, 2.5)),
        "ci95_high": float(np.percentile(differences, 97.5)),
        "draws": draws,
    }


def cohens_d(control: np.ndarray, treatment: np.ndarray) -> float:
    """คำนวณ standardized mean difference; คืน NaN เมื่อข้อมูลไม่เพียงพอ"""
    n0, n1 = len(control), len(treatment)
    if n0 < 2 or n1 < 2:
        return np.nan
    var0 = np.var(control, ddof=1)
    var1 = np.var(treatment, ddof=1)
    pooled_sd = np.sqrt(((n0 - 1) * var0 + (n1 - 1) * var1) / (n0 + n1 - 2))
    if pooled_sd == 0:
        return np.nan
    return float((np.mean(treatment) - np.mean(control)) / pooled_sd)


def plot_group_comparison(
    df: pd.DataFrame,
    group_col: str,
    response_col: str,
    output_file: Path,
    unit: str = "",
) -> None:
    """สร้างกราฟจุดข้อมูลจริง + ค่าเฉลี่ย ± 95% CI เพื่อเลี่ยงการซ่อนการกระจายของข้อมูล"""
    groups = list(df[group_col].dropna().unique())
    positions = np.arange(len(groups))
    rng = np.random.default_rng(2026)

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=160)
    for pos, group_name in zip(positions, groups):
        values = df.loc[df[group_col] == group_name, response_col].to_numpy(dtype=float)
        jitter = rng.normal(0, 0.045, size=len(values))
        ax.scatter(
            np.full(len(values), pos) + jitter,
            values,
            alpha=0.75,
            s=42,
            color="#1f77b4",
            edgecolor="white",
            linewidth=0.5,
            label="ข้อมูลรายซ้ำ" if pos == 0 else None,
            zorder=2,
        )
        mean = np.mean(values)
        if len(values) > 1:
            sem = np.std(values, ddof=1) / np.sqrt(len(values))
            ci = 1.96 * sem
            ax.errorbar(pos, mean, yerr=ci, fmt="D", markersize=7, color="#d95f02", capsize=6,
                        label="ค่าเฉลี่ย ± 95% CI" if pos == 0 else None, zorder=4)
        else:
            ax.scatter(pos, mean, marker="D", s=60, color="#d95f02", zorder=4)

    y_label = response_col + (f" ({unit})" if unit else "")
    ax.set_ylabel(y_label)
    ax.set_xlabel(group_col)
    ax.set_xticks(positions, groups)
    ax.set_title("การเปรียบเทียบผลการทดลอง: แสดงข้อมูลรายซ้ำและค่าเฉลี่ย")
    ax.grid(axis="y", alpha=0.2)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(output_file, bbox_inches="tight")
    plt.close(fig)


def run_experiment(args: argparse.Namespace) -> None:
    raw = read_csv_or_stop(args.input)
    data = validate_experiment_data(raw, args.group, args.response)
    out = make_output_dir(args.output)

    # ทำสำเนาเฉพาะข้อมูลที่ผ่านการตรวจ เพื่อความโปร่งใสในการประมวลผล
    data.to_csv(out / "01_cleaned_data.csv", index=False, encoding="utf-8-sig")
    summary = descriptive_summary(data, args.group, args.response)
    summary.to_csv(out / "02_group_summary.csv", index=False, encoding="utf-8-sig")

    available_groups = sorted(data[args.group].unique().tolist())
    print("กลุ่มที่พบ:", ", ".join(available_groups))
    print("\nสถิติสรุป:")
    print(summary.to_string(index=False, float_format=lambda v: f"{v:.4g}"))

    report_lines = [
        "# รายงาน Data Lab: การวิเคราะห์ข้อมูลทดลอง\n",
        "## ขอบเขตการตีความ\n",
        "ผลลัพธ์นี้สรุปข้อมูลจากไฟล์ที่ผู้ใช้ระบุเท่านั้น ต้องพิจารณา metadata, วิธีวัด, control, ความเป็นอิสระของการทำซ้ำ และข้อจำกัดของเครื่องมือก่อนเชื่อมสู่ข้อสรุปเชิงกลไกหรือการตัดสินใจ\n",
        "## สถิติสรุปรายกลุ่ม\n",
        summary.to_markdown(index=False),
        "\n",
    ]

    # วิเคราะห์ control-treament เฉพาะเมื่อระบุครบ เพื่อไม่ให้ script เดาความหมายของกลุ่มเอง
    if args.control and args.treatment:
        missing_groups = set([args.control, args.treatment]) - set(available_groups)
        if missing_groups:
            raise SystemExit(f"ไม่พบกลุ่มที่ระบุ: {', '.join(sorted(missing_groups))}")

        control = data.loc[data[args.group] == args.control, args.response].to_numpy(dtype=float)
        treatment = data.loc[data[args.group] == args.treatment, args.response].to_numpy(dtype=float)
        boot = bootstrap_mean_difference(control, treatment, args.bootstrap_draws, args.seed)
        effect = cohens_d(control, treatment)
        pairwise = pd.DataFrame([
            {
                "control_group": args.control,
                "treatment_group": args.treatment,
                "mean_difference_treatment_minus_control": boot["mean_difference"],
                "bootstrap_ci95_low": boot["ci95_low"],
                "bootstrap_ci95_high": boot["ci95_high"],
                "bootstrap_draws": boot["draws"],
                "cohens_d": effect,
            }
        ])
        pairwise.to_csv(out / "03_pairwise_effect.csv", index=False, encoding="utf-8-sig")
        report_lines.extend([
            "## การเปรียบเทียบที่ผู้ใช้ระบุ\n",
            pairwise.to_markdown(index=False),
            "\n",
            "**คำเตือนการแปลผล:** ช่วงความเชื่อมั่นของ bootstrap บอกความแปรปรวนที่เข้ากันได้กับข้อมูลตัวอย่าง ไม่ได้ยืนยันกลไกหรือความปลอดภัย และหากจำนวนซ้ำน้อย ผลจะไม่เสถียร\n",
        ])

    graph_file = out / "04_group_comparison.png"
    plot_group_comparison(data, args.group, args.response, graph_file, args.unit)
    report_lines.extend([
        "## ไฟล์ผลลัพธ์\n",
        "- `01_cleaned_data.csv`: ข้อมูลหลังตรวจชนิดและค่า missing\n",
        "- `02_group_summary.csv`: สถิติสรุป\n",
        "- `03_pairwise_effect.csv`: ผลต่าง control–treatment (เมื่อระบุทั้งสองกลุ่ม)\n",
        "- `04_group_comparison.png`: กราฟจุดข้อมูลจริงและค่าเฉลี่ย\n",
    ])
    save_text(out / "05_analysis_report.md", "\n".join(report_lines))
    print(f"\nบันทึกผลลัพธ์ใน: {out.resolve()}")


# ------------------------------
# ส่วนที่ 3: Decision Matrix บทที่ 7
# ------------------------------

def validate_decision_data(df: pd.DataFrame) -> pd.DataFrame:
    """ตรวจตาราง criteria สำหรับการอภิปราย value–risk–evidence"""
    required = ["criterion", "dimension", "weight", "score", "evidence_quality", "uncertainty"]
    require_columns(df, required, "decision matrix")
    clean = df.copy()

    for col in ["weight", "score", "evidence_quality", "uncertainty"]:
        clean[col] = pd.to_numeric(clean[col], errors="coerce")
    if clean[required].isna().any().any():
        raise SystemExit("decision matrix มีค่า missing หรือชนิดข้อมูลไม่ถูกต้องในคอลัมน์บังคับ")
    if (clean["weight"] < 0).any():
        raise SystemExit("weight ต้องไม่ติดลบ")
    if not clean["score"].between(1, 5).all():
        raise SystemExit("score ต้องอยู่ระหว่าง 1 ถึง 5")
    if not clean["evidence_quality"].between(1, 5).all():
        raise SystemExit("evidence_quality ต้องอยู่ระหว่าง 1 ถึง 5")
    if not clean["uncertainty"].between(1, 5).all():
        raise SystemExit("uncertainty ต้องอยู่ระหว่าง 1 ถึง 5; 1 = ต่ำ, 5 = สูง")
    if clean["weight"].sum() == 0:
        raise SystemExit("ผลรวม weight ต้องมากกว่า 0")

    clean["dimension"] = clean["dimension"].astype(str).str.strip().str.lower()
    allowed = {"benefit", "risk", "safety", "feasibility", "equity", "evidence"}
    unknown = sorted(set(clean["dimension"]) - allowed)
    if unknown:
        raise SystemExit(f"dimension ที่ไม่รองรับ: {', '.join(unknown)}\nใช้ได้: {', '.join(sorted(allowed))}")
    return clean


def calculate_decision_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """คำนวณ contribution ที่ลดทอนด้วยคุณภาพหลักฐานและความไม่แน่นอนอย่างเปิดเผย"""
    result = df.copy()
    result["weight_normalized"] = result["weight"] / result["weight"].sum()
    result["score_normalized"] = (result["score"] - 1) / 4  # 1–5 -> 0–1
    result["evidence_factor"] = result["evidence_quality"] / 5
    result["certainty_factor"] = (6 - result["uncertainty"]) / 5
    result["confidence_factor"] = result["evidence_factor"] * result["certainty_factor"]
    result["raw_contribution"] = result["weight_normalized"] * result["score_normalized"]
    result["evidence_adjusted_contribution"] = result["raw_contribution"] * result["confidence_factor"]
    return result


def plot_decision_matrix(result: pd.DataFrame, output_file: Path) -> None:
    """สร้าง scatter plot เพื่อให้ผู้เรียนเห็นเกณฑ์ที่ evidence ต่ำและ uncertainty สูง"""
    colours = {
        "benefit": "#1b9e77", "risk": "#d95f02", "safety": "#7570b3",
        "feasibility": "#e7298a", "equity": "#66a61e", "evidence": "#666666",
    }
    fig, ax = plt.subplots(figsize=(9.5, 6), dpi=160)
    for dimension, group in result.groupby("dimension"):
        ax.scatter(
            group["uncertainty"], group["evidence_quality"],
            s=500 * group["weight_normalized"] + 70,
            alpha=0.8,
            color=colours.get(dimension, "#555555"),
            label=dimension,
            edgecolor="white",
            linewidth=0.8,
        )
        for _, row in group.iterrows():
            ax.annotate(str(row["criterion"]), (row["uncertainty"], row["evidence_quality"]),
                        xytext=(6, 5), textcoords="offset points", fontsize=8)

    ax.axvline(3, color="#777777", linestyle="--", linewidth=0.8)
    ax.axhline(3, color="#777777", linestyle="--", linewidth=0.8)
    ax.text(4.8, 1.15, "ต้องหาหลักฐานเพิ่ม\n(ความไม่แน่นอนสูง)", ha="right", va="bottom", fontsize=9)
    ax.text(1.2, 4.8, "ฐานหลักฐานค่อนข้างดี", ha="left", va="top", fontsize=9)
    ax.set_xlim(0.7, 5.8)
    ax.set_ylim(0.7, 5.8)
    ax.set_xlabel("ความไม่แน่นอน (1 = ต่ำ, 5 = สูง)")
    ax.set_ylabel("คุณภาพหลักฐาน (1 = ต่ำ, 5 = สูง)")
    ax.set_title("แผนที่หลักฐาน–ความไม่แน่นอน: ใช้เพื่อกำหนดคำถามถัดไป")
    ax.legend(title="dimension", frameon=False, loc="lower left")
    ax.grid(alpha=0.15)
    fig.tight_layout()
    fig.savefig(output_file, bbox_inches="tight")
    plt.close(fig)


def run_decision(args: argparse.Namespace) -> None:
    raw = read_csv_or_stop(args.input)
    data = validate_decision_data(raw)
    result = calculate_decision_matrix(data)
    out = make_output_dir(args.output)

    result.to_csv(out / "01_decision_matrix_scored.csv", index=False, encoding="utf-8-sig")
    by_dimension = result.groupby("dimension", as_index=False).agg(
        raw_score=("raw_contribution", "sum"),
        evidence_adjusted_score=("evidence_adjusted_contribution", "sum"),
        mean_evidence_quality=("evidence_quality", "mean"),
        mean_uncertainty=("uncertainty", "mean"),
    )
    by_dimension.to_csv(out / "02_dimension_summary.csv", index=False, encoding="utf-8-sig")
    plot_decision_matrix(result, out / "03_evidence_uncertainty_map.png")

    high_priority = result.sort_values(
        ["uncertainty", "weight_normalized"], ascending=[False, False]
    ).head(3)[["criterion", "dimension", "weight", "evidence_quality", "uncertainty"]]

    report = "\n".join([
        "# รายงาน Decision Matrix: Value–Risk–Evidence\n",
        "> ตารางนี้เป็นเครื่องมือทำให้สมมติฐาน น้ำหนัก และความไม่แน่นอนมองเห็นได้ ไม่ใช่อัลกอริทึมที่ให้คำตอบแทนการพิจารณาทางวิทยาศาสตร์หรือจริยธรรม\n",
        "## สรุปตามมิติ\n",
        by_dimension.to_markdown(index=False),
        "\n## เกณฑ์ที่ควรหาหลักฐานเพิ่มก่อนตัดสินใจ\n",
        high_priority.to_markdown(index=False),
        "\n## คำถามอภิปราย\n",
        "1. หากเปลี่ยนน้ำหนักของ safety หรือ equity ข้อเสนอของกลุ่มเปลี่ยนหรือไม่?\n",
        "2. เกณฑ์ใดได้คะแนนสูงแต่มี evidence_quality ต่ำ และเหตุใดจึงยังไม่ควรใช้เป็นข้อสรุป?\n",
        "3. มี control, comparator หรือข้อมูลวงจรชีวิตใดที่ควรเพิ่ม?\n",
        "4. ผู้มีส่วนได้ส่วนเสียใดอาจได้ประโยชน์หรือรับภาระจากข้อเสนอของเรา?\n",
    ])
    save_text(out / "04_decision_report.md", report)
    print("\nสรุปคะแนนตามมิติ:")
    print(by_dimension.to_string(index=False, float_format=lambda v: f"{v:.3f}"))
    print(f"\nบันทึกผลลัพธ์ใน: {out.resolve()}")


# ------------------------------
# ส่วนที่ 4: Command-line interface
# ------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Data Lab บทที่ 7: วิเคราะห์ข้อมูลทดลองและ decision matrix แบบโปร่งใส",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """
            ตัวอย่างการใช้
            -------------
            # วิเคราะห์ผลทดลองจริง control เทียบกับ coating
            python data_lab_บทที่7_วิเคราะห์ข้อมูล.py experiment \\
                --input experiment.csv --output results_experiment \\
                --group group --response response --unit "a.u." \\
                --control control --treatment coating

            # วิเคราะห์ decision matrix ของกลุ่ม
            python data_lab_บทที่7_วิเคราะห์ข้อมูล.py decision \\
                --input decision_matrix.csv --output results_decision
            """
        ),
    )
    sub = parser.add_subparsers(dest="mode", required=True)

    exp = sub.add_parser("experiment", help="วิเคราะห์ข้อมูลทดลองจาก CSV")
    exp.add_argument("--input", required=True, help="ไฟล์ CSV ของข้อมูลทดลองจริง")
    exp.add_argument("--output", required=True, help="โฟลเดอร์เก็บผลลัพธ์")
    exp.add_argument("--group", default="group", help="ชื่อคอลัมน์กลุ่มทดลอง (default: group)")
    exp.add_argument("--response", default="response", help="ชื่อคอลัมน์ค่าที่วัด (default: response)")
    exp.add_argument("--unit", default="", help="หน่วยของค่าที่วัด เพื่อใส่ในกราฟ")
    exp.add_argument("--control", default=None, help="ชื่อกลุ่ม control สำหรับเปรียบเทียบ")
    exp.add_argument("--treatment", default=None, help="ชื่อกลุ่ม treatment สำหรับเปรียบเทียบ")
    exp.add_argument("--bootstrap-draws", type=int, default=10_000, help="จำนวน bootstrap draws")
    exp.add_argument("--seed", type=int, default=2026, help="seed เพื่อทำซ้ำผล bootstrap")
    exp.set_defaults(func=run_experiment)

    dec = sub.add_parser("decision", help="วิเคราะห์ decision matrix แบบ value–risk–evidence")
    dec.add_argument("--input", required=True, help="ไฟล์ CSV decision matrix")
    dec.add_argument("--output", required=True, help="โฟลเดอร์เก็บผลลัพธ์")
    dec.set_defaults(func=run_decision)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
