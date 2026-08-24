#!/usr/bin/env python3
"""Data Lab template for Nanotechnological Physics.

Purpose
-------
Read a learner-supplied CSV, perform transparent descriptive analysis, and
write reusable tables/figures. The script never invents observations and never
drops apparent outliers automatically. Use metadata and domain judgment before
excluding any point.

Example
-------
python data_lab_analysis_template.py \
  --input measurements.csv \
  --group condition \
  --value particle_size_nm \
  --output results

Minimum CSV schema
------------------
A categorical grouping column (e.g., ``condition``) and a numeric measurement
column (e.g., ``particle_size_nm``). Optional fields such as ``sample_id``,
``replicate``, ``instrument``, ``unit``, and ``notes`` should be retained in
the source file as metadata.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


REQUIRED_MIN_REPLICATES = 3


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyse a real CSV dataset without silently altering observations."
    )
    parser.add_argument("--input", required=True, help="Path to the input CSV file.")
    parser.add_argument(
        "--group",
        required=True,
        help="Categorical column used to compare conditions, samples, or treatments.",
    )
    parser.add_argument(
        "--value", required=True, help="Numeric measurement column to analyse."
    )
    parser.add_argument(
        "--output", default="data_lab_results", help="Directory for tables and figures."
    )
    parser.add_argument(
        "--unit",
        default="",
        help="Optional unit label for plots, for example 'nm' or 'a.u.'.",
    )
    parser.add_argument(
        "--title", default="Data Lab analysis", help="Title used on the figures."
    )
    return parser.parse_args()


def validate_columns(data: pd.DataFrame, group: str, value: str) -> None:
    missing = [column for column in (group, value) if column not in data.columns]
    if missing:
        available = ", ".join(map(str, data.columns))
        raise ValueError(
            f"Missing required column(s): {', '.join(missing)}. "
            f"Available columns: {available}"
        )


def clean_for_analysis(data: pd.DataFrame, group: str, value: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return analysis-ready rows and an audit table of excluded missing/non-numeric rows.

    Only rows missing a group or numeric value are excluded from *this* analysis.
    The original source file remains unchanged, and the audit is written to disk.
    """
    working = data.copy()
    working["_numeric_value"] = pd.to_numeric(working[value], errors="coerce")
    invalid = working[working[group].isna() | working["_numeric_value"].isna()].copy()
    valid = working.drop(index=invalid.index).copy()
    valid[group] = valid[group].astype(str).str.strip()
    valid = valid[valid[group] != ""].copy()

    if valid.empty:
        raise ValueError("No analysable rows remain after checking group and numeric value fields.")
    return valid, invalid


def summarize(valid: pd.DataFrame, group: str) -> pd.DataFrame:
    grouped = valid.groupby(group, dropna=False)["_numeric_value"]
    summary = grouped.agg(n="count", mean="mean", std="std", median="median", minimum="min", maximum="max")
    summary["sem"] = summary["std"] / np.sqrt(summary["n"])
    # The normal-approximation interval is labelled clearly; it is not a substitute
    # for a study-specific uncertainty model or an appropriate inferential test.
    summary["ci95_low_normal_approx"] = summary["mean"] - 1.96 * summary["sem"]
    summary["ci95_high_normal_approx"] = summary["mean"] + 1.96 * summary["sem"]
    summary["replicate_check"] = np.where(
        summary["n"] >= REQUIRED_MIN_REPLICATES,
        f"n ≥ {REQUIRED_MIN_REPLICATES}",
        f"n < {REQUIRED_MIN_REPLICATES}; interpret variation cautiously",
    )
    return summary.reset_index()


def make_figures(valid: pd.DataFrame, summary: pd.DataFrame, group: str, unit: str, title: str, output: Path) -> None:
    labels = summary[group].astype(str).tolist()
    values = [
        valid.loc[valid[group].astype(str) == label, "_numeric_value"].to_numpy()
        for label in labels
    ]
    ylabel = f"Measurement ({unit})" if unit else "Measurement"

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), constrained_layout=True)

    axes[0].boxplot(values, tick_labels=labels, showmeans=True)
    axes[0].set_title("Distribution by group")
    axes[0].set_xlabel(group)
    axes[0].set_ylabel(ylabel)
    axes[0].tick_params(axis="x", rotation=25)
    axes[0].grid(axis="y", alpha=0.25)

    x = np.arange(len(summary))
    means = summary["mean"].to_numpy()
    sems = summary["sem"].fillna(0).to_numpy()
    axes[1].bar(x, means, yerr=sems, capsize=5, color="#d97706", alpha=0.88)
    axes[1].set_xticks(x, labels)
    axes[1].set_title("Mean ± SEM")
    axes[1].set_xlabel(group)
    axes[1].set_ylabel(ylabel)
    axes[1].tick_params(axis="x", rotation=25)
    axes[1].grid(axis="y", alpha=0.25)

    fig.suptitle(title, fontsize=13, fontweight="bold")
    fig.savefig(output / "summary_plots.png", dpi=220, bbox_inches="tight")
    plt.close(fig)


def write_readme(summary: pd.DataFrame, group: str, value: str, unit: str, invalid_rows: int, output: Path) -> None:
    unit_text = f" {unit}" if unit else ""
    lines = [
        "# Data Lab analysis record",
        "",
        f"- **Grouping field:** `{group}`",
        f"- **Measurement field:** `{value}`{unit_text}",
        f"- **Rows excluded only because group/value was missing or non-numeric:** {invalid_rows}",
        "- **Outliers:** No values were removed automatically.",
        "- **Uncertainty statement:** The table reports SD, SEM, and a normal-approximation 95% interval. These are descriptive summaries, not proof of a causal difference.",
        "",
        "## Interpretation prompts",
        "",
        "1. Which condition has the largest central value, and does the spread overlap with other conditions?",
        "2. Are the number of replicates, units, instrument settings, and sample preparation metadata sufficient to support the claim?",
        "3. Which control or additional measurement would most reduce uncertainty?",
        "4. What conclusion should remain conditional rather than definitive?",
        "",
        "## Group summary",
        "",
        summary.to_markdown(index=False),
    ]
    (output / "analysis_record.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 2

    try:
        data = pd.read_csv(input_path)
        validate_columns(data, args.group, args.value)
        valid, invalid = clean_for_analysis(data, args.group, args.value)
        summary = summarize(valid, args.group)
    except (OSError, pd.errors.ParserError, ValueError) as error:
        print(f"Could not analyse data: {error}", file=sys.stderr)
        return 2

    valid.to_csv(output_path / "analysis_ready_rows.csv", index=False)
    invalid.to_csv(output_path / "excluded_missing_or_non_numeric_rows.csv", index=False)
    summary.to_csv(output_path / "summary_by_group.csv", index=False)
    make_figures(valid, summary, args.group, args.unit, args.title, output_path)
    write_readme(summary, args.group, args.value, args.unit, len(invalid), output_path)

    print("Analysis complete. Created:")
    for name in (
        "analysis_ready_rows.csv",
        "excluded_missing_or_non_numeric_rows.csv",
        "summary_by_group.csv",
        "summary_plots.png",
        "analysis_record.md",
    ):
        print(f"  - {output_path / name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
