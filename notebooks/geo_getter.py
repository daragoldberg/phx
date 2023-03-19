import pandas as pd
import numpy as np


base_url = 'https://tigerweb.geo.census.gov/tigerwebmain/Files/'
acre = 0.000247105


#get area data for cities and consolidated city (indianapolis)
def make_city(year):
    indy = pd.read_html(f'{base_url}tab20/tigerweb_tab20_concity_{year}_in.html')
    indy = indy[0]

    states = ['az','tx','fl']
    pl = pd.DataFrame()
    for state in states:
        df = pd.read_html(f'{base_url}tab20/tigerweb_tab20_incplace_{year}_{state}.html')
        dff = df[0]
        pl = pd.concat([pl,dff])
        
    places = pd.concat([indy,pl])
    places = places[['GEOID','BASENAME','AREALAND','AREAWATER']].copy()
    places['AREALAND_ACRE'] = places.AREALAND * acre
    
    for col in places.columns[1:]:
        places.rename(columns={col:f'{col}{year[-2:]}'},inplace=True)
        
    return places

#get maricopa county
def make_maricopa(year):
    df = pd.read_html(f'{base_url}tab20/tigerweb_tab20_county_{year}_az.html')
    df = df[0]   
    df = df[['GEOID','BASENAME','AREALAND','AREAWATER']].copy()
    df = df[df.GEOID==4013]
    df['AREALAND_ACRE'] = df.AREALAND * acre
    for col in df.columns[1:]:
        df.rename(columns={col:f'{col}{year[-2:]}'},inplace=True)
    return df

def make_az(year):
    df = pd.read_html(f'{base_url}tab20/tigerweb_tab20_state_{year}_us.html')
    df = df[0]   
    df = df[['GEOID','BASENAME','AREALAND','AREAWATER']].copy()
    df = df[df.GEOID==4]
    df['AREALAND_ACRE'] = df.AREALAND * acre
    for col in df.columns[1:]:
        df.rename(columns={col:f'{col}{year[-2:]}'},inplace=True)
    return df

#get us
def make_us(year):
    df = pd.read_html(f'{base_url}tab20/tigerweb_tab20_region_{year}_us.html')
    df = df[0]   
    df = df[['FUNCSTAT','AREALAND','AREAWATER']].copy().groupby(['FUNCSTAT']).sum().reset_index()
    df['AREALAND_ACRE'] = df.AREALAND * acre
    for col in df.columns[1:]:
        df.rename(columns={col:f'{col}{year[-2:]}'},inplace=True)
    return df