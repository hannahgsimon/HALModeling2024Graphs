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
4. Build the project to ensure all dependencies are resolved.

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
<br>
The simulation starts with the below initial conditions (modifiable in the code). You can update these parameters in the indicated lines of code to fit your specific simulation requirements.
- **<ins>Plot with Confidence Intervals</ins>:** Enabled.
     ```python
    plot_with_CIs = True
     ```
- **<ins>Scenario Analysis</ins>:** Disabled.
     ```python
     scenarioAnalysis = False
     ```
- **<ins>Scenario</ins>:** A. When `scenarioAnalysis = True`, the indicated scenario will be graphed.
     ```python
    scenario = 'A'
     ```
- **<ins>Timesteps 500</ins>:** Enabled.
     ```python
    timesteps500 = True
     ```
- **<ins>Plot Immune Response</ins>:** Enabled.
     ```python
    graph_immune = True
     ```
                    
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
