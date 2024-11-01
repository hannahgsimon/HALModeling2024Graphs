import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

class HALModeling2024Graphs:

    plot_with_CIs = True
    scenarioAnalysis = False
    scenario = 'D'
    timesteps500 = True

    if plot_with_CIs and scenarioAnalysis:
        print("Error: plot_with_CIs and scenarioAnalysis cannot be true simultaneously.")
        sys.exit()
    
    # Specify the full path to the CSV file
    if not plot_with_CIs:
        file_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunCounts.csv'
        if scenarioAnalysis:
            folder_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\Scenario{scenario}\*.csv'
            all_files = glob.glob(folder_path)
            # Sort the files alphabetically and select the last one
            if all_files:
                file_path = sorted(all_files)[-1]  # Last file in alphabetical order
                print("Last file in alphabetical order:", file_path)
            else:
                print("No CSV files found.")
        
        # Read the data from the CSV file
        df = pd.read_csv(file_path)

        timestep = 302
        tumor_cells_at_timestep = df.loc[df['Timestep'] == timestep, 'TumorCells']
        if not tumor_cells_at_timestep.empty:
            print(f"Number of tumor cells at timestep {timestep}: {tumor_cells_at_timestep.values[0]}")
        else:
            print(f"Timestep {timestep} not found in the data.")

        # Extract data for plotting
        Timestep = df['Timestep']
        lymphocyte_cells = df['Lymphocytes']
        triggering_cells = df['TriggeringCells']
        tumor_cells = df['TumorCells']
        doomed_cells = df['DoomedCells']

        plt.figure(figsize=(8,6))

        plt.plot(Timestep, lymphocyte_cells, label='Lymphocytes', marker='o', color='blue', markersize = 1)
        plt.plot(Timestep, triggering_cells, label='Triggering Cells', marker='*', color='green', markersize=1)
        plt.plot(Timestep, tumor_cells, label='Tumor Cells', marker='s', color='red', markersize = 1)
        plt.plot(Timestep, doomed_cells, label='Doomed Cells', marker='^', color='gold', markersize = 1)

    if plot_with_CIs:
        print("Scenario:", scenario)
        file_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\Scenario{scenario}\*.csv'
        all_files = glob.glob(file_path)
        
        # Initialize lists for plotting
        Timestep = []
        lymphocyte_cells = []
        triggering_cells = []
        tumor_cells = []
        doomed_cells = []

        # Check if scenario is C or D
        if scenario in ['C', 'D']:
            included_files = []  # List to keep track of included files
            # Read each file and append the data only if max timestep >= 200
            for file in all_files:
                df = pd.read_csv(file)

                # Check if the maximum timestep is 200 or more, to include include escape trials
                if df['Timestep'].max() >= 200:
                    Timestep.append(df['Timestep'])
                    lymphocyte_cells.append(df['Lymphocytes'])
                    triggering_cells.append(df['TriggeringCells'])
                    tumor_cells.append(df['TumorCells'])
                    doomed_cells.append(df['DoomedCells'])
                    included_files.append(os.path.basename(file))  # Add only the filename to the list
            '''print("Included files:")
            for filename in included_files:
                print(filename)'''

        else:
            # Read all files normally for other scenarios
            for file in all_files:
                df = pd.read_csv(file)
                Timestep.append(df['Timestep'])
                lymphocyte_cells.append(df['Lymphocytes'])
                triggering_cells.append(df['TriggeringCells'])
                tumor_cells.append(df['TumorCells'])
                doomed_cells.append(df['DoomedCells'])

        # Convert lists to DataFrames
        Timestep = pd.concat(Timestep).reset_index(drop=True)
        if timesteps500:
            Timestep = Timestep[Timestep <= 500]
        lymphocyte_cells = pd.concat(lymphocyte_cells).reset_index(drop=True)
        triggering_cells = pd.concat(triggering_cells).reset_index(drop=True)
        tumor_cells = pd.concat(tumor_cells).reset_index(drop=True)
        doomed_cells = pd.concat(doomed_cells).reset_index(drop=True)

        if timesteps500:
            # Filter lymphocyte, triggering, tumor, and doomed cells based on the filtered Timestep
            lymphocyte_cells = lymphocyte_cells[Timestep.index]
            triggering_cells = triggering_cells[Timestep.index]
            tumor_cells = tumor_cells[Timestep.index]
            doomed_cells = doomed_cells[Timestep.index]

        # Create a DataFrame to calculate means and stds
        mean_df = pd.DataFrame({
            'Timestep': Timestep,
            'Lymphocyte': lymphocyte_cells,
            'TriggeringCells': triggering_cells,
            'TumorCells': tumor_cells,
            'DoomedCells': doomed_cells
        })

        # Group by 'Timestep' and calculate mean and std
        mean_values = mean_df.groupby('Timestep').agg(['mean', 'std']).reset_index()

        # Calculate means and standard deviations for confidence intervals
        lymphocyte_mean = lymphocyte_cells.mean()
        lymphocyte_std = lymphocyte_cells.std()
        triggering_mean = triggering_cells.mean()
        triggering_std = triggering_cells.std()
        tumor_mean = tumor_cells.mean()
        tumor_std = tumor_cells.std()
        doomed_mean = doomed_cells.mean()
        doomed_std = doomed_cells.std()

        plt.figure(figsize=(10, 6))

        # Error bars with lighter colors (confidence intervals) and transparency
        plt.errorbar(mean_values['Timestep'], mean_values['Lymphocyte']['mean'], 
                     yerr=mean_values['Lymphocyte']['std'],
                     marker='', color='#66B2FF', markersize=0, capsize=3)
        plt.errorbar(mean_values['Timestep'], mean_values['TriggeringCells']['mean'], 
                     yerr=mean_values['TriggeringCells']['std'],
                     marker='', color='lightgreen', markersize=0, capsize=3)
        plt.errorbar(mean_values['Timestep'], mean_values['TumorCells']['mean'], 
                     yerr=mean_values['TumorCells']['std'],
                     marker='', color='lightpink', markersize=0, capsize=3, alpha=0.3)
        plt.errorbar(mean_values['Timestep'], mean_values['DoomedCells']['mean'], 
                     yerr=mean_values['DoomedCells']['std'],
                     marker='', color='#FFFF4C', markersize=0, capsize=3, alpha=0.2) #lower alpha values are more transparent

        # Mean values with regular colors
        plt.errorbar(mean_values['Timestep'], mean_values['Lymphocyte']['mean'], 
                     yerr=None, label='Lymphocytes', 
                     marker='o', color='blue', markersize=1, capsize=3)
        plt.errorbar(mean_values['Timestep'], mean_values['TriggeringCells']['mean'], 
                     yerr=None, label='Triggering Cells', 
                     marker='*', color='green', markersize=1, capsize=3)
        plt.errorbar(mean_values['Timestep'], mean_values['TumorCells']['mean'], 
                     yerr=None, label='Tumor Cells', 
                     marker='s', color='red', markersize=1, capsize=3)
        plt.errorbar(mean_values['Timestep'], mean_values['DoomedCells']['mean'], 
                     yerr=None, label='Doomed Cells', 
                     marker='^', color='#D1A600', markersize=1, capsize=3)

        plt.title(f"Scenario {scenario}", fontsize=30)
        
    plt.xlabel('Timestep', fontsize = 24)
    plt.ylabel('Cell Count', fontsize = 24)
    plt.tick_params(axis='both', labelsize=16)

    plt.legend()
    plt.legend(prop={'size': 14})
    plt.grid(True)
    save_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunGraphScenario{scenario}.png'
    plt.savefig(save_path, dpi=600, bbox_inches='tight')

    # Immune Graph
    graph_immune = False
    if graph_immune:
        primary_immune_response = df['PrimaryImmuneResponse']
        secondary_immune_response = df['SecondaryImmuneResponse']
        immune_response = df['ImmuneResponse']
        plt.figure(figsize=(8, 6))
        plt.plot(Timestep, immune_response, label='Total Immune Response', marker='o', color='black', markersize=1)
        plt.plot(Timestep, primary_immune_response, label='Primary Immune Response', marker='s', color='purple', markersize=1)
        plt.plot(Timestep, secondary_immune_response, label='Secondary Immune Response', marker='^', color='brown', markersize=1)
        plt.xlabel('Timestep')
        plt.ylabel('Immune Response')
        plt.legend()
        plt.grid(True)
        save_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunGraphImmuneResponse.png'
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.show()
