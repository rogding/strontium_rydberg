"""
Analysis program for blt_1982 data.

blt_1982: 
    Title: Determination of absolute level energies of 5sns1S0 and 5snd1D2 Rydberg series of Sr
    Authors: R. Beigang, K. Lücke, A. Timmermann, P. J. West, D. Frölich
    DOI: 10.1016/0030-4018(82)90082-7
    URL: https://www.sciencedirect.com/science/article/pii/0030401882900827?via%3Dihub

@author: Roger Ding
"""

import os.path
import pandas as pd
import scipy.constants as spc

# Names of data files in source/ subdirectory
REF = 'blt_1982'
DATA_FILES = [os.path.join('source', REF+'-table_1.csv'),
              os.path.join('source', REF+'-table_2.csv')]

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
    
    # Drop NaN values in 'New' column
    df_temp.dropna(subset=['New'], inplace=True)
    
    # Only load data for which this paper provides new measurements and drop 'New' column
    df_temp = df_temp[df_temp['New']]

    # Add string with biblatex reference key
    df_temp['Ref'] = REF
    
    # Assuming all measured energies are for 88Sr
    df_temp['Isotope'] = 88

    # Just copying contents of 'E_obs' (observed energy) to 'E_exp' to match output column labels
    df_temp['E_exp'] = df_temp['E_obs']
    df_temp['E_exp_unc'] = 30*((10**4)/spc.c)
    
    df_output = pd.concat([df_output, df_temp], join='inner', ignore_index=True)


# I'm not sure why, but joining loses track that 'n' and 'Isotope' are int
df_output['n'] = df_output['n'].astype(int)
df_output['Isotope'] = df_output['Isotope'].astype(int)

df_output.to_csv(REF+'-analyzed.csv', index=False)