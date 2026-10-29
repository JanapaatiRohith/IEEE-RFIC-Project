# IEEE RFIC — Device Modeling Progress Report

## Environment
- OS: Ubuntu 24.04 under WSL 2
- EDA: eSim 2.6
- Simulator: Ngspice 45
- PDK: IHP SG13G2
- PDK root: IHP SG13G2 PDK installed separately; model libraries are external to this repository.

## 1. NMOS DC Operating Point
- Gate voltage: 0.4 V
- Drain voltage: 1.0 V
- Drain current magnitude: 1.145623 uA
- Status: Simulation completed

## 2. NMOS DC Transfer Sweep
- Gate-voltage range: 0 to 1.2 V
- Step: 0.01 V
- Data points: 121
- Maximum measured current: 388.624551 uA
- Status: Simulation and plots generated

## 3. SiGe HBT DC Output Characteristics
- Device: npn13G2
- Process corner: hbt_typ
- Temperature: 27 C
- VCE range: 0.01 to 1.50 V
- Base-current range: 0.50 to 5.00 uA
- Data points: 1500
- Collector-current magnitude range: 0.013216 to 2.337222 mA
- Status: Simulation and plot generated

## 4. SiGe HBT AC Response
- Process corner: hbt_typ
- Frequency range: 10 kHz to 100 MHz
- Frequency samples: 401
- Collector magnitude at 100 kHz: 0.12618199 V
- Base-to-collector voltage gain at 100 kHz: 145.53264 V/V
- Voltage gain at 100 kHz: 43.25921 dB
- Estimated magnitude-based -3 dB frequency: 17.975386 MHz
- Reference circuit: IHP PDK HBT AC testbench
- Status: Simulation, data export, analysis, and plots generated

## Key Results
- simulation_results/nmos_id_vgs.dat
- simulation_results/nmos_id_vgs_linear.png
- simulation_results/nmos_id_vgs_semilog.png
- simulation_results/ihp_hbt_dc_sweep.dat
- simulation_results/hbt_ic_vce_typ.png
- simulation_results/hbt_ac_typ_dense.dat
- simulation_results/hbt_ac_dense_summary.txt
- simulation_results/hbt_ac_output_magnitude_dense.png
- simulation_results/hbt_ac_gain_db_dense.png

## Limitations and Next Work
These are device-model validation exercises using reference testbenches.
The 17.975386 MHz result is an estimated -3 dB point for the reference
HBT AC circuit; it is not a verified LNA bandwidth.

Next:
1. Compare these exercises with the official Module 2 deliverables.
2. Complete any remaining required device-modeling exercises.
3. Begin the assigned RF amplifier/LNA design.
4. Verify its gain, matching, stability, noise performance, and bandwidth
   according to the course specifications.
5. Package all source files, raw data, plots, logs, and documentation.
