# HALModeling2024Graphs

## Overview
The HALModeling2024Graphs repository contains Python scripts to generate and analyze graphs for the HALModeling2024 project, found at https://github.com/hannahgsimon/HALModeling2024. This code graphs cell population changes in response to radiotherapy, as well as the immune response.

## Prerequisites
- **Python**: Version 3.6 or higher.
- **Required Python packages**: You can install them using `pip`:
   ```bash
   pip install pandas matplotlib

## Installation
1. Clone the repository:
    - git clone https://github.com/hannahgsimon/HALModeling2024Graphs.git
2. Navigate to the project directory with the cd command.
3. Import the project into your preferred Python IDE.
4. Build the project.

## Features
- **<ins>Plot Trial Cell Populations</ins>:** Plots cell counts at each timestep for the last trial.
- **<ins>Plot Trial Immune Response</ins>:** Plots the total immune response, primary immune response, and secondary immune response at each timestep.
- **<ins>Plot Scenario Cell Populations with Confidence Intervals</ins>:** For the indicated scenario, plots the average cell counts with confidence intervals (±1 SD) at each timestep across all trials. For scenarios C, D, and E, will only plot trials with initial escape & radiation.
- **<ins>Plot Tumor Cells at Equilibrium</ins>:** For trials in which bifurcation to escape occurred, plots a box and whisker plot of the number of tumor cells at equilibrium across each scenario.
- **<ins>Plot Timesteps to Equilibrium</ins>:** For trials in which bifurcation to escape occurred, plots a box and whisker plot of the number of timesteps to equilibrium across each scenario.

## Usage
Before running the code, you will need to update the file paths.  
In `HALModeling2024Graphs.py`:  
  ```python
  file_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunCounts.csv'
  folder_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\Scenario{scenario}\*.csv'
  file_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\Scenario{scenario}\*.csv'
  save_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunGraphScenario{scenario}.png'
  save_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunGraphImmuneResponse.png'
   ```
In `HALModeling2024Plots.py`:  
  ```python
  file_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\AvgTimestepstoEscape.csv'
  timesteps_save_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\BoxplotTimesteps.png'
  tumorcells_save_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\BoxplotTumorCells.png'
  ```
##### Usage in `HALModeling2024Graphs.py`:
- Input 1: `TrialRunCounts.csv` — Contains data from the final trial (non-scenario-specific), generated when `printCounts = true` and `scenarioActive = false` in `OnLattice2DGrid.java`.
- Input 2: A folder containing trials for a specific scenario, generated when `printCounts = true` and `scenarioActive = true` in `OnLattice2DGrid.java`.

The simulation starts with the below initial conditions (modifiable in the code). You can update these parameters in the indicated lines of code to fit your specific simulation requirements.
- **<ins>Plot with Confidence Intervals</ins>:** Disabled. For the indicated scenario, plots the average cell counts with confidence intervals (±1 SD) at each timestep across all trials. For scenarios C, D, and E, will only plot trials with initial escape & radiation.
     ```python
    plot_with_CIs = False
     ```
- **<ins>Scenario Analysis</ins>:** Disabled. For the last trial of the indicated scenario, plots the cell counts at each timestep.
     ```python
     scenarioAnalysis = False
     ```
- **<ins>Scenario</ins>:** A. The indicated scenario that will be graphed for `plot_with_CIs = True` or `scenarioAnalysis = True`.
     ```python
    scenario = 'A'
     ```
- **<ins>Timesteps 500</ins>:** Enabled. For `plot_with_CIs = True`, only the first 500 timesteps are plotted.  In the original `OnLattice2DGrid.java` code, this corresponds to the time by which the triggering cell population typically reaches 0. This occurs because there are initially 500 triggering cells, with 1 removed per timestep; however, the population may reach 0 sooner if cells are killed by radiation.
     ```python
    timesteps500 = True
     ```
- **<ins>Plot Immune Response</ins>:** Enabled. Plots the total immune response, primary immune response, and secondary immune response at each timestep. If `scenarioAnalysis = True`, plots the data for the last trial of the indicated scenario. If `scenarioAnalysis = False`, plots the data for the last trial (titled `TrialRunCounts.csv`, not a specific scenario).
     ```python
    graph_immune = True
     ```
- Note: When both `plot_with_CIs = False` and `scenarioAnalysis = False`, plots cell counts at each timestep for the last trial (`TrialRunCounts.csv`, not tied to a specific scenario).

#### Usage in `HALModeling2024Plots.py`:
- Input: A CSV file with 5 columns: "Scenario", "Trial" number, "Bifurcation to Escape" (Y/N), "Timesteps to Equilibrium", and "Tumor Cells at Equilibrium". The last 2 columns are blank for non-escape trials.
- Output 1: For trials in which bifurcation to escape occurred, plots a box and whisker plot of the number of tumor cells at equilibrium across each scenario.
- Output 2: For trials in which bifurcation to escape occurred, plots a box and whisker plot of the number of timesteps to equilibrium across each scenario.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    - git checkout -b feature-name
3. Commit your changes and push the branch:
    - git commit -m "Add new feature"
    - git push origin feature-name
4. Open a pull request and describe your changes in detail.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, please contact Hannah G. Simon at hgsimon2@gmail.com.
