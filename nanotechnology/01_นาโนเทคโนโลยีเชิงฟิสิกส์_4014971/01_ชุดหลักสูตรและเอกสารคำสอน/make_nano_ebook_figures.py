from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUT = Path('/home/ubuntu/nano_ebook_assets')
OUT.mkdir(exist_ok=True)

plt.rcParams.update({'font.family': 'DejaVu Sans', 'axes.titleweight': 'bold', 'font.size': 11})

# Figure 1: Surface-area-to-volume scaling for a sphere (values in arbitrary units)
d = np.geomspace(1, 1000, 300)
sa_to_v = 6 / d
fig, ax = plt.subplots(figsize=(9, 5), dpi=180)
ax.plot(d, sa_to_v, color='#6ee7ff', lw=3)
ax.set_xscale('log'); ax.set_yscale('log')
ax.set_xlabel('Particle diameter (arbitrary unit, log scale)')
ax.set_ylabel('Surface area / volume (arbitrary unit, log scale)')
ax.set_title('Size reduction increases surface-area-to-volume ratio')
ax.grid(True, which='both', alpha=.25)
ax.annotate('Smaller particles\n→ larger surface contribution', xy=(5, 1.2), xytext=(25, 2.5),
            arrowprops={'arrowstyle': '->', 'color': '#fbbf24'}, color='#7c2d12', fontsize=10)
fig.tight_layout(); fig.savefig(OUT/'fig_surface_area_ratio.png', transparent=False, facecolor='white'); plt.close(fig)

# Figure 2: Simulated DLS distributions
x = np.linspace(1, 250, 600)
def normal(mu, sigma, amp=1):
    return amp * np.exp(-0.5*((x-mu)/sigma)**2)
y1 = normal(48, 10, 1.0)
y2 = normal(105, 28, .55)
fig, ax = plt.subplots(figsize=(9,5), dpi=180)
ax.plot(x, y1, label='Condition A (simulated)', color='#2563eb', lw=2.5)
ax.plot(x, y2, label='Condition B (simulated)', color='#f97316', lw=2.5)
ax.set_xlabel('Hydrodynamic diameter (nm)')
ax.set_ylabel('Relative intensity (arbitrary unit)')
ax.set_title('Example of simulated size distributions for discussion')
ax.legend(frameon=False); ax.grid(axis='y', alpha=.25)
ax.text(0.01, -0.23, 'Teaching data only: interpret with sample preparation and measurement conditions.', transform=ax.transAxes, fontsize=9, color='#555')
fig.tight_layout(); fig.savefig(OUT/'fig_simulated_dls.png', transparent=False, facecolor='white'); plt.close(fig)

# Figure 3: Means with uncertainty from a simulated repeated measurement
conditions = ['A', 'B', 'C']
means = np.array([52, 71, 95])
sd = np.array([5, 9, 14])
fig, ax = plt.subplots(figsize=(8,5), dpi=180)
colors = ['#1d4ed8','#0891b2','#7c3aed']
ax.bar(conditions, means, yerr=sd, capsize=7, color=colors, alpha=.9)
ax.set_ylim(0, 130); ax.set_xlabel('Measurement condition'); ax.set_ylabel('Mean diameter (nm)')
ax.set_title('Reporting repeated measurements with variability (simulated)')
ax.grid(axis='y', alpha=.25)
for i, v in enumerate(means):
    ax.text(i, v+sd[i]+4, f'{v} ± {sd[i]}', ha='center', fontsize=10)
fig.tight_layout(); fig.savefig(OUT/'fig_uncertainty_bars.png', transparent=False, facecolor='white'); plt.close(fig)

print('Figures written to', OUT)
