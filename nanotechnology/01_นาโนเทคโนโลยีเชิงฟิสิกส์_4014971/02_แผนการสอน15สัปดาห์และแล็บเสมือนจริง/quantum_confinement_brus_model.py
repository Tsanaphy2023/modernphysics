"""
Quantum confinement in semiconductor quantum dots
---------------------------------------------------
ตัวอย่างสำหรับการสอนสัปดาห์ที่ 4: สารกึ่งตัวนำและ quantum dot

แบบจำลองที่ใช้คือสมการ Brus ในกรอบ effective-mass approximation:

E_g(R) = E_g_bulk
         + (hbar^2*pi^2/(2*R^2)) * (1/m_e* + 1/m_h*)
         - 1.8*e^2/(4*pi*epsilon_0*epsilon_r*R)

โดย R คือรัศมีของ quantum dot

ข้อควรระวัง:
- แบบจำลองนี้เป็นแบบจำลองอย่างง่าย เหมาะสำหรับแสดงแนวโน้มเชิงฟิสิกส์
- ยังไม่รวมรายละเอียด band structure, dielectric mismatch, surface states,
  strain, polydispersity และ quantum corrections อื่น ๆ
- ควรใช้เพื่ออภิปรายว่า "ขนาดเล็กลงทำให้ band gap สูงขึ้นได้อย่างไร"
  ไม่ควรใช้แทนค่าทดลองโดยตรงสำหรับทุกขนาดอนุภาค
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# ค่าคงที่ทางฟิสิกส์ SI
# ---------------------------
E_CHARGE = 1.602176634e-19       # ประจุอิเล็กตรอน, C
H_BAR = 1.054571817e-34          # hbar, J s
EPSILON_0 = 8.8541878128e-12     # permittivity ของสุญญากาศ, F/m
M_ELECTRON = 9.1093837015e-31    # มวลอิเล็กตรอน, kg

# ---------------------------
# พารามิเตอร์ตัวอย่าง: CdSe quantum dot
# ค่าเป็นค่าประมาณสำหรับการสาธิต
# ---------------------------
MATERIAL = {
    "name": "CdSe",
    "Eg_bulk_eV": 1.74,          # band gap ของ bulk CdSe โดยประมาณ
    "m_e_eff": 0.13,             # effective electron mass / m0
    "m_h_eff": 0.45,             # effective hole mass / m0
    "relative_permittivity": 9.5 # dielectric constant โดยประมาณ
}


def confinement_energy_eV(radius_nm, effective_mass_ratio):
    """พลังงาน confinement ของอนุภาคหนึ่งชนิดในหน่วย eV."""
    radius_m = np.asarray(radius_nm, dtype=float) * 1e-9
    effective_mass = effective_mass_ratio * M_ELECTRON

    energy_joule = (H_BAR**2 * np.pi**2) / (2 * effective_mass * radius_m**2)
    return energy_joule / E_CHARGE


def coulomb_attraction_eV(radius_nm, relative_permittivity):
    """พลังงานดึงดูด Coulomb ระหว่าง electron-hole ในหน่วย eV."""
    radius_m = np.asarray(radius_nm, dtype=float) * 1e-9

    energy_joule = (
        1.8 * E_CHARGE**2
        / (4 * np.pi * EPSILON_0 * relative_permittivity * radius_m)
    )
    return energy_joule / E_CHARGE


def brus_bandgap_eV(radius_nm, material=MATERIAL, include_coulomb=True):
    """คำนวณ band gap ของ quantum dot ตามสมการ Brus ในหน่วย eV."""
    electron_term = confinement_energy_eV(radius_nm, material["m_e_eff"])
    hole_term = confinement_energy_eV(radius_nm, material["m_h_eff"])

    bandgap = material["Eg_bulk_eV"] + electron_term + hole_term

    if include_coulomb:
        coulomb_term = coulomb_attraction_eV(
            radius_nm, material["relative_permittivity"]
        )
        bandgap = bandgap - coulomb_term

    return bandgap


def wavelength_nm(energy_eV):
    """แปลงพลังงานโฟตอนเป็นความยาวคลื่นโดยใช้ hc ≈ 1240 eV nm."""
    return 1240.0 / np.asarray(energy_eV, dtype=float)


def print_example_table(radii_nm, material=MATERIAL):
    """พิมพ์ตารางค่าตัวอย่างสำหรับใช้ถามนักศึกษาในชั้นเรียน."""
    print(f"วัสดุ: {material['name']}")
    print("สมการ: Brus model with electron-hole Coulomb attraction")
    print("\nรัศมี (nm) | เส้นผ่านศูนย์กลาง (nm) | Eg (eV) | wavelength (nm)")
    print("-" * 66)

    for radius in radii_nm:
        eg = brus_bandgap_eV(radius, material)
        wavelength = wavelength_nm(eg)
        print(
            f"{radius:10.2f} | {2*radius:21.2f} | "
            f"{eg:7.3f} | {wavelength:14.1f}"
        )


def make_figure(material=MATERIAL):
    """สร้างกราฟ band gap และ wavelength ในฟังก์ชันของขนาด quantum dot."""
    radius_nm = np.linspace(1.2, 10.0, 500)
    diameter_nm = 2 * radius_nm

    eg_with_coulomb = brus_bandgap_eV(
        radius_nm, material, include_coulomb=True
    )
    eg_without_coulomb = brus_bandgap_eV(
        radius_nm, material, include_coulomb=False
    )
    wavelength = wavelength_nm(eg_with_coulomb)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)

    # กราฟซ้าย: band gap
    axes[0].plot(
        diameter_nm,
        eg_with_coulomb,
        color="tab:blue",
        linewidth=2.5,
        label="Brus model: รวม Coulomb term",
    )
    axes[0].plot(
        diameter_nm,
        eg_without_coulomb,
        color="tab:orange",
        linestyle="--",
        linewidth=2,
        label="ไม่รวม Coulomb term",
    )
    axes[0].axhline(
        material["Eg_bulk_eV"],
        color="black",
        linestyle=":",
        linewidth=1.8,
        label=f"Bulk Eg = {material['Eg_bulk_eV']:.2f} eV",
    )
    axes[0].set_xlabel("Quantum-dot diameter (nm)")
    axes[0].set_ylabel("Effective band gap, Eg (eV)")
    axes[0].set_title(f"Quantum confinement in {material['name']}")
    axes[0].grid(alpha=0.25)
    axes[0].legend(fontsize=9)

    # กราฟขวา: ความยาวคลื่นที่สอดคล้องกับ band gap
    axes[1].plot(
        diameter_nm,
        wavelength,
        color="tab:green",
        linewidth=2.5,
    )
    axes[1].set_xlabel("Quantum-dot diameter (nm)")
    axes[1].set_ylabel("Approx. optical wavelength (nm)")
    axes[1].set_title("Size-dependent optical transition")
    axes[1].grid(alpha=0.25)

    fig.suptitle(
        "Smaller quantum dots generally show larger effective band gaps",
        fontsize=13,
    )
    return fig


if __name__ == "__main__":
    # ตารางค่าตัวอย่างสำหรับอภิปรายในชั้นเรียน
    sample_radii_nm = np.array([1.5, 2.0, 3.0, 4.0, 5.0])
    print_example_table(sample_radii_nm)

    # สร้างและบันทึกกราฟความละเอียดสูง
    figure = make_figure()
    output_file = "quantum_confinement_cdse.png"
    figure.savefig(output_file, dpi=180)
    print(f"\nบันทึกกราฟแล้วที่: {output_file}")

    # แสดงกราฟเมื่อรันบนเครื่องที่มี graphical backend
    plt.show()
