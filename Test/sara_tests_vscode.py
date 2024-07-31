#import matplotlib.pyplot as plt
import pandas as pd
import datetime
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import gsw
import xroms
import pyresample
import glob 

#%%
#txtfile_d2_500m  = '/home/sagjo8396/NorEMSO/example_notebooks/StaM_Dep2_files/StaM_SBE_20211127_500m_2021-11.csv'
txtfile_d1_2020_08 = '/home/sagjo8396/NorEMSO/example_notebooks/StaM_Dep1_files/StationM_2021_hydrography_2020-08.csv'
txtfile_d1_2020_09 = '/home/sagjo8396/NorEMSO/example_notebooks/StaM_Dep1_files/StationM_2021_hydrography_2020-09.csv'
#%%
d1_08 = pd.read_csv(txtfile_d1_2020_08)
d1_09 = pd.read_csv(txtfile_d1_2020_09)

#%%
d1_08_500m  = d1_08[d1_08['DEPTH']==500]
d1_08_800m  = d1_08[d1_08['DEPTH']==800]
d1_08_1000m = d1_08[d1_08['DEPTH']==1000]
d1_08_1200m = d1_08[d1_08['DEPTH']==1200]
d1_08_2000m = d1_08[d1_08['DEPTH']==2000]

d1_09_500m  = d1_09[d1_09['DEPTH']==500]
d1_09_800m  = d1_09[d1_09['DEPTH']==800]
d1_09_1000m = d1_09[d1_09['DEPTH']==1000]
d1_09_1200m = d1_09[d1_09['DEPTH']==1200]
d1_09_2000m = d1_09[d1_09['DEPTH']==2000]

# %%
ramme = [d1_08_500m, d1_09_500m]

samla = pd.concat(ramme, ignore_index =True)

# %%
