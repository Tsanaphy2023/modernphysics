"""
Temperature-dependent exciton absorption spectra
--------------------------------------------------
ไฟล์ส่วนขยายของ quantum_confinement_exciton_spectra.py
สำหรับสาธิตผลของอุณหภูมิต่อ

1) band-gap shift ด้วย Varshni-type model
2) homogeneous linewidth/broadening จาก acoustic และ optical phonons
3) exciton absorption spectra ที่ทั้งเลื่อนตำแหน่งและกว้างขึ้นตามอุณหภูมิ
4) temperature-energy map ของ absorption spectrum

คำเตือน: เป็น pedagogical model ไม่ใช่ many-body calculation ของวัสดุจริง
"""

import numpy as np
import matplotlib.pyplot as plt

import quantum_confinement_exciton_spectra as base

# Boltzmann constant ในหน่วย eV/K
K_B_EV_PER_K = 8.617333262e-5

# พารามิเตอร์ CdSe แบบประมาณสำหรับการสาธิต
MATERIAL_T = dict(base.MATERIAL)
MATERIAL_T.update(
    {
        # Eg_reference_eV คือ band gap ที่อุณหภูมิอ้างอิง T_reference_K
        "Eg_reference_eV": base.MATERIAL["Eg_bulk_eV"],
        "T_reference_K": 300.0,
        # Varshni parameters: ใช้เป็นค่าตัวอย่าง ไม่ใช่ค่าที่ fit กับ sample ใดโดยเฉพาะ
        "varshni_alpha_eV_per_K": 4.5e-4,
        "varshni_beta_K": 180.0,
        # linewidth model: FWHM(T) = residual + acoustic*T + LO occupation term
        "linewidth_residual_meV": 18.0,
        "acoustic_slope_meV_per_K": 0.025,
        "LO_phonon_energy_meV": 25.0,
        "LO_coupling_meV": 38.0,
    }
)


def varshni_term_eV(temperature_K, material=MATERIAL_T):
    """คำนวณ Varshni term alpha*T^2/(T+beta) ในหน่วย eV."""
    temperature = np.asarray(temperature_K, dtype=float)
    alpha = material["varshni_alpha_eV_per_K"]
    beta = material["varshni_beta_K"]
    return alpha * temperature**2 / (temperature + beta)


def bulk_bandgap_temperature_eV(temperature_K, material=MATERIAL_T):
    """คำนวณ bulk band gap ที่อุณหภูมิ T โดยอ้างอิงค่า Eg ที่ T_reference.

    ใช้รูปแบบ Varshni แบบ relative เพื่อให้ค่า band gap ที่ T_reference_K
    เท่ากับ Eg_reference_eV พอดี:

    Eg(T) = Eg(Tref) + VarshniTerm(Tref) - VarshniTerm(T)
    """
    temperature = np.asarray(temperature_K, dtype=float)
    reference_temperature = material["T_reference_K"]
    reference_gap = material["Eg_reference_eV"]
    return (
        reference_gap
        + varshni_term_eV(reference_temperature, material)
        - varshni_term_eV(temperature, material)
    )


def phonon_broadening_components_meV(
    temperature_K,
    material=MATERIAL_T,
):
    """แยกองค์ประกอบของ FWHM temperature-dependent broadening.

    แบบจำลองเชิงสาธิต:

    FWHM(T) = Gamma_res
              + Gamma_acoustic(T)
              + Gamma_LO * n_LO(T)

    โดย n_LO(T) = 1/[exp(E_LO/(k_B*T)) - 1]
    """
    temperature = np.asarray(temperature_K, dtype=float)
    temperature_nonnegative = np.maximum(temperature, 0.0)

    residual = np.full_like(
        temperature_nonnegative,
        material["linewidth_residual_meV"],
        dtype=float,
    )
    acoustic = material["acoustic_slope_meV_per_K"] * temperature_nonnegative

    phonon_energy_eV = material["LO_phonon_energy_meV"] / 1000.0
    occupation = np.zeros_like(temperature_nonnegative, dtype=float)
    positive_temperature = temperature_nonnegative > 0
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        exponent = phonon_energy_eV / (
            K_B_EV_PER_K * temperature_nonnegative[positive_temperature]
        )
        occupation[positive_temperature] = 1.0 / np.expm1(exponent)

    optical = material["LO_coupling_meV"] * occupation
    total = residual + acoustic + optical

    return {
        "residual_meV": residual,
        "acoustic_meV": acoustic,
        "optical_phonon_meV": optical,
        "total_fwhm_meV": total,
        "LO_occupation": occupation,
    }


def temperature_dependent_exciton_levels_eV(
    radius_nm,
    temperature_K,
    material=MATERIAL_T,
    n_max=3,
):
    """คำนวณ exciton levels เมื่อรวม temperature-dependent bulk gap."""
    continuum = float(bulk_bandgap_temperature_eV(temperature_K, material))
    continuum += float(
        base.confinement_energy_eV(radius_nm, material["m_e_eff"])
    )
    continuum += float(
        base.confinement_energy_eV(radius_nm, material["m_h_eff"])
    )

    # ในรุ่นนี้ถือว่า dielectric constant และ Coulomb correction คงที่ตาม T
    binding = float(
        base.coulomb_correction_eV(
            radius_nm, material["relative_permittivity"]
        )
    )
    n = np.arange(1, n_max + 1, dtype=float)
    energies = continuum - binding / n**2
    strengths = 1.0 / n**3
    return energies, strengths, continuum, binding


def temperature_dependent_absorption_spectrum(
    energy_grid_eV,
    radius_nm,
    temperature_K,
    material=MATERIAL_T,
    n_max=3,
    linewidth_meV=None,
    include_continuum=True,
    continuum_strength=0.10,
):
    """สร้าง exciton absorption spectrum ที่ขึ้นกับอุณหภูมิ.

    หาก linewidth_meV=None จะใช้ linewidth ที่คำนวณจาก phonon model
    หากระบุค่า linewidth_meV จะใช้ค่าคงที่นั้นเพื่อเปรียบเทียบกับกรณี
    ที่มี temperature-dependent peak position แต่ไม่มี thermal broadening
    """
    energy = np.asarray(energy_grid_eV, dtype=float)
    levels, strengths, continuum, binding = (
        temperature_dependent_exciton_levels_eV(
            radius_nm,
            temperature_K,
            material=material,
            n_max=n_max,
        )
    )

    components = phonon_broadening_components_meV(temperature_K, material)
    if linewidth_meV is None:
        fwhm_meV = float(np.asarray(components["total_fwhm_meV"]))
    else:
        fwhm_meV = float(linewidth_meV)

    absorption = np.zeros_like(energy)
    for level, strength in zip(levels, strengths):
        absorption += strength * base.lorentzian(
            energy,
            level,
            fwhm_meV / 1000.0,
        )

    if include_continuum:
        excess = np.maximum(energy - continuum, 0.0)
        continuum_profile = np.sqrt(excess)
        if np.max(continuum_profile) > 0:
            continuum_profile = continuum_profile / np.max(continuum_profile)
        absorption += continuum_strength * continuum_profile

    maximum = np.max(absorption)
    if maximum > 0:
        absorption = absorption / maximum

    return absorption, {
        "levels_eV": levels,
        "strengths": strengths,
        "continuum_eV": continuum,
        "binding_eV": binding,
        "temperature_K": temperature_K,
        "linewidth_fwhm_meV": fwhm_meV,
        "linewidth_components": components,
        "bulk_bandgap_eV": float(
            np.asarray(bulk_bandgap_temperature_eV(temperature_K, material))
        ),
    }


def make_temperature_figure(
    material=MATERIAL_T,
    radius_nm=2.5,
    output_file=None,
):
    """สร้างกราฟ 4 แผงสำหรับสอน temperature-dependent broadening."""
    energy_grid = np.linspace(1.60, 2.80, 2400)
    temperatures = np.array([10.0, 50.0, 100.0, 200.0, 300.0])
    colors = plt.cm.plasma(np.linspace(0.05, 0.90, len(temperatures)))

    fig, axes = plt.subplots(2, 2, figsize=(12, 8), constrained_layout=True)

    # แผง 1: peak shift + thermal broadening
    ax = axes[0, 0]
    for temperature, color in zip(temperatures, colors):
        spectrum, metadata = temperature_dependent_absorption_spectrum(
            energy_grid,
            radius_nm,
            temperature,
            material=material,
            n_max=3,
            linewidth_meV=None,
            include_continuum=True,
            continuum_strength=0.06,
        )
        ax.plot(
            energy_grid,
            spectrum,
            color=color,
            linewidth=1.8,
            label=(
                f"T = {temperature:.0f} K, "
                f"FWHM = {metadata['linewidth_fwhm_meV']:.1f} meV"
            ),
        )
    ax.set_title(f"Temperature-dependent spectra, R = {radius_nm:.1f} nm")
    ax.set_xlabel("Photon energy (eV)")
    ax.set_ylabel("Normalized absorption")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    # แผง 2: linewidth components
    ax = axes[0, 1]
    temperature_grid = np.linspace(0.0, 350.0, 400)
    components = phonon_broadening_components_meV(temperature_grid, material)
    ax.plot(
        temperature_grid,
        components["total_fwhm_meV"],
        color="black",
        linewidth=2.5,
        label="Total FWHM",
    )
    ax.plot(
        temperature_grid,
        components["residual_meV"],
        linestyle=":",
        linewidth=2,
        label="Residual",
    )
    ax.plot(
        temperature_grid,
        components["acoustic_meV"],
        linestyle="--",
        linewidth=2,
        label="Acoustic phonon term",
    )
    ax.plot(
        temperature_grid,
        components["optical_phonon_meV"],
        linestyle="-.",
        linewidth=2,
        label="Optical phonon term",
    )
    ax.set_title("Temperature-dependent linewidth model")
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("FWHM (meV)")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    # แผง 3: peak energy and Varshni band gap
    ax = axes[1, 0]
    peak_energies = []
    continuum_energies = []
    bulk_gaps = []
    for temperature in temperature_grid:
        levels, _, continuum, _ = temperature_dependent_exciton_levels_eV(
            radius_nm,
            temperature,
            material=material,
            n_max=1,
        )
        peak_energies.append(levels[0])
        continuum_energies.append(continuum)
        bulk_gaps.append(bulk_bandgap_temperature_eV(temperature, material))
    ax.plot(
        temperature_grid,
        peak_energies,
        color="tab:blue",
        linewidth=2.5,
        label="1s exciton peak",
    )
    ax.plot(
        temperature_grid,
        continuum_energies,
        color="tab:orange",
        linewidth=2,
        label="Continuum onset",
    )
    ax.plot(
        temperature_grid,
        bulk_gaps,
        color="tab:green",
        linestyle="--",
        linewidth=2,
        label="Bulk Eg(T), Varshni",
    )
    ax.set_title("Temperature-dependent peak position")
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Energy (eV)")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    # แผง 4: heatmap temperature-energy map
    ax = axes[1, 1]
    map_temperatures = np.linspace(10.0, 300.0, 180)
    spectra = []
    for temperature in map_temperatures:
        spectrum, _ = temperature_dependent_absorption_spectrum(
            energy_grid,
            radius_nm,
            temperature,
            material=material,
            n_max=1,
            linewidth_meV=None,
            include_continuum=False,
        )
        spectra.append(spectrum)
    spectra = np.asarray(spectra)
    image = ax.imshow(
        spectra,
        origin="lower",
        aspect="auto",
        extent=[
            energy_grid[0],
            energy_grid[-1],
            map_temperatures[0],
            map_temperatures[-1],
        ],
        cmap="magma",
    )
    ax.set_title("Exciton peak: temperature–energy map")
    ax.set_xlabel("Photon energy (eV)")
    ax.set_ylabel("Temperature (K)")
    fig.colorbar(image, ax=ax, label="Normalized absorption")

    fig.suptitle(
        f"Temperature-dependent exciton broadening in {material['name']}",
        fontsize=14,
    )
    if output_file is not None:
        fig.savefig(output_file, dpi=180)
    return fig


def print_temperature_table(
    temperatures_K,
    radius_nm=2.5,
    material=MATERIAL_T,
):
    """พิมพ์ตารางสรุปผลอุณหภูมิสำหรับใช้ในชั้นเรียน."""
    print(f"วัสดุ: {material['name']}, radius = {radius_nm:.2f} nm")
    print(
        "\nT (K) | Eg_bulk (eV) | 1s peak (eV) | "
        "FWHM (meV) | wavelength (nm)"
    )
    print("-" * 76)
    for temperature in temperatures_K:
        _, metadata = temperature_dependent_absorption_spectrum(
            np.linspace(1.5, 3.5, 2000),
            radius_nm,
            temperature,
            material=material,
            n_max=1,
        )
        peak_energy = metadata["levels_eV"][0]
        print(
            f"{temperature:5.1f} | "
            f"{metadata['bulk_bandgap_eV']:12.4f} | "
            f"{peak_energy:12.4f} | "
            f"{metadata['linewidth_fwhm_meV']:11.2f} | "
            f"{base.wavelength_nm(peak_energy):14.1f}"
        )


if __name__ == "__main__":
    sample_temperatures_K = np.array([10.0, 50.0, 100.0, 200.0, 300.0])
    print_temperature_table(sample_temperatures_K)

    output_file = "quantum_confinement_temperature_exciton.png"
    make_temperature_figure(
        MATERIAL_T,
        radius_nm=2.5,
        output_file=output_file,
    )
    print(f"\nบันทึกกราฟแล้วที่: {output_file}")

    # ใช้ plt.show() เมื่อต้องการแสดงกราฟใน Jupyter หรือเครื่องที่มี GUI
    plt.show()
