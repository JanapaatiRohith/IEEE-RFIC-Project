from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

data_file = Path(
    "/mnt/c/IEEE_RFIC_Project/simulation_results/ihp_hbt_dc_sweep.dat"
)
out_dir = data_file.parent

if not data_file.is_file():
    raise SystemExit(f"Missing data file: {data_file}")

data = np.loadtxt(data_file, skiprows=1)

if data.ndim != 2 or data.shape[1] < 3:
    raise SystemExit("Expected columns: VCE, IB, IC")

vce = data[:, 0]
ib = data[:, 1]
ic = data[:, 2]

base_levels = np.unique(np.round(ib, 12))

fig, ax = plt.subplots(figsize=(10, 6))

for base_current in base_levels:
    mask = np.isclose(ib, base_current, atol=1e-12, rtol=0)
    order = np.argsort(vce[mask])

    x = vce[mask][order]
    y = np.abs(ic[mask][order]) * 1e3

    ax.plot(x, y, linewidth=1.8,
            label=f"IB = {base_current * 1e6:.1f} µA")

ax.set_xlabel("Collector-emitter voltage VCE (V)")
ax.set_ylabel("Collector current magnitude |IC| (mA)")
ax.set_title("IHP SG13G2 SiGe HBT Output Characteristics")
ax.grid(True, alpha=0.35)
ax.legend(title="Base current", ncol=2)
fig.tight_layout()

plot_path = out_dir / "hbt_ic_vce_typ.png"
fig.savefig(plot_path, dpi=200)
plt.close(fig)

print("========== HBT SWEEP SUMMARY ==========")
print(f"Data points: {len(data)}")
print(f"VCE range: {vce.min():.2f} V to {vce.max():.2f} V")
print(f"Base-current levels: {len(base_levels)}")
print(f"Base-current range: {ib.min()*1e6:.2f} to {ib.max()*1e6:.2f} µA")
print(f"Collector-current magnitude range: "
      f"{np.abs(ic).min()*1e3:.6f} to "
      f"{np.abs(ic).max()*1e3:.6f} mA")
print(f"Saved graph: {plot_path}")
