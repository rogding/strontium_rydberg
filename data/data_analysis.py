# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:23:00 2018

@author: Roger Ding
"""

import os.path
import pandas as pd
from subprocess import call
from uncertainties import unumpy

REF = ['awe_1979',
        'bls_1982',
        'blt_1982',
        'dai_1995',
        'daz_1995',
        'esh_1977',
        'ewp_1976',
        'khk_1993',
        'phc_2007']

# Need to find a better way of optionally running *-analysis.py programs from
# this program.
#for ref in REF:
#    analysis_code = os.path.join(ref, ref+'-analysis.py')
#    call(analysis_code, shell=True)

DATA_FILES = []
for i in REF:
    DATA_FILES.append(os.path.join(i, i+'-analyzed.csv'))

COLUMNS = {'Series':       str(),
           'n':            int(),
           'Term':         str(), 
           'Label':        str(),
           'E_exp':        float(),
           'E_exp_unc':    float(),
           'Isotope':      int(),
           'Ref':          str()}

df_read_data = pd.DataFrame(columns=COLUMNS)

for i in DATA_FILES:
    print('Reading ' + i)
    df_temp = pd.read_csv(i)
    
    df_read_data = pd.concat([df_read_data, df_temp], join='inner', ignore_index=True)

# I'm not sure why, but joining loses track that 'n' and 'Isotope' are int
df_read_data['n'] = df_read_data['n'].astype(int)
df_read_data['Isotope'] = df_read_data['Isotope'].astype(int)

SERIES_TERM = [['5sns', '1S0'],
               ['5sns', '3S1']]

for s,t in SERIES_TERM:
    print(s + t)
    
    df_temp = df_read_data[(df_read_data['Series']==s) & (df_read_data['Term']==t)].copy()
    df_temp.sort_values(by=['n'], ascending=True, inplace=True)
    
    for n in df_temp['n'].unique():
        print(n)
        E_exp = df_temp[df_temp['n']==n]['E_exp']
        E_exp_unc = df_temp[df_temp['n']==n]['E_exp_unc']
        temp = unumpy.uarray(E_exp,E_exp_unc)
        print(temp.mean())
        #print(df_temp[df_temp['n']==n])
    