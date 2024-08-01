import pandas as pd
import matplotlib.pyplot as plt

class HALModeling2024Graphs:
    # Specify the full path to the CSV file
    file_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRun.csv'

    # Read the data from the CSV file
    df = pd.read_csv(file_path)

    # Extract data for plotting
    Timestep = df['Timestep']
    lymphocyte_cells = df['Lymphocyte Cells']
    tumor_cells = df['Tumor Cells']
    doomed_cells = df['Doomed Cells']

    plt.figure(figsize=(4,3))
    plt.plot(Timestep, lymphocyte_cells, label='Lymphocytes', marker='o', color='blue', markersize = 1)
    plt.plot(Timestep, tumor_cells, label='Tumor Cells', marker='s', color='red', markersize = 1)
    plt.plot(Timestep, doomed_cells, label='Doomed Cells', marker='^', color='gold', markersize = 1)

    #plt.title('Cell Counts Over Time')
    plt.xlabel('Timestep')
    plt.ylabel('Cell Count')

    plt.legend()
    plt.grid(True)
    save_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\TrialRunGraph.png'
    plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.show()