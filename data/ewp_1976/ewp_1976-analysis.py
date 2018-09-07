"""
Analysis program for ewp_1976 data.

ewp_1976: 
    Title: Laser ionization spectroscopy of Rydberg and autoionization levels in Sr I
    Authors: P. Ewart and A. F. Purdie
    DOI: 10.1088/0022-3700/9/15/002
    URL: http://iopscience.iop.org/article/10.1088/0022-3700/9/15/002/meta

@author: Roger Ding
"""

import os.path
import pandas as pd

# Names of data files in source/ subdirectory
REF = 'ewp_1976'
DATA_FILES = [os.path.join('source', REF+'-table_1.csv')]

COLUMNS = {'Series':       str(),
           'n':            int(),
           'Term':         str(), 
           'Label':        str(),
           'E_exp':        float(),
           'E_exp_unc':    float(),
           'Isotope':      int(),
           'Ref':          str()}

df_output = pd.DataFrame(columns=COLUMNS)

for i in DATA_FILES:
    print('Analyzing ' + i)
    df_temp = pd.read_csv(i)
    
    df_temp['Label'] = df_temp['Assignment']
    
    # Drop NaN values in 'New' column
    df_temp.dropna(subset=['New'], inplace=True)
    
    # Only load data for which this paper provides new measurements and drop 'New' column
    df_temp = df_temp[df_temp['New']]

    # Add string with biblatex reference key
    df_temp['Ref'] = REF
    
    # Assuming all measured energies are for 88Sr
    df_temp['Isotope'] = 88

    # Just copying contents of 'E_obs' (observed energy) to 'E_exp' to match output column labels
    df_temp['E_exp'] = df_temp['Energy_level']
    df_temp['E_exp_unc'] = 0.3
    
    df_output = pd.concat([df_output, df_temp], join='inner', ignore_index=True)


# I'm not sure why, but joining loses track that 'n' and 'Isotope' are int
df_output['n'] = df_output['n'].astype(int)
df_output['Isotope'] = df_output['Isotope'].astype(int)

df_output.to_csv(REF+'-analyzed.csv', index=False)