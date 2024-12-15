# HALModeling2024Graphs

## Overview
The **HALModeling2024Graphs** repository contains Python scripts to generate and analyze graphs for the HALModeling2024 project, found at https://github.com/hannahgsimon/HALModeling2024. This project focuses on visualizing various tumor and immune system interactions using graph-based representations, particularly in the context of immunology and cancer research.

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
- **Graph Generation**: Generates various plots to visualize tumor dynamics, immune response, and cell migration.
- **Data Analysis**: Processes simulation data and computes key metrics like tumor growth rate, infiltration rate, and immune suppression.

## Usage
Before running the code, you will need to update the file paths.  
In HALModeling2024Graphs.py:  
  ```python
  file_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunCounts.csv'
  folder_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\Scenario{scenario}\*.csv'
  file_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\Scenario{scenario}\*.csv'
  save_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunGraphScenario{scenario}.png'
  save_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunGraphImmuneResponse.png'
   ```
In HALModeling2024Plots.py:  
  ```python
  file_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\AvgTimestepstoEscape.csv'
  timesteps_save_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\BoxplotTimesteps.png'
  tumorcells_save_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\BoxplotTumorCells.png'
  ```
##### Usage in HALModeling2024Graphs.py:
- Input: TrialRunCounts.csv. Data of the last trial (general, not a scenario), a product of `printCounts = true` and `scenarioActive = true` in OnLattice2DGrid.java.
- Input: A folder of trials of a specific scneario, a product of `scenarioActive = true` and `printCounts = true` and `scenarioActive = true`
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
- **<ins>Timesteps 500</ins>:** Enabled. For `plot_with_CIs = True`, will only plot the first 500 timesteps. In the original OnLattice2DGrid.java code, that is the timestep by which the triggering cell population reaches 0 since there are 500 initial triggering cells and 1 is removed from the grid every timestep; it may reach 0 sooner if cells are killed due to radiation.
     ```python
    timesteps500 = True
     ```
- **<ins>Plot Immune Response</ins>:** Enabled. Plots the total immune response, primary immune response, and secondary immune response at each timestep. If `scenarioAnalysis = True`, plots the data for the indicated scenario. If `scenarioAnalysis = False`, plots the data for the last trial (titled TrialRunCounts.csv, not a specific scenario).
     ```python
    graph_immune = True
     ```
- Note: When both `plot_with_CIs = False` and `scenarioAnalysis = False`, for the last trial (titled TrialRunCounts.csv, not a specific scenario), plots the cell counts at each timestep.
#### Usage in HALModeling2024Plots.py:
- Input: A CSV file with 5 columns: "Scenario", "Trial" number, "Bifurcation to Escape" (Y/N), "Timesteps to Equilibrium", and "Tumor Cells at Equilibrium". The last 2 columns are blank for non-escape trials.

  Output: For trials in which bifurcation to escape occurred,
- Plots a box and whisker plot of the number of tumor cells at equilibrium across each scenario.
- Plots a box and whisker plot of the number of timesteps to equilibrium across each scenario.

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
