"""
Analysis program for blt_1982a data.

blt_1982a: https://doi.org/10.1016/0030-4018(82)90082-7

@author: Roger Ding
"""

import os.path
import pandas as pd
import numpy as np

# Names of data files in subdirectory
DATA_FILES = [os.path.join('data','blt_1982a-table_1.csv'),
              os.path.join('data','blt_1982a-table_2.csv')]

output_df = pd.DataFrame()

for i in range(len(DATA_FILES)):
    temp_df = pd.read_csv(DATA_FILES[i])
    
    output_df = pd.concat([output_df, temp_df])

output_df.to_csv('blt_1982a.csv', sep=',')