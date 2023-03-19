import math
import numpy as np
import pandas as pd


bgp_10 = pd.read_csv('../data/geo/bgp_vil_10.csv')
bgp_20 = pd.read_csv('../data/geo/bgp_vil_20.csv')
for df in [bgp_10,bgp_20]: df.geoid = df.geoid.apply(lambda x: '{0:0>12}'.format(x))
    
#get rid of area & geo stuff not being useed
bgp_20 = bgp_20.drop(['aland20','awater20','lat20','lon20','land_acre'],axis=1)
bgp_10 = bgp_10.drop(['aland10','awater10','lat10','lon10','land_acre'],axis=1)


#function that will aggregate estimates, calc new MOEs and CVs
def sumgeo_cv(df,sumgeo):
    variables = list(df.columns[1:])
    var = set()
    for i in variables:
        if i[-1] == 'E' or i[-1] == 'M' or i[-1] == 'C':
            i = i[:-1]
            var.add(i)
        else:
            var.add(i)
    var = list(var)
    results = []
    for i in df[sumgeo].unique():
        dff = df[df[sumgeo] == i]
        record = {}
        record[sumgeo] = i
        for v in var:
            e = dff[f'{v}E'].sum()
            if f'{v}M' not in dff.columns:
                m = np.nan
            else:
                m = math.sqrt(dff[f'{v}M'].apply(lambda x: x**2).sum())
            if m == 0 or e == 0:
                c = 0
            else:
                c = np.absolute(m/1.645/e*100)
            record[f'{v}E'] = e
            record[f'{v}M'] = m
            record[f'{v}C'] = c            
        results.append(record)   
    r = pd.DataFrame(results)
    return r

#function that sums estimates and calculates aggregate MOE
def sumgeo(df,sumgeo):
    variables = list(df.columns[1:])
    var = set()
    for i in variables:
        if i[-1] == 'E' or i[-1] == 'M':
            i = i[:-1]
            var.add(i)
        else:
            var.add(i)
    var = list(var)
    results = []
    for i in df[sumgeo].unique():
        dff = df[df[sumgeo] == i]
        record = {}
        record[sumgeo] = i
        for v in var:
            e = dff[f'{v}E'].sum()
            if f'{v}M' not in dff.columns:
                m = np.nan
            else:
                m = math.sqrt(dff[f'{v}M'].apply(lambda x: x**2).sum())
            record[f'{v}E'] = e
            record[f'{v}M'] = m            
        results.append(record)   
    return pd.DataFrame(results)


def make_uv(df,year):
    if year >= 2020:
        geodf = bgp_20
    else:
        geodf = bgp_10
    df = pd.merge(geodf,df,how='left',left_on='geoid',right_on='GEO_ID')
    df = df.drop(['geoid','GEO_ID'],axis=1)
    df = sumgeo_cv(df,'name')
    return df
