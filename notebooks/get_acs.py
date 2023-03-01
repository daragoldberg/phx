import pandas as pd
import requests
import os
import json

census_key = os.getenv('Census_API')

#### ACS DATA GETTERS - IMPORT INTO ANALYSIS NOTEBOOKS

def get_us(source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    url = f'{base_url}?get={col}&for=us:*&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    return df

def get_az(source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    url = f'{base_url}?get={col}&for=state:04&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    return df

def get_az_co(source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    url = f'{base_url}?get={col}&for=county:*&in=state:04&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    df['GEO_ID'] = df['GEO_ID'].str[-5:]
    return df

def get_phx(source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    url = f'{base_url}?get={col}&for=place:*&in=state:04&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    df['GEO_ID'] = df.state + df.place
    df = df[df.GEO_ID=='0455000'].drop(['NAME','state','place'],axis=1)
    return df

def get_tract(source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    url = f'{base_url}?get={col}&for=tract:*&in=state:04&in=county:013&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    return df

def get_bgp(source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    url = f'{base_url}?get={col}&for=block%20group:*&in=state:04%20county:013&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    df = df.drop(['NAME','state','county','tract','block group'],axis=1)
    df['GEO_ID'] = df['GEO_ID'].str[-12:]
    return df


def get_puma(source,year,col):
    base_url = f'https://api.census.gov/data/{year}/{source}'
    url = f'{base_url}?get={col}&for=public%20use%20microdata%20area:*&in=state:04&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    df = df.drop(['NAME','state','public use microdata area'],axis=1)
    df['GEO_ID'] = df['GEO_ID'].str[-7:]
    return df


def clean_data(df,var_list):
    dff = df[var_list].copy()
    #assumes first item in variable list is GEO_ID and no other id cols
    for col in dff.columns[1:]:
        dff[col] = dff[col].astype(float)
    dff = dff.replace([999999999, 555555555, 333333333, 222222222,\
                    666666666, 888888888, -999999999, -555555555,\
                    -333333333, -222222222, -666666666, -888888888],0)
    return dff

def clean_table(df):   
    df = df.filter(regex='(?<!A)$',axis=1) #drop non-estimate columns
    df = df[['GEO_ID']+[col for col in df.columns if col != 'GEO_ID']] #move id to first col
    df = clean_data(df,df.columns)
    return df