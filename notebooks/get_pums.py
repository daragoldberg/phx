import pandas as pd
import requests
import os
import json

census_key = os.getenv('Census_API')

# pull data from PUMS API specifying the sample (1/5 yr), 
# year, and desired data columns
def pull_data(sample,year,cols):
    base_url = f'https://api.census.gov/data/{year}/acs/{sample}/pums'
    url = f'{base_url}?get={cols}&for=state:04&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    df = df.drop(['state'],axis=1)
    return df


# make three sets of data columns to merge replicate weight columns             
def make_var_list(data_cols,var_type):    
    wt_1 = wt_2 = wt_3 = data_cols
    
    for wt in range(1,30):
        wt_1+=f',{var_type}WGTP{wt}'
        
    for wt in range(30,60):
        wt_2+=f',{var_type}WGTP{wt}'
     
    for wt in range(60,81):
        wt_3+=f',{var_type}WGTP{wt}'
    
    return wt_1,wt_2,wt_3


def get_puma(sample,year,data_cols,var_type=''):
    '''if person weight, var_type='P',else blank'''
    
    cols1,cols2,cols3 = make_var_list(data_cols,var_type)
    df_1 = pull_data(sample,year,cols1)
    df_2 = pull_data(sample,year,cols2)
    df_3 = pull_data(sample,year,cols3)
    
    join_cols = list(df_1.columns[:df_1.columns.get_loc(f'{var_type}WGTP1')])
    
    df_fin = pd.merge(df_1,pd.merge(df_2,df_3,on=join_cols,how='left'),on=join_cols,how='left')
    
    return df_fin
    

