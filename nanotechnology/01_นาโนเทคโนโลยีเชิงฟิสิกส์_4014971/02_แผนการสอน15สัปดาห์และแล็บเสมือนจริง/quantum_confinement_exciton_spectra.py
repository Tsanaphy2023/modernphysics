"""
Quantum confinement + exciton absorption spectra in semiconductor quantum dots
-------------------------------------------------------------------------------
ตัวอย่างสำหรับการบรรยายเชิงลึกในสัปดาห์ที่ 4

แบบจำลองประกอบด้วย 3 ส่วนหลัก
1) quantum-confinement shift จาก electron และ hole confinement
2) exciton Coulomb binding/correction แบบง่ายตามสมการ Brus
3) absorption spectrum ที่สร้างจาก Lorentzian exciton peaks และ continuum onset

ข้อควรระวังทางฟิสิกส์
----------------------
โค้ดนี้เป็น pedagogical model ไม่ใช่การคำนวณ many-body spectrum แบบเต็มรูปแบบ
โดยยังไม่รวมรายละเอียด เช่น dielectric mismatch, surface polarization,
finite barrier, atomistic band structure, exchange interaction, phonon coupling,
spin fine structure และ disorder เฉพาะของตัวอย่างจริง
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# ค่าคงที่ทางฟิสิกส์ SI
# -----------------------------------------------------------------------------
E_CHARGE = 1.602176634e-19       # C
H_BAR = 1.054571817e-34          # J s
EPSILON_0 = 8.8541878128e-12     # F/m
M_ELECTRON = 9.1093837015e-31    # kg
RYDBERG_ELECTRON_EV = 13.605693  # eV
BOHR_RADIUS_NM = 0.052917721     # nm

# -----------------------------------------------------------------------------
# พารามิเตอร์ตัวอย่าง: CdSe quantum dot
# ค่าประมาณสำหรับการสาธิต ไม่ใช่ชุดพารามิเตอร์สำหรับการ fit ข้อมูลจริง
# -----------------------------------------------------------------------------
MATERIAL = {
    "name": "CdSe",
    "Eg_bulk_eV": 1.74,
    "m_e_eff": 0.13,             # m_e* / m0
    "m_h_eff": 0.45,             # m_h* / m0
    "relative_permittivity": 9.5,
}


def _as_array(values):
    """แปลง scalar/array เป็น NumPy array เพื่อให้ฟังก์ชันรองรับทั้งสองแบบ."""
    return np.asarray(values, dtype=float)


def confinement_energy_eV(radius_nm, effective_mass_ratio):
    """พลังงาน confinement ของอนุภาคหนึ่งชนิดในหน่วย eV."""
    radius_m = _as_array(radius_nm) * 1e-9
    effective_mass = effective_mass_ratio * M_ELECTRON
    energy_joule = H_BAR**2 * np.pi**2 / (2 * effective_mass * radius_m**2)
    return energy_joule / E_CHARGE


def coulomb_correction_eV(radius_nm, relative_permittivity):
    """Coulomb correction แบบ Brus ในหน่วย eV.

    ในแบบจำลองนี้ใช้เป็น effective exciton binding/coulomb correction
    เพื่อแสดงแนวโน้ม ไม่ใช่ค่า binding energy ที่แม่นยำสำหรับทุก regime.
    """
    radius_m = _as_array(radius_nm) * 1e-9
    energy_joule = (
        1.8 * E_CHARGE**2
        / (4 * np.pi * EPSILON_0 * relative_permittivity * radius_m)
    )
    return energy_joule / E_CHARGE


def single_particle_continuum_eV(radius_nm, material=MATERIAL):
    """ขอบพลังงานของ electron-hole continuum ก่อนหัก exciton binding."""
    electron_term = confinement_energy_eV(radius_nm, material["m_e_eff"])
    hole_term = confinement_energy_eV(radius_nm, material["m_h_eff"])
    return material["Eg_bulk_eV"] + electron_term + hole_term


def brus_bandgap_eV(radius_nm, material=MATERIAL, include_coulomb=True):
    """effective optical gap ตามสมการ Brus แบบง่าย."""
    continuum = single_particle_continuum_eV(radius_nm, material)
    if include_coulomb:
        continuum = continuum - coulomb_correction_eV(
            radius_nm, material["relative_permittivity"]
        )
    return continuum


def reduced_mass_ratio(material=MATERIAL):
    """คำนวณ reduced mass ในหน่วยของมวลอิเล็กตรอน m0."""
    me = material["m_e_eff"]
    mh = material["m_h_eff"]
    return (me * mh) / (me + mh)


def exciton_bohr_radius_nm(material=MATERIAL):
    """effective exciton Bohr radius แบบ bulk-like ในหน่วย nm."""
    mu_ratio = reduced_mass_ratio(material)
    epsilon_r = material["relative_permittivity"]
    return BOHR_RADIUS_NM * epsilon_r / mu_ratio


def bulk_exciton_rydberg_eV(material=MATERIAL):
    """effective bulk exciton Rydberg ในหน่วย eV."""
    mu_ratio = reduced_mass_ratio(material)
    epsilon_r = material["relative_permittivity"]
    return RYDBERG_ELECTRON_EV * mu_ratio / epsilon_r**2


def exciton_levels_eV(radius_nm, material=MATERIAL, n_max=3):
    """พลังงาน exciton series แบบ hydrogenic อย่างง่าย.

    E_continuum คือพลังงานของ electron-hole continuum
    E_n = E_continuum - E_binding/n^2

    ใน quantum dot ที่มี strong confinement ค่า binding ที่ใช้เป็น
    effective Coulomb correction ซึ่งขึ้นกับรัศมีของ dot.
    """
    continuum = float(single_particle_continuum_eV(radius_nm, material))
    binding = float(
        coulomb_correction_eV(radius_nm, material["relative_permittivity"])
    )
    n = np.arange(1, n_max + 1, dtype=float)
    energies = continuum - binding / n**2
    # oscillator strength แบบง่าย: peak สูงสุดอยู่ที่ n=1
    strengths = 1.0 / n**3
    return energies, strengths, continuum, binding


def wavelength_nm(energy_eV):
    """แปลงพลังงานโฟตอนเป็นความยาวคลื่นโดยใช้ hc ≈ 1240 eV nm."""
    return 1240.0 / _as_array(energy_eV)


def lorentzian(energy_eV, center_eV, fwhm_eV):
    """Lorentzian line shape ที่มีพื้นที่ใต้เส้นเป็น 1 โดยประมาณ."""
    gamma = max(float(fwhm_eV), 1e-12) / 2.0
    return (gamma / np.pi) / ((energy_eV - center_eV)**2 + gamma**2)


def gaussian(energy_eV, center_eV, sigma_eV):
    """Gaussian line shape ที่มีพื้นที่ใต้เส้นเป็น 1."""
    sigma = max(float(sigma_eV), 1e-12)
    return np.exp(-0.5 * ((energy_eV - center_eV) / sigma)**2) / (
        sigma * np.sqrt(2 * np.pi)
    )


def exciton_absorption_spectrum(
    energy_grid_eV,
    radius_nm,
    material=MATERIAL,
    n_max=3,
    linewidth_meV=35.0,
    include_continuum=True,
    continuum_strength=0.10,
):
    """คำนวณ absorption spectrum ของ quantum dot เดี่ยวแบบง่าย.

    Parameters
    ----------
    energy_grid_eV : array-like
        ช่วงพลังงานโฟตอนที่ต้องการคำนวณ
    radius_nm : float
        รัศมี quantum dot
    n_max : int
        จำนวน exciton states ที่นำมารวม เช่น 1s, 2s, 3s
    linewidth_meV : float
        FWHM ของแต่ละ peak รวม homogeneous broadening แบบจำลอง
    include_continuum : bool
        เพิ่ม absorption continuum เหนือ continuum onset หรือไม่
    continuum_strength : float
        น้ำหนักของ continuum เมื่อเทียบกับ exciton peak
    """
    energy = _as_array(energy_grid_eV)
    levels, strengths, continuum, binding = exciton_levels_eV(
        radius_nm, material, n_max=n_max
    )
    linewidth_eV = linewidth_meV / 1000.0

    absorption = np.zeros_like(energy)
    for level, strength in zip(levels, strengths):
        absorption += strength * lorentzian(
            energy, level, linewidth_eV
        )

    if include_continuum:
        # continuum onset ที่ E_continuum; ใช้ sqrt(E-Ec) เป็นเส้นฐานเชิงสาธิต
        excess = np.maximum(energy - continuum, 0.0)
        continuum_profile = np.sqrt(excess)
        if np.max(continuum_profile) > 0:
            continuum_profile = continuum_profile / np.max(continuum_profile)
        absorption += continuum_strength * continuum_profile

    # normalize เพื่อให้เปรียบเทียบรูปร่างของ spectra ได้ง่าย
    maximum = np.max(absorption)
    if maximum > 0:
        absorption = absorption / maximum

    return absorption, {
        "levels_eV": levels,
        "strengths": strengths,
        "continuum_eV": continuum,
        "binding_eV": binding,
    }


def ensemble_absorption_spectrum(
    energy_grid_eV,
    mean_radius_nm,
    radius_sigma_nm,
    material=MATERIAL,
    n_dots=61,
    n_max=1,
    linewidth_meV=25.0,
    include_continuum=True,
):
    """สเปกตรัมเฉลี่ยของตัวอย่างที่มีการกระจายขนาดแบบ Gaussian.

    ใช้ quadrature ที่กำหนดแน่นอนแทนการสุ่ม เพื่อให้ผลทำซ้ำได้ทุกครั้ง.
    radius_sigma_nm = 0 หมายถึง quantum dot เดี่ยวขนาดเดียว
    """
    energy = _as_array(energy_grid_eV)

    if radius_sigma_nm <= 0:
        spectrum, metadata = exciton_absorption_spectrum(
            energy,
            mean_radius_nm,
            material=material,
            n_max=n_max,
            linewidth_meV=linewidth_meV,
            include_continuum=include_continuum,
        )
        return spectrum, metadata

    radii = np.linspace(
        max(0.5, mean_radius_nm - 3 * radius_sigma_nm),
        mean_radius_nm + 3 * radius_sigma_nm,
        n_dots,
    )
    weights = np.exp(-0.5 * ((radii - mean_radius_nm) / radius_sigma_nm)**2)
    weights = weights / np.sum(weights)

    spectrum = np.zeros_like(energy)
    weighted_levels = []
    for radius, weight in zip(radii, weights):
        single_spectrum, metadata = exciton_absorption_spectrum(
            energy,
            radius,
            material=material,
            n_max=n_max,
            linewidth_meV=linewidth_meV,
            include_continuum=include_continuum,
        )
        spectrum += weight * single_spectrum
        weighted_levels.append(metadata["levels_eV"][0])

    maximum = np.max(spectrum)
    if maximum > 0:
        spectrum = spectrum / maximum

    return spectrum, {
        "radii_nm": radii,
        "weights": weights,
        "first_exciton_energies_eV": np.asarray(weighted_levels),
    }


def print_exciton_table(radii_nm, material=MATERIAL):
    """พิมพ์ตาราง exciton peak และ continuum onset."""
    print(f"วัสดุ: {material['name']}")
    print(f"effective exciton Bohr radius ≈ {exciton_bohr_radius_nm(material):.2f} nm")
    print(f"bulk-like exciton Rydberg ≈ {bulk_exciton_rydberg_eV(material)*1000:.1f} meV")
    print("\nR (nm) | 1s exciton (eV) | continuum (eV) | binding (meV) | wavelength (nm)")
    print("-" * 82)

    for radius in radii_nm:
        levels, _, continuum, binding = exciton_levels_eV(radius, material, n_max=3)
        print(
            f"{radius:6.2f} | {levels[0]:15.3f} | {continuum:15.3f} | "
            f"{binding*1000:13.1f} | {wavelength_nm(levels[0]):14.1f}"
        )


def make_exciton_figure(material=MATERIAL, output_file=None):
    """สร้างกราฟ 4 แผงสำหรับการบรรยายเชิงลึก."""
    energy_grid = np.linspace(1.60, 3.60, 2600)
    radii = [1.5, 2.5, 4.0, 6.0]
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8), constrained_layout=True)

    # 1) spectra ของ quantum dots เดี่ยวหลายขนาด
    ax = axes[0, 0]
    for radius, color in zip(radii, colors):
        spectrum, metadata = exciton_absorption_spectrum(
            energy_grid,
            radius,
            material=material,
            n_max=3,
            linewidth_meV=28,
            continuum_strength=0.08,
        )
        ax.plot(
            energy_grid,
            spectrum,
            color=color,
            linewidth=1.8,
            label=f"R = {radius:.1f} nm",
        )
        ax.axvline(
            metadata["levels_eV"][0],
            color=color,
            alpha=0.20,
            linestyle=":",
        )
    ax.set_title("Single-dot exciton absorption")
    ax.set_xlabel("Photon energy (eV)")
    ax.set_ylabel("Normalized absorption")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    # 2) แสดง exciton series ของ quantum dot เดียว
    ax = axes[0, 1]
    radius = 2.5
    spectrum, metadata = exciton_absorption_spectrum(
        energy_grid,
        radius,
        material=material,
        n_max=4,
        linewidth_meV=22,
        continuum_strength=0.10,
    )
    ax.plot(energy_grid, spectrum, color="black", linewidth=2)
    for n, (level, strength) in enumerate(
        zip(metadata["levels_eV"], metadata["strengths"]), start=1
    ):
        ax.axvline(level, linestyle="--", alpha=0.6, label=f"n = {n}")
    ax.axvline(
        metadata["continuum_eV"],
        color="tab:red",
        linestyle=":",
        linewidth=2,
        label="Continuum onset",
    )
    ax.set_title(f"Exciton series, R = {radius:.1f} nm")
    ax.set_xlabel("Photon energy (eV)")
    ax.set_ylabel("Normalized absorption")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    # 3) homogeneous vs inhomogeneous broadening
    ax = axes[1, 0]
    mean_radius = 2.5
    for sigma, color, label in [
        (0.0, "tab:purple", "Monodisperse: sigma = 0"),
        (0.20, "tab:cyan", "Narrow distribution: sigma = 0.20 nm"),
        (0.50, "tab:brown", "Broad distribution: sigma = 0.50 nm"),
    ]:
        spectrum, _ = ensemble_absorption_spectrum(
            energy_grid,
            mean_radius,
            sigma,
            material=material,
            n_dots=81,
            n_max=1,
            linewidth_meV=22,
            include_continuum=False,
        )
        ax.plot(energy_grid, spectrum, linewidth=1.8, color=color, label=label)
    ax.set_title("Size-distribution broadening")
    ax.set_xlabel("Photon energy (eV)")
    ax.set_ylabel("Normalized absorption")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    # 4) พลังงาน exciton และ binding energy ตามขนาด
    ax = axes[1, 1]
    radius_grid = np.linspace(1.2, 8.0, 300)
    levels_1s = []
    continua = []
    bindings = []
    for radius in radius_grid:
        levels, _, continuum, binding = exciton_levels_eV(radius, material, n_max=1)
        levels_1s.append(levels[0])
        continua.append(continuum)
        bindings.append(binding * 1000)
    ax.plot(2 * radius_grid, levels_1s, label="1s exciton energy", linewidth=2)
    ax.plot(2 * radius_grid, continua, label="Continuum onset", linewidth=2)
    ax2 = ax.twinx()
    ax2.plot(
        2 * radius_grid,
        bindings,
        color="tab:red",
        linestyle="--",
        label="Binding energy",
    )
    ax.set_title("Size dependence of exciton energy")
    ax.set_xlabel("Quantum-dot diameter (nm)")
    ax.set_ylabel("Energy (eV)")
    ax2.set_ylabel("Binding energy (meV)", color="tab:red")
    ax.grid(alpha=0.25)

    # รวม legend ของแกนซ้ายและขวา
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc="best")

    fig.suptitle(
        f"Quantum confinement and exciton absorption in {material['name']}",
        fontsize=14,
    )

    if output_file is not None:
        fig.savefig(output_file, dpi=180)
    return fig


if __name__ == "__main__":
    sample_radii_nm = np.array([1.5, 2.0, 2.5, 3.0, 4.0, 5.0])
    print_exciton_table(sample_radii_nm)

    output_file = "quantum_confinement_exciton_spectra.png"
    make_exciton_figure(MATERIAL, output_file=output_file)
    print(f"\nบันทึกกราฟแล้วที่: {output_file}")

    # ใช้ plt.show() เมื่อต้องการแสดงกราฟใน Jupyter หรือเครื่องที่มี GUI
    plt.show()
