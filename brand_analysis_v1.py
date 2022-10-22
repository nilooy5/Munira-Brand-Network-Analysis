# -*- coding: utf-8 -*-
"""Copy of brand_analysis_v1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ESsH_f3fZAkNXOM9zsAjmYCAzNE9MA0t
"""

import os
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from tqdm import tqdm

pd.set_option('display.min_rows', 20)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_excel('combined_edges_str.xlsx', dtype={'source': str, 'target': str})

"""### Logic: "source"/follower is following "target"

### Brand IDs

- 290081566 => @EsteeLauder

- 18148242 => @dermalogica

- 91259072 => @Neutrogena

- 44693072 => @cerave

- 132543891 => @SkinCeuticals

"""

brand_list = ['1_@EsteeLauder', '2_@dermalogica', '3_@Neutrogena', '4_@cerave', '5_@SkinCeuticals']

for colname in ['source', 'target']:
    df.loc[df[colname]=='290081566', colname] = brand_list[0]
    df.loc[df[colname]=='18148242', colname] = brand_list[1]
    df.loc[df[colname]=='91259072', colname] = brand_list[2]
    df.loc[df[colname]=='44693072', colname] = brand_list[3]
    df.loc[df[colname]=='132543891', colname] = brand_list[4]

df

df.source[0]

## Num of followings
pd.DataFrame(df.source.value_counts())

## Num of followers
pd.DataFrame(df.target.value_counts())

"""# Following/follower matrix:"""

def prep_matrix(df, colname='source', col_rename='following'):
    df_res = pd.DataFrame(df[colname].value_counts()).reset_index()
    df_res.columns = ['id', col_rename]
    #df_res = df_res.loc[df_res[col_rename] > 1, :]

    for b in brand_list:
        df_res[b] = 0

    return df_res

"""### 1. df_source: what brands people are following"""

# df_source = prep_matrix(df, colname='source', col_rename='following')

# for i in tqdm(range(len(df_source))):
#     targets = list(df[df['source'] == df_source.id[i]]['target'])
#     for j in brand_list:
#         if j in targets:
#             df_source.loc[i, j] = 1
            
# df_source['n_brand_following'] = np.sum(df_source.iloc[:, [2,3,4,5,6]], axis=1)

## Checking
# len(df_source) - np.sum(df_source.following == df_source['n_brand_following'])

## Output: 5

## Save CSV
# df_source.to_csv('m1_source.csv')

## Load CSV
df_source = pd.read_csv('m1_source.csv', index_col=0)

df_source

pd.DataFrame(df_source.n_brand_following.value_counts())

big_fans = df_source[df_source.n_brand_following == 4].id.tolist()
big_fans

"""### Matrix 1. df_source: what brands people are following

### Analysis:

Among the brand followers we collected, 567 users are following 2 brands, 80 users are following 3 brands, 8 users are following 4 brands.

### Define big_fans:

The 8 users who follow 4 brands are: 

['1568382218002735105',
 '1572625750003441664',
 '1572641040032567301',
 '1409136155384221698',
 '3059011803',
 '1565358112172818434',
 '1556000179081416706',
 '1541449042604990465']
"""

plt.hist(df_source.n_brand_following)





"""### 2. df_target: what brands are following them"""

# df_target = prep_matrix(df, colname='target', col_rename='follower')

# for i2 in tqdm(range(len(df_target))):
#     sources = list(df[df['target'] == df_target.id[i2]]['source'])
#     for j2 in brand_list:
#         if j2 in sources:
#             df_target.loc[i2, j2] = 1
            
# df_target['n_brand_follower'] = np.sum(df_target.iloc[:, [2,3,4,5,6]], axis=1)

## Checking
# len(df_target) - np.sum(df_target.follower == df_target['n_brand_follower'])

## Output: 5

## Save CSV
# df_target.to_csv('m2_target.csv')

## Load CSV
df_target = pd.read_csv('m2_target.csv', index_col=0)

df_target

pd.DataFrame(df_target.n_brand_follower.value_counts())

brand_icons = df_target[df_target.n_brand_follower == 5].id.tolist()
brand_icons

"""### Matrix 2. df_target: what brands are following them

### Analysis

Among the accounts that the brands are following, 222 accounts are followed by 2 brands, 64 accounts are followed by 3 brands, 44 accounts are followed by 4 brands, 9 accounts are followed by 5 brands. 

### Define brand_icons:

The 9 accounts that are followed by 5 brands are: 

['14222518',
 '40965341',
 '19247844',
 '19658436',
 '19546942',
 '15279429',
 '32469566',
 '14934818',
 '482591078']
"""

plt.hist(df_target.n_brand_follower)

"""### Matrix 1"""

for aa in big_fans:
    print(aa, '---', list(df[df['source'] == aa]['target']))

for aa in big_fans:
    print(aa, '---', list(df[df['target'] == aa]['source']))

df_source.head(5)

"""### Matrix 2"""

for bb in brand_icons:
    print(bb, '---', list(df[df['target'] == bb]['source']))

for bb in brand_icons:
    print(bb, '---', list(df[df['source'] == bb]['target']))

df_target.head(5)
