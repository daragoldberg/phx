import pandas as pd
import requests
import os
import json

census_key = os.getenv('Census_API')
from geo import *
nyc = pd.read_csv('../../data/geo/nyc_subbor_10.csv')

#### DEC DATA GETTERS - NEED TO BE ADAPTED FOR DECENNIAL CENSUS DATA

def get_county(proxy,source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    url = f'{base_url}?get={col}&for=county:*&in=state:*&key={census_key}'
    resp = requests.request('GET',url,proxies=proxy).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    df['GEO_ID'] = df.GEO_ID.str[-5:]
    df = df[df.GEO_ID.isin(stco_fips)].drop(['state','county'],axis=1)
    return df

def get_mcd(proxy,source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    frames = []
    for st,co in stco.items():
        for i in co:
            url = f'{base_url}?get={col}&for=county%20subdivision:*&in=state:{st}%20county:{i}&key={census_key}'
            resp = requests.request('GET',url,proxies=proxy).content
            df = pd.DataFrame(json.loads(resp)[1:])
            df.columns = json.loads(resp)[0]
            df['GEO_ID'] = df.GEO_ID.str[-10:]
            frames.append(df)
    dff = pd.concat(frames)
    dff = dff.drop(['state','county','county subdivision'],axis=1)
    return dff

def get_place(proxy,source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    url = f'{base_url}?get={col}&for=place:*&in=state:36&key={census_key}'
    resp = requests.request('GET',url,proxies=proxy).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    df['GEO_ID'] = df.GEO_ID.str[-7:]
    df = df.drop(['state','place'],axis=1)
    return df

def get_nyc_tract(proxy,source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    nyc = ['005','047','061','081','085']
    frames = []
    for i in nyc:
        url = f'{base_url}?get={col}&for=tract:*&in=state:36&in=county:{i}&key={census_key}'
        resp = requests.request('GET',url,proxies=proxy).content
        df = pd.DataFrame(json.loads(resp)[1:])
        df.columns = json.loads(resp)[0]
        df = df.drop(['state','county','tract'],axis=1)
        frames.append(df)
    return pd.concat(frames)

def get_tract(proxy,source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    states = ['09','34','36']
    frames = []
    for st in states:
        url = f'{base_url}?get={col}&for=tract:*&in=state:{st}&in=county:*&key={census_key}'
        resp = requests.request('GET',url,proxies=proxy).content
        df = pd.DataFrame(json.loads(resp)[1:])
        df.columns = json.loads(resp)[0]
        df['stco']=df.state+df.county
        df['GEO_ID'] = df.GEO_ID.str[-11:]
        df = df[df.stco.isin(stco_fips)].drop(['state','county','tract','stco'],axis=1)
        frames.append(df)
    return pd.concat(frames)

def get_cbg(proxy,source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    frames = []
    for st,co in stco.items():
        for c in co:
            url = f'{base_url}?get={col}&for=block%20group:*&in=state:{st}%20county:{c}&key={census_key}'
            resp = requests.request('GET',url,proxies=proxy).content
            df = pd.DataFrame(json.loads(resp)[1:])
            df.columns = json.loads(resp)[0]
            df['GEO_ID'] = df.GEO_ID.str[-12:]
            df = df.drop(['state','county','tract','block group'],axis=1)
            frames.append(df)
    return pd.concat(frames)

#def get_nyc_nta(proxy,source,year,col):
#    pass


#def get_nyc_subbor(proxy,source,year,col):
#    pass




def clean_data(df,var_list):
    dff = df[var_list].copy()
    #assumes first item in variable list is GEO_ID and no other data cols
    for col in dff.columns[1:]:
        dff[col] = dff[col].astype(float)
    dff = dff.replace([999999999, 555555555, 333333333, 222222222,\
                    666666666, 888888888, -999999999, -555555555,\
                    -333333333, -222222222, -666666666, -888888888],0)
    return dff