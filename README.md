# IEEE RFIC Project

This repository organizes the RFIC project into three modules:
eSim setup, IHP device modeling, and LNA design.

## Project structure

- `Module1_eSim/` — eSim and IHP device setup documentation.
- `Module2_Device_Modeling/` — ngspice decks and Python analysis scripts
  for NMOS and HBT device characterization.
- `Module3_LNA_Design/` — workspace and planned steps for LNA design.
- `reports/` — setup validation and preliminary modeling reports.
- `simulation_results/` — simulation data, logs, measurements, and plots.
- `downloads/` — local downloads are not intended to be version controlled.

## Current status

### Module 1 — eSim setup
The setup-validation report is in `reports/Module1_eSim_Setup_Validation.md`.
The repository does not currently contain a complete, reproducible Module 1
schematic and simulation-result package.

### Module 2 — Device modeling
The repository includes NMOS DC characterization, HBT DC output
characterization, HBT AC analysis, plotting scripts, and recorded results.
The preliminary report is in `reports/Module2_Device_Modeling_Preliminary_Report.md`.

### Module 3 — LNA design
This is a planned workspace. An LNA circuit, design specifications,
and verified LNA simulation results have not yet been added.

## Tools and dependencies

The project uses ngspice, Python plotting/analysis tools, and the IHP
SG13G2 process design kit for the relevant simulations. Install these
separately and configure local model-library paths as required.

The PDK and its model libraries are not bundled with this repository.
The eSim installer is also excluded.

## Reproducibility

Review the model-library paths in the simulation decks before running
them on another machine. The stored logs, datasets, and plots document
the runs available at the time of this repository snapshot.
