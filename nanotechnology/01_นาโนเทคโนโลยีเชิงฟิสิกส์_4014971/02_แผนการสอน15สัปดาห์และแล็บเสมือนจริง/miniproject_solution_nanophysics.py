"""
Instructor reference solution
=============================
Mini-project: From quantum-dot size to temperature-dependent exciton spectra

โค้ดนี้เป็น solution reference สำหรับผู้สอน ไม่ใช่เฉลยที่จำเป็นต้องเหมือน
คำตอบของนักศึกษาทุกบรรทัด นักศึกษาสามารถเลือกโครงสร้างฟังก์ชันหรือรูปแบบกราฟ
ที่ต่างกันได้ หากให้ผลทางฟิสิกส์สอดคล้องกับสมมติฐานและผ่านการตรวจสอบ

แบบจำลองที่รวมอยู่
-------------------
1) Quantum confinement: electron/hole confinement energy ~ 1/R^2
2) Brus-type optical gap: bulk gap + confinement - Coulomb correction
3) Exciton series: E_n = E_continuum - E_binding/n^2
4) Absorption spectrum: Lorentzian exciton peaks + optional continuum
5) Size distribution: deterministic Gaussian quadrature over quantum-dot radii
6) Temperature effects: Varshni-type band-gap shift and phenomenological phonon FWHM

หน่วยที่ใช้
-----------
- radius_nm: nm
- energy_eV: eV
- linewidth_meV: meV
- temperature_K: K
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Physical constants
# -----------------------------------------------------------------------------
E_CHARGE = 1.602176634e-19       # C
H_BAR = 1.054571817e-34          # J s
EPSILON_0 = 8.8541878128e-12     # F/m
M_ELECTRON = 9.1093837015e-31    # kg
K_B_EV_PER_K = 8.617333262e-5    # eV/K

# -----------------------------------------------------------------------------
# Demonstration material parameters: CdSe-like values
# -----------------------------------------------------------------------------
MATERIAL = {
    "name": "CdSe-like",
    "Eg_bulk_eV": 1.74,
    "m_e_eff": 0.13,
    "m_h_eff": 0.45,
    "relative_permittivity": 9.5,
    "Eg_reference_eV": 1.74,
    "T_reference_K": 300.0,
    "varshni_alpha_eV_per_K": 4.5e-4,
    "varshni_beta_K": 180.0,
    "linewidth_residual_meV": 18.0,
    "acoustic_slope_meV_per_K": 0.025,
    "LO_phonon_energy_meV": 25.0,
    "LO_coupling_meV": 38.0,
}


def as_array(values):
    """Convert scalar or sequence to a floating-point NumPy array."""
    return np.asarray(values, dtype=float)


def confinement_energy_eV(radius_nm, effective_mass_ratio):
    """Return particle-in-a-spherical-box confinement energy in eV."""
    radius_m = as_array(radius_nm) * 1e-9
    effective_mass = effective_mass_ratio * M_ELECTRON
    energy_joule = H_BAR**2 * np.pi**2 / (2.0 * effective_mass * radius_m**2)
    return energy_joule / E_CHARGE


def coulomb_correction_eV(radius_nm, material=MATERIAL):
    """Return a Brus-type electron-hole Coulomb correction in eV."""
    radius_m = as_array(radius_nm) * 1e-9
    energy_joule = (
        1.8 * E_CHARGE**2
        / (4.0 * np.pi * EPSILON_0
           * material["relative_permittivity"] * radius_m)
    )
    return energy_joule / E_CHARGE


def temperature_bandgap_eV(temperature_K, material=MATERIAL):
    """Return bulk Eg(T) using a relative Varshni-type expression."""
    temperature = as_array(temperature_K)
    alpha = material["varshni_alpha_eV_per_K"]
    beta = material["varshni_beta_K"]
    tref = material["T_reference_K"]
    eg_ref = material["Eg_reference_eV"]

    varshni_T = alpha * temperature**2 / (temperature + beta)
    varshni_ref = alpha * tref**2 / (tref + beta)
    return eg_ref + varshni_ref - varshni_T


def continuum_onset_eV(radius_nm, temperature_K, material=MATERIAL):
    """Return the electron-hole continuum onset before exciton binding."""
    electron = confinement_energy_eV(radius_nm, material["m_e_eff"])
    hole = confinement_energy_eV(radius_nm, material["m_h_eff"])
    return temperature_bandgap_eV(temperature_K, material) + electron + hole


def exciton_levels_eV(
    radius_nm,
    temperature_K,
    material=MATERIAL,
    n_max=3,
):
    """Return exciton levels, oscillator strengths, onset and binding energy."""
    continuum = float(continuum_onset_eV(radius_nm, temperature_K, material))
    binding = float(coulomb_correction_eV(radius_nm, material))
    n = np.arange(1, n_max + 1, dtype=float)
    levels = continuum - binding / n**2
    oscillator_strength = 1.0 / n**3
    return levels, oscillator_strength, continuum, binding


def lorentzian(energy_eV, center_eV, fwhm_eV):
    """Unit-area Lorentzian line shape."""
    energy = as_array(energy_eV)
    gamma = max(float(fwhm_eV), 1e-12) / 2.0
    return (gamma / np.pi) / ((energy - center_eV)**2 + gamma**2)


def gaussian(energy_eV, center_eV, sigma_eV):
    """Unit-area Gaussian line shape, useful for comparison."""
    energy = as_array(energy_eV)
    sigma = max(float(sigma_eV), 1e-12)
    return np.exp(-0.5 * ((energy - center_eV) / sigma)**2) / (
        sigma * np.sqrt(2.0 * np.pi)
    )


def phonon_linewidth_components_meV(temperature_K, material=MATERIAL):
    """Return residual, acoustic, optical and total FWHM in meV."""
    temperature = np.maximum(as_array(temperature_K), 0.0)
    residual = np.full_like(
        temperature,
        material["linewidth_residual_meV"],
        dtype=float,
    )
    acoustic = material["acoustic_slope_meV_per_K"] * temperature

    occupation = np.zeros_like(temperature, dtype=float)
    positive = temperature > 0.0
    phonon_energy_eV = material["LO_phonon_energy_meV"] / 1000.0
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        exponent = phonon_energy_eV / (K_B_EV_PER_K * temperature[positive])
        occupation[positive] = 1.0 / np.expm1(exponent)

    optical = material["LO_coupling_meV"] * occupation
    total = residual + acoustic + optical
    return {
        "residual_meV": residual,
        "acoustic_meV": acoustic,
        "optical_meV": optical,
        "total_fwhm_meV": total,
        "LO_occupation": occupation,
    }


def exciton_absorption_spectrum(
    energy_grid_eV,
    radius_nm,
    temperature_K,
    material=MATERIAL,
    n_max=1,
    include_continuum=False,
    continuum_strength=0.08,
    linewidth_meV=None,
):
    """Return normalized absorption spectrum and metadata for one dot."""
    energy = as_array(energy_grid_eV)
    levels, strengths, continuum, binding = exciton_levels_eV(
        radius_nm,
        temperature_K,
        material=material,
        n_max=n_max,
    )

    components = phonon_linewidth_components_meV(temperature_K, material)
    if linewidth_meV is None:
        fwhm_meV = float(np.asarray(components["total_fwhm_meV"]))
    else:
        fwhm_meV = float(linewidth_meV)

    absorption = np.zeros_like(energy)
    for level, strength in zip(levels, strengths):
        absorption += strength * lorentzian(
            energy,
            center_eV=level,
            fwhm_eV=fwhm_meV / 1000.0,
        )

    if include_continuum:
        excess = np.maximum(energy - continuum, 0.0)
        continuum_tail = np.sqrt(excess)
        if np.max(continuum_tail) > 0.0:
            continuum_tail /= np.max(continuum_tail)
        absorption += continuum_strength * continuum_tail

    maximum = np.max(absorption)
    if maximum > 0.0:
        absorption /= maximum

    metadata = {
        "levels_eV": levels,
        "strengths": strengths,
        "continuum_eV": continuum,
        "binding_eV": binding,
        "linewidth_fwhm_meV": fwhm_meV,
        "bulk_bandgap_eV": float(
            np.asarray(temperature_bandgap_eV(temperature_K, material))
        ),
    }
    return absorption, metadata


def ensemble_absorption_spectrum(
    energy_grid_eV,
    mean_radius_nm,
    radius_sigma_nm,
    temperature_K,
    material=MATERIAL,
    n_dots=81,
    n_max=1,
    linewidth_meV=None,
    include_continuum=False,
):
    """Average spectra over a deterministic Gaussian size distribution."""
    energy = as_array(energy_grid_eV)
    if radius_sigma_nm <= 0.0:
        return exciton_absorption_spectrum(
            energy,
            mean_radius_nm,
            temperature_K,
            material=material,
            n_max=n_max,
            linewidth_meV=linewidth_meV,
            include_continuum=include_continuum,
        )

    radii = np.linspace(
        max(0.5, mean_radius_nm - 3.0 * radius_sigma_nm),
        mean_radius_nm + 3.0 * radius_sigma_nm,
        int(n_dots),
    )
    weights = np.exp(
        -0.5 * ((radii - mean_radius_nm) / radius_sigma_nm)**2
    )
    weights /= np.sum(weights)

    spectrum = np.zeros_like(energy)
    first_exciton_energies = []
    for radius, weight in zip(radii, weights):
        single, metadata = exciton_absorption_spectrum(
            energy,
            radius,
            temperature_K,
            material=material,
            n_max=n_max,
            linewidth_meV=linewidth_meV,
            include_continuum=include_continuum,
        )
        spectrum += weight * single
        first_exciton_energies.append(metadata["levels_eV"][0])

    maximum = np.max(spectrum)
    if maximum > 0.0:
        spectrum /= maximum

    return spectrum, {
        "radii_nm": radii,
        "weights": weights,
        "first_exciton_energies_eV": np.asarray(first_exciton_energies),
    }


def generate_reference_outputs(
    output_dir="miniproject_solution_outputs",
    material=MATERIAL,
):
    """Generate reference CSV tables and a four-panel reference figure."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    energy_grid = np.linspace(1.60, 3.40, 2600)
    radii_nm = np.array([1.5, 2.5, 4.0, 6.0])
    temperatures_K = np.array([10.0, 100.0, 200.0, 300.0])

    # ------------------------------------------------------------------
    # Table 1: 1s exciton energy versus radius and temperature
    # ------------------------------------------------------------------
    rows = []
    for radius in radii_nm:
        for temperature in temperatures_K:
            levels, _, continuum, binding = exciton_levels_eV(
                radius,
                temperature,
                material=material,
                n_max=1,
            )
            linewidth = float(
                np.asarray(
                    phonon_linewidth_components_meV(temperature, material)[
                        "total_fwhm_meV"
                    ]
                )
            )
            rows.append(
                [
                    radius,
                    temperature,
                    float(temperature_bandgap_eV(temperature, material)),
                    float(levels[0]),
                    float(continuum),
                    float(binding * 1000.0),
                    linewidth,
                    float(1240.0 / levels[0]),
                ]
            )
    table_header = (
        "radius_nm,temperature_K,Eg_bulk_eV,exciton_1s_eV,"
        "continuum_eV,binding_meV,FWHM_meV,wavelength_nm"
    )
    np.savetxt(
        output_path / "reference_peak_table.csv",
        np.asarray(rows),
        delimiter=",",
        header=table_header,
        comments="",
    )

    # ------------------------------------------------------------------
    # Table 2: linewidth components versus temperature
    # ------------------------------------------------------------------
    temp_grid = np.linspace(0.0, 350.0, 351)
    components = phonon_linewidth_components_meV(temp_grid, material)
    linewidth_table = np.column_stack(
        [
            temp_grid,
            components["residual_meV"],
            components["acoustic_meV"],
            components["optical_meV"],
            components["total_fwhm_meV"],
        ]
    )
    np.savetxt(
        output_path / "reference_linewidth_table.csv",
        linewidth_table,
        delimiter=",",
        header="temperature_K,residual_meV,acoustic_meV,optical_meV,total_FWHM_meV",
        comments="",
    )

    # ------------------------------------------------------------------
    # Reference figure
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), constrained_layout=True)
    colors = plt.cm.viridis(np.linspace(0.05, 0.90, len(temperatures_K)))

    # A: size and temperature spectra
    ax = axes[0, 0]
    for radius in radii_nm:
        spectrum, _ = ensemble_absorption_spectrum(
            energy_grid,
            mean_radius_nm=radius,
            radius_sigma_nm=0.0,
            temperature_K=300.0,
            material=material,
            n_max=1,
            linewidth_meV=None,
            include_continuum=True,
        )
        ax.plot(energy_grid, spectrum, linewidth=1.7, label=f"R = {radius:.1f} nm")
    ax.set_title("Size-dependent exciton spectra at 300 K")
    ax.set_xlabel("Photon energy (eV)")
    ax.set_ylabel("Normalized absorption")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    # B: size distribution broadening
    ax = axes[0, 1]
    for sigma, label in [
        (0.0, "sigma_R = 0.00 nm"),
        (0.20, "sigma_R = 0.20 nm"),
        (0.50, "sigma_R = 0.50 nm"),
    ]:
        spectrum, _ = ensemble_absorption_spectrum(
            energy_grid,
            mean_radius_nm=2.5,
            radius_sigma_nm=sigma,
            temperature_K=300.0,
            material=material,
            n_dots=401,
            n_max=1,
            linewidth_meV=None,
            include_continuum=False,
        )
        ax.plot(energy_grid, spectrum, linewidth=1.8, label=label)
    ax.set_title("Inhomogeneous broadening from size distribution")
    ax.set_xlabel("Photon energy (eV)")
    ax.set_ylabel("Normalized absorption")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    # C: temperature-dependent peak and linewidth
    ax = axes[1, 0]
    for temperature, color in zip(temperatures_K, colors):
        spectrum, metadata = exciton_absorption_spectrum(
            energy_grid,
            radius_nm=2.5,
            temperature_K=temperature,
            material=material,
            n_max=3,
            linewidth_meV=None,
            include_continuum=True,
        )
        ax.plot(
            energy_grid,
            spectrum,
            color=color,
            linewidth=1.8,
            label=f"T = {temperature:.0f} K, FWHM = {metadata['linewidth_fwhm_meV']:.1f} meV",
        )
    ax.set_title("Temperature-dependent exciton spectra at R = 2.5 nm")
    ax.set_xlabel("Photon energy (eV)")
    ax.set_ylabel("Normalized absorption")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    # D: temperature-energy map including size distribution
    ax = axes[1, 1]
    map_temperatures = np.linspace(10.0, 300.0, 180)
    map_spectra = []
    for temperature in map_temperatures:
        spectrum, _ = ensemble_absorption_spectrum(
            energy_grid,
            mean_radius_nm=2.5,
            radius_sigma_nm=0.20,
            temperature_K=temperature,
            material=material,
            n_dots=161,
            n_max=1,
            linewidth_meV=None,
            include_continuum=False,
        )
        map_spectra.append(spectrum)
    image = ax.imshow(
        np.asarray(map_spectra),
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
    ax.set_title("Size + temperature: absorption map")
    ax.set_xlabel("Photon energy (eV)")
    ax.set_ylabel("Temperature (K)")
    fig.colorbar(image, ax=ax, label="Normalized absorption")

    fig.suptitle("Reference solution: nanophysics mini-project", fontsize=14)
    figure_path = output_path / "reference_solution_figure.png"
    fig.savefig(figure_path, dpi=180)
    plt.close(fig)

    return {
        "output_dir": str(output_path),
        "peak_table": str(output_path / "reference_peak_table.csv"),
        "linewidth_table": str(output_path / "reference_linewidth_table.csv"),
        "figure": str(figure_path),
    }


def run_reference_checks(material=MATERIAL):
    """Run instructor checks for the main physical limiting cases."""
    checks = {}

    # Check 1: confinement energy should decrease as radius increases.
    e_small = float(confinement_energy_eV(2.0, material["m_e_eff"]))
    e_large = float(confinement_energy_eV(4.0, material["m_e_eff"]))
    checks["confinement_decreases_with_radius"] = e_small > e_large
    checks["approximately_inverse_square"] = np.isclose(e_small / e_large, 4.0, rtol=1e-10)

    # Check 2: at fixed size, the model predicts lower band gap at higher T.
    gap_low_T = float(temperature_bandgap_eV(10.0, material))
    gap_high_T = float(temperature_bandgap_eV(300.0, material))
    checks["bandgap_decreases_with_temperature"] = gap_low_T > gap_high_T

    # Check 3: linewidth should grow over the demonstrated temperature range.
    width_low_T = float(
        np.asarray(phonon_linewidth_components_meV(10.0, material)["total_fwhm_meV"])
    )
    width_high_T = float(
        np.asarray(phonon_linewidth_components_meV(300.0, material)["total_fwhm_meV"])
    )
    checks["linewidth_increases_with_temperature"] = width_high_T > width_low_T

    # Check 4: normalized spectra should be in [0, 1].
    energy = np.linspace(1.6, 3.4, 2500)
    spectrum, _ = ensemble_absorption_spectrum(
        energy,
        mean_radius_nm=2.5,
        radius_sigma_nm=0.20,
        temperature_K=300.0,
        material=material,
    )
    checks["spectrum_normalized"] = (
        np.min(spectrum) >= -1e-12 and np.max(spectrum) <= 1.0 + 1e-12
    )

    # Check 5: sigma -> 0 should match the single-dot spectrum.
    single, _ = exciton_absorption_spectrum(
        energy,
        radius_nm=2.5,
        temperature_K=300.0,
        material=material,
    )
    ensemble_zero, _ = ensemble_absorption_spectrum(
        energy,
        mean_radius_nm=2.5,
        radius_sigma_nm=0.0,
        temperature_K=300.0,
        material=material,
    )
    checks["zero_sigma_matches_single_dot"] = np.allclose(
        single,
        ensemble_zero,
        rtol=1e-12,
        atol=1e-12,
    )

    return checks


def print_reference_summary(material=MATERIAL):
    """Print a compact table that can be copied into an instructor key."""
    print(f"Material: {material['name']}")
    print("\nT (K) | R (nm) | Eg_bulk (eV) | 1s peak (eV) | FWHM (meV) | lambda (nm)")
    print("-" * 82)
    for temperature in [10.0, 100.0, 200.0, 300.0]:
        for radius in [1.5, 2.5, 4.0, 6.0]:
            levels, _, _, _ = exciton_levels_eV(
                radius,
                temperature,
                material=material,
                n_max=1,
            )
            fwhm = float(
                np.asarray(
                    phonon_linewidth_components_meV(temperature, material)[
                        "total_fwhm_meV"
                    ]
                )
            )
            print(
                f"{temperature:5.0f} | {radius:6.2f} | "
                f"{temperature_bandgap_eV(temperature, material):12.4f} | "
                f"{levels[0]:12.4f} | {fwhm:11.2f} | "
                f"{1240.0 / levels[0]:10.1f}"
            )


if __name__ == "__main__":
    print_reference_summary()
    checks = run_reference_checks()
    print("\nReference checks:")
    for name, passed in checks.items():
        print(f"- {name}: {'PASS' if passed else 'FAIL'}")

    if not all(checks.values()):
        raise RuntimeError("At least one reference check failed.")

    outputs = generate_reference_outputs()
    print("\nGenerated reference outputs:")
    for key, value in outputs.items():
        print(f"- {key}: {value}")
