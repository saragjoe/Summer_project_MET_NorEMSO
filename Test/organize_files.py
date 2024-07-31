import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
# Funksjon for å laste inn og filtrere data basert på dybde
def load_and_filter_data(base_directories, depths):
    all_data = {depth: [] for depth in depths}
    
    for base_directory in base_directories:
        for file in os.listdir(base_directory):
            if file.endswith('.csv'):
                file_path = os.path.join(base_directory, file)
                data = pd.read_csv(file_path)
                for depth in depths:
                    filtered_data = data[data['DEPTH'] == depth]
                    all_data[depth].append(filtered_data)
    
    # Slå sammen dataene for hver dybde
    for depth in depths:
        all_data[depth] = pd.concat(all_data[depth], ignore_index=True)
    
    return all_data

# Liste over base directories
base_directories = [
    '/home/sagjo8396/NorEMSO/example_notebooks/StaM_Dep1_files',
    '/home/sagjo8396/NorEMSO/example_notebooks/StaM_Dep2_files',
    '/home/sagjo8396/NorEMSO/example_notebooks/StaM_Dep3_files'
]

# Dybder du er interessert i
depths = [500, 800, 1000, 1200, 2000]

# Laste inn og filtrere data
filtered_data = load_and_filter_data(base_directories, depths)

# Nå har du dataene for hver dybde i `filtered_data` dictionary
# Du kan få tilgang til dataene slik:
data_500m = filtered_data[500]
data_800m = filtered_data[800]
data_1000m = filtered_data[1000]
data_1200m = filtered_data[1200]
data_2000m = filtered_data[2000]
#%%
def apply_qc_filter(data, qc_column, value_column, qc_min=0, qc_max=3):
    return np.where((data[qc_column] > qc_min) & (data[qc_column] < qc_max), data[value_column], np.nan)

data_500m["PSAL_FILTER"] = apply_qc_filter(data_500m, "PSAL_QC", "PSAL")
data_500m["TEMP_FILTER"] = apply_qc_filter(data_500m, "TEMP_QC", "TEMP")
data_800m["PSAL_FILTER"] = apply_qc_filter(data_800m, "PSAL_QC", "PSAL")
data_800m["TEMP_FILTER"] = apply_qc_filter(data_800m, "TEMP_QC", "TEMP")
data_1000m["PSAL_FILTER"] = apply_qc_filter(data_1000m, "PSAL_QC", "PSAL")
data_1000m["TEMP_FILTER"] = apply_qc_filter(data_1000m, "TEMP_QC", "TEMP")
data_1200m["PSAL_FILTER"] = apply_qc_filter(data_1200m, "PSAL_QC", "PSAL")
data_1200m["TEMP_FILTER"] = apply_qc_filter(data_1200m, "TEMP_QC", "TEMP")
data_2000m["PSAL_FILTER"] = apply_qc_filter(data_2000m, "PSAL_QC", "PSAL")
data_2000m["TEMP_FILTER"] = apply_qc_filter(data_2000m, "TEMP_QC", "TEMP")


# %%
# Definer dybdene og tilhørende data
depths = [500, 800, 1000, 1200,2000]
datasets = [data_500m, data_800m, data_1000m, data_1200m, data_2000m,]

# Opprett et subplot-rutenett med 5 rader og 2 kolonner
fig, axs = plt.subplots(nrows=5, ncols=2, figsize=(12, 18))

# Gå gjennom hver dybde og tilsvarende datasett
for i, (depth, dataset) in enumerate(zip(depths, datasets)):
    row = i  # Riktig rad for dette datasettet
    col_temp = 0  # Kolonne for temperaturplot
    col_salt = 1  # Kolonne for salinitetsplot

    # Temperaturplot (venstre kolonne)
    axs[row, col_temp].plot(dataset["TIME"], dataset["TEMP_FILTER"], label=f"{depth}m - QC Obs")
    axs[row, col_temp].plot(dataset["TIME"], dataset["TEMP_MOD"], label=f"{depth}m - Modell")
    axs[row, col_temp].set_ylim((dataset["TEMP_FILTER"].min(),dataset["TEMP_FILTER"].max))  # Juster y-aksen om nødvendig
    axs[row, col_temp].set_title(f"Temperatur for {depth}m")
    axs[row, col_temp].legend()

    # Salinitetsplot (høyre kolonne)
    axs[row, col_salt].plot(dataset["TIME"], dataset["PSAL_FILTER"], label=f"{depth}m - QC Obs")
    axs[row, col_salt].plot(dataset["TIME"], dataset["SALT_MOD"], label=f"{depth}m - Modell")
    axs[row, col_salt].set_ylim((dataset["PSAL_FILTER"].min(), dataset["PSAL_FILTER"].max()))  # Juster y-aksen om nødvendig
    axs[row, col_salt].set_title(f"Salinitet for {depth}m")
    axs[row, col_salt].legend()

# Legg til padding mellom subplots for bedre lesbarhet
plt.tight_layout()