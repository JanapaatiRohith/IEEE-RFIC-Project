from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

results = Path("/mnt/c/IEEE_RFIC_Project/simulation_results")
data_file = results / "hbt_ac_typ_dense.dat"

if not data_file.is_file():
    raise SystemExit(f"Missing simulation data: {data_file}")

data = np.loadtxt(data_file, skiprows=1)

if data.shape != (401, 3):
    raise SystemExit(
        f"Expected 401 rows and 3 columns; got {data.shape}"
    )

freq = data[:, 0]
vout = data[:, 1]
vbase = data[:, 2]

if np.any(freq <= 0) or np.any(vout <= 0) or np.any(vbase <= 0):
    raise SystemExit("Invalid frequency or voltage magnitude in data.")

gain = vout / vbase
gain_db = 20 * np.log10(gain)
output_db = 20 * np.log10(vout)

# Use the output magnitude at 100 kHz as the reference.
ref_idx = int(np.argmin(np.abs(freq - 100e3)))
ref_freq = freq[ref_idx]
ref_vout = vout[ref_idx]
target_db = 20 * np.log10(ref_vout) - 10 * np.log10(2)

# Find the first crossing after the reference frequency.
crossings = np.where(
    (np.arange(len(freq)) > ref_idx)
    & (output_db <= target_db)
)[0]

cutoff = None

if len(crossings):
    j = int(crossings[0])
    f1, f2 = freq[j - 1], freq[j]
    y1, y2 = output_db[j - 1], output_db[j]

    # Interpolate in dB against logarithmic frequency.
    log_f = np.log10(f1) + (
        (target_db - y1) / (y2 - y1)
    ) * (np.log10(f2) - np.log10(f1))
    cutoff = 10 ** log_f

# Plot collector-output magnitude and the -3 dB threshold.
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.semilogx(freq, vout, linewidth=2, label="Collector magnitude")
ax.axvline(ref_freq, linestyle=":", label="100 kHz reference")
ax.axhline(
    ref_vout / np.sqrt(2),
    linestyle="--",
    label="Reference magnitude −3 dB"
)
if cutoff is not None:
    ax.axvline(cutoff, linestyle="--", label=f"Cutoff ≈ {cutoff/1e6:.3f} MHz")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("|Vcollector| (V)")
ax.set_title("IHP SG13G2 HBT — Dense AC Output Response")
ax.grid(True, which="both", alpha=0.35)
ax.legend()
fig.tight_layout()
fig.savefig(results / "hbt_ac_output_magnitude_dense.png", dpi=180)
plt.close(fig)

# Plot voltage gain.
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.semilogx(freq, gain_db, linewidth=2)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Voltage gain (dB)")
ax.set_title("IHP SG13G2 HBT — Dense Base-to-Collector Gain")
ax.grid(True, which="both", alpha=0.35)
fig.tight_layout()
fig.savefig(results / "hbt_ac_gain_db_dense.png", dpi=180)
plt.close(fig)

summary = [
    "IHP SG13G2 HBT Dense AC Analysis",
    f"Data points: {len(freq)}",
    f"Frequency range: {freq[0]:.8g} to {freq[-1]:.8g} Hz",
    f"Reference frequency: {ref_freq:.8g} Hz",
    f"Collector magnitude at reference: {ref_vout:.8g} V",
    f"Base-to-collector gain at reference: {gain[ref_idx]:.8g} V/V",
    f"Voltage gain at reference: {gain_db[ref_idx]:.5f} dB",
]

if cutoff is not None:
    summary.append(f"Estimated magnitude-based -3 dB frequency: {cutoff:.8g} Hz")
else:
    summary.append("No -3 dB crossing found within the simulated range.")

summary.extend([
    "Plots:",
    "hbt_ac_output_magnitude_dense.png",
    "hbt_ac_gain_db_dense.png",
])

summary_text = "\n".join(summary) + "\n"
(results / "hbt_ac_dense_summary.txt").write_text(summary_text)
print(summary_text)
