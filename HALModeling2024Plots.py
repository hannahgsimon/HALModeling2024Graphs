import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = r'C:\Users\Hannah\Documents\HALModeling2024Outs\AvgTimestepstoEscape.csv'
data = pd.read_csv(file_path)

# Filter the data for Bifurcation to Escape equals 'Y'
filtered_data = data[data['Bifurcation to Escape'] == 'Y']

# Create a boxplot for "Timesteps to Equilibrium"
plt.figure(figsize=(10, 6))
filtered_data.boxplot(column='Timesteps to Equilibrium', by='Scenario', grid=False, widths=0.7)
plt.suptitle('')  # Suppress the default title
plt.title('')     # Remove the secondary title
plt.xlabel('Scenario', fontsize = 24)
plt.ylabel('Timestep', fontsize = 24)
plt.tick_params(axis='both', labelsize=16)

timesteps_save_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\BoxplotTimesteps.png'
plt.savefig(timesteps_save_path, dpi=600, bbox_inches='tight')
#plt.show()
plt.close()

# Create a boxplot for "Tumor Cells at Equilibrium"
filtered_data = data[data['Bifurcation to Escape'] == 'Y'].copy()
filtered_data.rename(columns={'Tumor Cells at Equilibrium': 'Tumor Cells'}, inplace=True)
print(filtered_data.columns)
plt.figure(figsize=(10, 6))
filtered_data.boxplot(column='Tumor Cells', by='Scenario', grid=False, widths=0.7)
plt.suptitle('')
plt.title('')
plt.xlabel('Scenario', fontsize=24)
plt.ylabel('Tumor Cells', fontsize=24)
plt.tick_params(axis='both', labelsize=16)

tumorcells_save_path = fr'C:\Users\Hannah\Documents\HALModeling2024Outs\BoxplotTumorCells.png'
plt.savefig(tumorcells_save_path, dpi=600, bbox_inches='tight')
#plt.show()
plt.close()