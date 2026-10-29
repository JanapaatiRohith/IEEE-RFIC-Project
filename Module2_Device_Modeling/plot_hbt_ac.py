from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

results = Path("/mnt/c/IEEE_RFIC_Project/simulation_results")
data_file = results / "hbt_ac_typ.dat"

if not data_file.exists():
    raise SystemExit(f"Missing AC data: {data_file}")

data = np.loadtxt(data_file, skiprows=1)

if data.ndim != 2 or data.shape[1] < 3:
    raise SystemExit("Expected frequency, collector magnitude and base magnitude.")

freq = data[:, 0]
vout = data[:, 1]
vbase = data[:, 2]

if np.any(freq <= 0) or np.any(vbase <= 0):
    raise SystemExit("Invalid frequency or base-voltage values.")

gain = vout / vbase
gain_db = 20 * np.log10(gain)

# Plot collector output magnitude.
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.semilogx(freq, vout, marker="o", markersize=3)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("|Vcollector| (V)")
ax.set_title("IHP SG13G2 HBT — Collector AC Response")
ax.grid(True, which="both", alpha=0.35)
fig.tight_layout()
fig.savefig(results / "hbt_ac_output_magnitude.png", dpi=180)
plt.close(fig)

# Plot voltage gain from the base node to collector.
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.semilogx(freq, gain_db, marker="o", markersize=3)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Voltage gain (dB)")
ax.set_title("IHP SG13G2 HBT — Base-to-Collector Gain")
ax.grid(True, which="both", alpha=0.35)
fig.tight_layout()
fig.savefig(results / "hbt_ac_gain_db.png", dpi=180)
plt.close(fig)

# Independently estimate the 3 dB point relative to the output
# magnitude at 100 kHz. This is a sampled-data estimate.
i0 = int(np.argmin(np.abs(freq - 100e3)))
reference_mag = vout[i0]
target = reference_mag / np.sqrt(2)

crossings = np.where(
    (np.arange(len(freq)) > i0) & (vout <= target)
)[0]

print("========== HBT AC SUMMARY ==========")
print(f"Data points: {len(freq)}")
print(f"Frequency range: {freq[0]:.6g} to {freq[-1]:.6g} Hz")
print(f"Collector magnitude at {freq[i0]:.6g} Hz: {reference_mag:.6g} V")
print(f"Base-to-collector gain at that point: {gain[i0]:.6g}")
print(f"Gain in dB at that point: {gain_db[i0]:.3f} dB")

if len(crossings):
    j = int(crossings[0])
    if j > i0:
        # Interpolate in log-frequency between the surrounding points.
        f1, f2 = freq[j - 1], freq[j]
        y1, y2 = vout[j - 1], vout[j]
        if y1 != y2 and y1 > target >= y2:
            log_f = np.log10(f1) + (
                (target - y1) / (y2 - y1)
            ) * (np.log10(f2) - np.log10(f1))
            print(f"Estimated magnitude-based 3 dB frequency: {10**log_f:.6g} Hz")
        else:
            print(f"First sampled point at/below 3 dB target: {freq[j]:.6g} Hz")
else:
    print("No 3 dB crossing relative to 100 kHz was found in the sweep range.")

print("Saved hbt_ac_output_magnitude.png")
print("Saved hbt_ac_gain_db.png")
