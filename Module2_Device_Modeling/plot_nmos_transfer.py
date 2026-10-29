from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

data_file = Path(
    "/mnt/c/IEEE_RFIC_Project/simulation_results/nmos_id_vgs.dat"
)
output_dir = data_file.parent

if not data_file.is_file():
    raise SystemExit(f"Missing simulation data: {data_file}")

data = np.loadtxt(data_file, skiprows=1)

if data.ndim != 2 or data.shape[1] < 2:
    raise SystemExit("Unexpected data format; expected two columns.")

vgs = data[:, 0]
id_a = data[:, 1]
id_ua = id_a * 1e6

# Linear transfer characteristic
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(vgs, id_ua, linewidth=2)
ax.set_xlabel("Gate voltage VGS (V)")
ax.set_ylabel("Drain current ID (µA)")
ax.set_title("IHP SG13G2 NMOS Transfer Curve — Linear Scale")
ax.grid(True, alpha=0.35)
fig.tight_layout()
fig.savefig(output_dir / "nmos_id_vgs_linear.png", dpi=180)
plt.close(fig)

# Logarithmic view for low-current behaviour
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.semilogy(vgs, np.maximum(np.abs(id_ua), 1e-15), linewidth=2)
ax.set_xlabel("Gate voltage VGS (V)")
ax.set_ylabel("|Drain current ID| (µA)")
ax.set_title("IHP SG13G2 NMOS Transfer Curve — Log Scale")
ax.grid(True, which="both", alpha=0.35)
fig.tight_layout()
fig.savefig(output_dir / "nmos_id_vgs_semilog.png", dpi=180)
plt.close(fig)

index_04 = np.argmin(np.abs(vgs - 0.4))
imax = np.argmax(id_a)

print("========== SWEEP SUMMARY ==========")
print(f"Data points: {len(vgs)}")
print(f"VGS range: {vgs[0]:.2f} V to {vgs[-1]:.2f} V")
print(f"ID at VGS={vgs[index_04]:.2f} V: {id_ua[index_04]:.6f} µA")
print(f"Maximum measured ID: {id_ua[imax]:.6f} µA")
print(f"VGS at maximum measured ID: {vgs[imax]:.2f} V")
print("Saved: nmos_id_vgs_linear.png")
print("Saved: nmos_id_vgs_semilog.png")
