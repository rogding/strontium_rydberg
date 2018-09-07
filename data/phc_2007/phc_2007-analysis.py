"""
Analysis program for phc_2007 data.

phc_2007: 
    Title: The controlled excitation of forbidden transitions in the two-photon spectrum of strontium by using collisions and electric fields
    Authors: G.Philip, J.-P.Connerade
    DOI: 10.1016/j.optcom.2007.07.001
    URL: https://www.sciencedirect.com/science/article/pii/S0030401807006931?via%3Dihub

@author: Roger Ding
"""

import os.path
import pandas as pd

# Names of data files in source/ subdirectory
REF = 'phc_2007'
DATA_FILES = [os.path.join('source', REF+'-table_1.csv'),
              os.path.join('source', REF+'-table_2.csv'),
              os.path.join('source', REF+'-table_3.csv'),
              os.path.join('source', REF+'-text.csv')]

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
    
    # Copy state label
    df_temp['Label'] = df_temp['Level_designation']

    # Add string with biblatex reference key
    df_temp['Ref'] = REF
    
    # Assuming all measured energies are for 88Sr
    df_temp['Isotope'] = 88

    # Just copying contents of 'E_obs' (observed energy) to 'E_exp' to match output column labels
    df_temp['E_exp'] = df_temp['E_Present_Expt']
    df_temp['E_exp_unc'] = 0.18
    
    # Drop rows states without an assigned energy
    df_temp.dropna(subset=['E_exp'], inplace=True)
    
    df_output = pd.concat([df_output, df_temp], join='inner', ignore_index=True)


# I'm not sure why, but joining loses track that 'n' and 'Isotope' are int
df_output['n'] = df_output['n'].astype(int)
df_output['Isotope'] = df_output['Isotope'].astype(int)

df_output.to_csv(REF+'-analyzed.csv', index=False)