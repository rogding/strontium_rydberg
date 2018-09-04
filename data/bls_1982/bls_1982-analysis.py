"""
Analysis program for bls_1982 data.

bls_1982: 
    Title: One-Photon Laser Spectroscopy of Rydberg Series from Metastable Levels in Calcium and Strontium
    Authors: R. Beigang, K. Lücke, D. Schmidt, A. Timmermann and P. J. West
    DOI: 10.1088/0031-8949/26/3/007
    URL: http://iopscience.iop.org/article/10.1088/0031-8949/26/3/007

@author: Roger Ding
"""

import os.path
import pandas as pd
import numpy as np

# Names of data files in source/ subdirectory
DATA_FILES = [os.path.join('source','bls_1982-table_4.csv'),
              os.path.join('source','bls_1982-table_5.csv')]

COLUMN_NAMES = ['Series', 'n', 'Term', 'E_exp', 'E_exp_unc', 'Isotope', 'Ref']

df_output = pd.DataFrame(columns=COLUMN_NAMES)

for i in DATA_FILES:
    print('Analyzing ' + i)
    df_temp = pd.read_csv(i)

    # Only load data for which this paper provides new measurements and drop 'New' column
    df_temp = df_temp[df_temp['New']]

    # Add string with biblatex reference key
    df_temp['Ref'] = 'bls_1982'

    # Assuming all measured energies are for 88Sr
    df_temp['Isotope'] = 88

    # Adding experimental uncertainty of +/-0.15 /cm
    df_temp['E_exp_unc'] = 0.15
    
    # Join dataframes with shared column names (i.e., COLUMN_NAMES)
    df_output = pd.concat([df_output, df_temp], join='inner')

df_output.to_csv('bls_1982-analyzed.csv')