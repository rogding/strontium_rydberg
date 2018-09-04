"""
Analysis program for esh_1977 data.

esh_1977: 
    Title: Bound, even-parity J=0 and J=2 spectra of Sr
    Authors: Peter Esherick
    DOI: 10.1103/PhysRevA.15.1920
    URL: https://journals.aps.org/pra/abstract/10.1103/PhysRevA.15.1920

@author: Roger Ding
"""

import os.path
import pandas as pd
import numpy as np

# Names of data files in source/ subdirectory
DATA_FILES = [os.path.join('source','esh_1977-table_3.csv'),
              os.path.join('source','esh_1977-table_4.csv')]

DATA_FILES = [os.path.join('source','esh_1977-table_4.csv')]

COLUMNS = {'Series':       str(),
           'n':            int(),
           'Term':         str(), 
           'Label':        str(),
           'E_exp':        float(),
           'E_exp_unc':    float(),
           'Isotope':      int(),
           'Ref':          str()}

df_output = pd.DataFrame(columns=COLUMNS)

def label(row):
    return row['Series'].replace('n', str(row['n']))

for i in DATA_FILES:
    print('Analyzing ' + i)
    df_temp = pd.read_csv(i)
    
    # Only load data for which this paper provides new measurements and drop 'New' column
    df_temp = df_temp[df_temp['New']]


# I'm not sure why, but joining loses track that 'n' and 'Isotope' are int
#df_output['n'] = df_output['n'].astype(int)
#df_output['Isotope'] = df_output['Isotope'].astype(int)

#df_output.to_csv('esh_1977-analyzed.csv', index=False)