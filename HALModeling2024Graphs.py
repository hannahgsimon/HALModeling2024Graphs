import pandas as pd
import matplotlib.pyplot as plt

class HALModeling2024Graphs:
    # Specify the full path to the CSV file
    file_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunCounts.csv'

    # Read the data from the CSV file
    df = pd.read_csv(file_path)

    # Extract data for plotting
    Timestep = df['Timestep']
    lymphocyte_cells = df['Lymphocytes']
    triggering_cells = df['TriggeringCells']
    tumor_cells = df['TumorCells']
    doomed_cells = df['DoomedCells']

    # First graph
    plt.figure(figsize=(8,6))
    plt.plot(Timestep, lymphocyte_cells, label='Lymphocytes', marker='o', color='blue', markersize = 1)
    plt.plot(Timestep, triggering_cells, label='Triggering Cells', marker='*', color='green', markersize=1)
    plt.plot(Timestep, tumor_cells, label='Tumor Cells', marker='s', color='red', markersize = 1)
    plt.plot(Timestep, doomed_cells, label='Doomed Cells', marker='^', color='gold', markersize = 1)

    plt.xlabel('Timestep')
    plt.ylabel('Cell Count')

    plt.legend()
    plt.grid(True)
    save_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunGraph.png'
    plt.savefig(save_path, dpi=300, bbox_inches='tight')

    #plt.show()

    # Second graph
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