import pandas as pd
import requests
import os
import json

census_key = os.getenv('Census_API')
comp_cities = {'04':['73000','65000','27820'],'48':['65000','19000'],'12':['35000']}

#AZ:tempe,scottsdale,glendale TX: san antonio, dallas
#FL: jacksonville
#Indianapolis consolidated: '18','36000'

#removed: louisville, ky '21':['48000'] - no data in 2010


#### DATA GETTERS - IMPORT INTO ANALYSIS NOTEBOOKS

base_url = f'https://api.census.gov/data/'

def get_us(source,year,col):
    url = f'{base_url}{year}/{source}?get={col}&for=us:*&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    return df

def get_az(source,year,col):
    url = f'{base_url}{year}/{source}?get={col}&for=state:04&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    #if source[:3]=='dec':
    #    df = df.rename({'name':'GEO_ID'},axis=1)
    #else:
    #    df = df.drop(['NAME','state'],axis=1)
    #    df['GEO_ID'] = df['GEO_ID'].str[-2:]
    return df

def get_az_co(source,year,col):
    url = f'{base_url}{year}/{source}?get={col}&for=county:*&in=state:04&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    if source[:3]=='dec':
        df['GEO_ID'] = df.state+df.county
        df = df.drop(['state','county'],axis=1) 
    else:
        df = df.drop(['NAME','state','county'],axis=1)
        df['GEO_ID'] = df['GEO_ID'].str[-5:]
    return df

def get_maricopa(source,year,col):
    url = f'{base_url}{year}/{source}?get={col}&for=county:013&in=state:04&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    if source[:3]=='dec':
        df['GEO_ID'] = df.state+df.county
        df = df.drop(['state','county'],axis=1)
    else:
        df = df.drop(['NAME','state','county'],axis=1)
        df['GEO_ID'] = df['GEO_ID'].str[-5:]
    return df

def get_phx(source,year,col):
    url = f'{base_url}{year}/{source}?get={col}&for=place:*&in=state:04&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    df['GEO_ID'] = df.state + df.place
    df = df[df.GEO_ID=='0455000']
    if source[:3]=='dec':
        df = df.drop(['state','place'],axis=1)
    else:
        df = df.drop(['NAME','state','place'],axis=1)
    return df

def get_comp_cities(source,year,col):
    frames = []
    for st,city in comp_cities.items():
        for i in city:
            url = f'{base_url}{year}/{source}?get={col}&for=place:{i}&in=state:{st}&key={census_key}'
            resp = requests.request('GET',url).content
            df = pd.DataFrame(json.loads(resp)[1:])
            df.columns = json.loads(resp)[0]
            df['GEO_ID'] = df.state + df.place
            frames.append(df)
    dff = pd.concat(frames)
    
    #special for Indianapolis, consolidated city, not in 5-year acs
    if source=='acs/acs1':
        pass
    else:
        url_ind = f'{base_url}{year}/{source}?get={col}&for=consolidated%20city:36000&in=state:18&key={census_key}'
        resp_ind = requests.request('GET',url_ind).content
        df_ind = pd.DataFrame(json.loads(resp_ind)[1:])
        df_ind.columns = json.loads(resp_ind)[0]
        df_ind['GEO_ID'] = df_ind.state+df_ind['consolidated city']
        df_ind.rename(columns={'consolidated city':'place'},inplace=True)
        dff = pd.concat([dff,df_ind])
    
    if source[:3]=='dec':
        dff = dff.drop(['state','place'],axis=1)
    else:
        dff = dff.drop(['NAME','state','place'],axis=1)      
    return dff

def get_tract(source,year,col):
    url = f'{base_url}{year}/{source}?get={col}&for=tract:*&in=state:04&in=county:013&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    return df

def get_bgp(source,year,col):
    url = f'{base_url}{year}/{source}?get={col}&for=block%20group:*&in=state:04%20county:013&key={census_key}'
    resp = requests.request('GET',url).content
    df = pd.DataFrame(json.loads(resp)[1:])
    df.columns = json.loads(resp)[0]
    if source[:3]=='dec':
        df['GEO_ID'] = df.state + df.county + df.tract + df['block group']
        df = df.drop(['state','county','tract','block group'],axis=1)
    else:
        df = df.drop(['NAME','state','county','tract','block group'],axis=1)
        df['GEO_ID'] = df['GEO_ID'].str[-12:]
    return df


def get_puma(source,year,col):
    url = f'{base_url}{year}/{source}?get={col}&for=public%20use%20microdata%20area:*&in=state:04&key={census_key}'
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