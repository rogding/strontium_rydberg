"""
Analysis program for awe_1979 data.

awe_1979: 
    Title: Bound, odd-parity J = 1 spectra of the alkaline earths: Ca, Sr, and Ba
    Authors: J. A. Armstrong, J. J. Wynne, and P. Esherick
    DOI: 10.1364/JOSA.69.000211
    URL: https://www.osapublishing.org/josa/abstract.cfm?uri=josa-69-2-211

@author: Roger Ding
"""

import os.path
import pandas as pd

# Names of data files in source/ subdirectory
DATA_FILES = [os.path.join('source','awe_1979-table_2.csv')]

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
    df_temp['Ref'] = 'awe_1979'
    
    # Assuming all measured energies are for 88Sr
    df_temp['Isotope'] = 88

    # Just copying contents of 'Obs' (observed energy) to 'E_exp' to match output column labels
    df_temp['E_exp'] = df_temp['Obs']
    df_temp['E_exp_unc'] = df_temp['Obs_unc']
    
    df_output = pd.concat([df_output, df_temp], join='inner', ignore_index=True)


# I'm not sure why, but joining loses track that 'n' and 'Isotope' are int
df_output['n'] = df_output['n'].astype(int)
df_output['Isotope'] = df_output['Isotope'].astype(int)

df_output.to_csv('awe_1979-analyzed.csv', index=False)