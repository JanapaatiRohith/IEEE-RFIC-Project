# Module 2 — Device Modeling

This module contains NMOS and HBT ngspice decks, Python analysis scripts,
and device-modeling results.

## Dependencies

- ngspice
- Python and the dependencies required by the analysis scripts
- IHP SG13G2 PDK, installed separately

## Running on another machine

The NMOS netlists currently reference the PDK through a local absolute path.
Before running them on another machine, update the `.lib` statements to point
to that machine's IHP SG13G2 model-library installation.

The PDK and its model libraries are not included in this repository.

## Results

The `../simulation_results/` directory contains saved simulation datasets,
logs, measurements, and plots. See the preliminary report in `../reports/`.
