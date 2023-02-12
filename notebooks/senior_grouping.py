import utilcalcs as calc
import pandas as pd


def population_group(df,year):
    All = ['B01001_001E']
    U5 = ['B01001_003E','B01001_027E'] # 0-4 years old
    U10 = ['B01001_004E','B01001_028E'] # 5-9
    U15 = ['B01001_005E','B01001_029E'] # 10-14
    U20 = ['B01001_006E','B01001_007E','B01001_030E','B01001_031E'] # 15-19
    U25 = ['B01001_008E','B01001_009E','B01001_010E','B01001_032E','B01001_033E','B01001_034E'] # 20-24
    U30 = ['B01001_011E','B01001_035E'] # 25-29
    U35 = ['B01001_012E','B01001_036E'] # 30-34
    U40 = ['B01001_013E','B01001_037E'] # 35-39
    U45 = ['B01001_014E','B01001_038E'] # 40-44
    U50 = ['B01001_015E','B01001_039E'] # 45-49
    U55 = ['B01001_016E','B01001_040E'] # 50-54
    U60 = ['B01001_017E','B01001_041E'] # 55-59
    U65 = ['B01001_018E','B01001_019E','B01001_042E','B01001_043E'] # 60-64
    U70 = ['B01001_020E','B01001_021E','B01001_044E','B01001_045E'] # 65-69
    U75 = ['B01001_022E','B01001_046E'] # 70-74
    U80 = ['B01001_023E','B01001_047E'] # 75-79
    U85 = ['B01001_024E','B01001_048E'] # 80-84
    A85 = ['B01001_025E','B01001_049E'] # 85+

    var_list = ['GEO_ID']+All+U5+U10+U15+U20+U25+U30+U35+U40+U45+U50+U55+U60+U65+U70+U75+U80+U85+A85
    df_ = df[var_list].copy()
    
    col_rename = {'B01001_001E':f'All_{year[-2:]}',
                 'B01001_003E':f'U5_{year[-2:]}','B01001_027E':f'U5_{year[-2:]}','B01001_004E':f'U10_{year[-2:]}',
                 'B01001_028E':f'U10_{year[-2:]}','B01001_005E':f'U15_{year[-2:]}','B01001_029E':f'U15_{year[-2:]}',
                 'B01001_006E':f'U20_{year[-2:]}','B01001_007E':f'U20_{year[-2:]}','B01001_030E':f'U20_{year[-2:]}',
                 'B01001_031E':f'U20_{year[-2:]}','B01001_008E':f'U25_{year[-2:]}','B01001_009E':f'U25_{year[-2:]}',
                 'B01001_010E':f'U25_{year[-2:]}','B01001_032E':f'U25_{year[-2:]}','B01001_033E':f'U25_{year[-2:]}',
                 'B01001_034E':f'U25_{year[-2:]}','B01001_011E':f'U30_{year[-2:]}','B01001_035E':f'U30_{year[-2:]}',
                 'B01001_012E':f'U35_{year[-2:]}','B01001_036E':f'U35_{year[-2:]}','B01001_013E':f'U40_{year[-2:]}',
                 'B01001_037E':f'U40_{year[-2:]}','B01001_014E':f'U45_{year[-2:]}','B01001_038E':f'U45_{year[-2:]}',
                 'B01001_015E':f'U50_{year[-2:]}','B01001_039E':f'U50_{year[-2:]}','B01001_016E':f'U55_{year[-2:]}',
                 'B01001_040E':f'U55_{year[-2:]}','B01001_017E':f'U60_{year[-2:]}','B01001_041E':f'U60_{year[-2:]}',
                 'B01001_018E':f'U65_{year[-2:]}','B01001_019E':f'U65_{year[-2:]}','B01001_042E':f'U65_{year[-2:]}',
                 'B01001_043E':f'U65_{year[-2:]}','B01001_020E':f'U70_{year[-2:]}','B01001_021E':f'U70_{year[-2:]}',
                 'B01001_044E':f'U70_{year[-2:]}','B01001_045E':f'U70_{year[-2:]}','B01001_022E':f'U75_{year[-2:]}',
                 'B01001_046E':f'U75_{year[-2:]}','B01001_023E':f'U80_{year[-2:]}','B01001_047E':f'U80_{year[-2:]}',
                 'B01001_024E':f'U85_{year[-2:]}','B01001_048E':f'U85_{year[-2:]}','B01001_025E':f'A85_{year[-2:]}',
                 'B01001_049E':f'A85_{year[-2:]}'}
    
    for col in df_.columns[1:]:
        df_[col] = df_[col].astype(int)
    df_ = df_.replace([999999999, 555555555, 333333333, 222222222,\
                    666666666, 888888888, -999999999, -555555555,\
                    -333333333, -222222222, -666666666, -888888888],0)
    df = df_.copy()
    df = df.rename(columns=col_rename)
    df = df.groupby(df.columns,axis=1).sum()
    df = df[['GEO_ID',f'All_{year[-2:]}',f'U5_{year[-2:]}',f'U10_{year[-2:]}',f'U15_{year[-2:]}',f'U20_{year[-2:]}',f'U25_{year[-2:]}',
             f'U30_{year[-2:]}',f'U35_{year[-2:]}',f'U40_{year[-2:]}',f'U45_{year[-2:]}',f'U50_{year[-2:]}',f'U55_{year[-2:]}',
             f'U60_{year[-2:]}',f'U65_{year[-2:]}',f'U70_{year[-2:]}',f'U75_{year[-2:]}',f'U80_{year[-2:]}',f'U85_{year[-2:]}',
             f'A85_{year[-2:]}']]
    return df


def senior_group(df, year):
  
    All = ['B01001_001E']
    AllM = ['B01001_001M']
    A85 = ['B01001_025E','B01001_049E'] # 85 years and over
    A85M = ['B01001_025M','B01001_049M']
    A65 = ['B01001_020E','B01001_021E','B01001_022E','B01001_023E','B01001_024E','B01001_025E','B01001_044E',
           'B01001_045E','B01001_046E','B01001_047E','B01001_048E','B01001_049E'] # 65 years and over
    A65M = ['B01001_020M','B01001_021M','B01001_022M','B01001_023M','B01001_024M','B01001_025M','B01001_044M',
           'B01001_045M','B01001_046M','B01001_047M','B01001_048M','B01001_049M']
    
    var_list = ['GEO_ID']+All+AllM+A65+A65M
    df_ = df[var_list].copy()
        
    for col in df_.columns[1:]:
        df_[col] = df_[col].astype(float)
    df_ = df_.replace([999999999, 555555555, 333333333, 222222222,\
                    666666666, 888888888, -999999999, -555555555,\
                    -333333333, -222222222, -666666666, -888888888],0)
    df = df_.copy()
    dff = pd.DataFrame()
    dff['GEO_ID'] = df['GEO_ID']
    
    dff[f'All_{year[-2:]}E'] = df[All]
    dff[f'All_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[AllM])),axis=1)
    dff[f'All_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'All_{year[-2:]}E'],x[f'All_{year[-2:]}M'])),axis=1)
    
    dff[f'A65_{year[-2:]}E'] = df[A65[0]]+df[A65[1]]+df[A65[2]]+df[A65[3]]+df[A65[4]]+df[A65[5]]+df[A65[6]]+df[A65[7]]+df[A65[8]]+df[A65[9]]+df[A65[10]]+df[A65[11]]
    dff[f'A65_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[A65M])),axis=1)
    dff[f'A65_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'A65_{year[-2:]}E'],x[f'A65_{year[-2:]}M'])),axis=1)
    
    dff[f'A85_{year[-2:]}E'] = df[A85[0]]+df[A85[1]]
    dff[f'A85_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[A85M])),axis=1)
    dff[f'A85_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'A85_{year[-2:]}E'],x[f'A85_{year[-2:]}M'])),axis=1)
    
    return dff


def householder_group(df, year):
    Otot = ['B25007_002E'] # all owning heads of household
    OtotM = ['B25007_002M']
    O24 = ['B25007_003E'] # 15 to 24 years old
    O24M = ['B25007_003M']
    O34 = ['B25007_004E'] # 25 to 34
    O34M = ['B25007_004M']
    O44 = ['B25007_005E'] # 35 to 44
    O44M = ['B25007_005M']
    O54 = ['B25007_006E'] # 45 to 54
    O54M = ['B25007_006M']
    O64 = ['B25007_007E','B25007_008E'] # 55 to 64 years old
    O64M = ['B25007_007M','B25007_008M']
    O65 = ['B25007_009E','B25007_010E','B25007_011E'] # 65 and older
    O65M = ['B25007_009M','B25007_010M','B25007_011M']
    O85 = ['B25007_011E'] # 85 and older
    O85M = ['B25007_011M']
    
    Rtot = ['B25007_012E'] # all renting heads of household
    RtotM = ['B25007_012M']
    R24 = ['B25007_013E'] # 15 to 24 years old
    R24M = ['B25007_013M']
    R34 = ['B25007_014E'] # 25 to 34
    R34M = ['B25007_014M']
    R44 = ['B25007_015E'] # 35 to 44
    R44M = ['B25007_015M']
    R54 = ['B25007_016E'] # 45 to 54
    R54M = ['B25007_016M']
    R64 = ['B25007_017E','B25007_018E'] # 55 to 64 years old
    R64M = ['B25007_017M','B25007_018M']
    R65 = ['B25007_019E','B25007_020E','B25007_021E'] # 65 and older
    R65M = ['B25007_019M','B25007_020M','B25007_021M']
    R85 = ['B25007_021E'] # 85 and older
    R85M = ['B25007_021M']
    
    var_list = ['GEO_ID']+Otot+OtotM+O24+O24M+O34+O34M+O44+O44M+O54+O54M+O64+O64M+O65+O65M+Rtot+RtotM+R24+R24M+R34+R34M+R44+R44M+R54+R54M+R64+R64M+R65+R65M
    df_ = df[var_list].copy()
    
    for col in df_.columns[1:]:
        df_[col] = df_[col].astype(float)
    df_ = df_.replace([999999999, 555555555, 333333333, 222222222,\
                    666666666, 888888888, -999999999, -555555555,\
                    -333333333, -222222222, -666666666, -888888888],0)
    df = df_.copy()
    dff = pd.DataFrame()
    dff['GEO_ID'] = df['GEO_ID']
    
    dff[f'Otot_{year[-2:]}E'] = df[Otot]
    dff[f'Otot_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[OtotM])),axis=1)
    dff[f'Otot_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'Otot_{year[-2:]}E'],x[f'Otot_{year[-2:]}M'])),axis=1)
    
    dff[f'O24_{year[-2:]}E'] = df[O24]
    dff[f'O24_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[O24M])),axis=1)
    dff[f'O24_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'O24_{year[-2:]}E'],x[f'O24_{year[-2:]}M'])),axis=1)
    
    dff[f'O34_{year[-2:]}E'] = df[O34]
    dff[f'O34_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[O34M])),axis=1)
    dff[f'O34_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'O34_{year[-2:]}E'],x[f'O34_{year[-2:]}M'])),axis=1)
    
    dff[f'O44_{year[-2:]}E'] = df[O44]
    dff[f'O44_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[O44M])),axis=1)
    dff[f'O44_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'O44_{year[-2:]}E'],x[f'O44_{year[-2:]}M'])),axis=1)
       
    dff[f'O54_{year[-2:]}E'] = df[O54]
    dff[f'O54_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[O54M])),axis=1)
    dff[f'O54_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'O54_{year[-2:]}E'],x[f'O54_{year[-2:]}M'])),axis=1)
    
    dff[f'O64_{year[-2:]}E'] = df[O64[0]]+df[O64[1]]
    dff[f'O64_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[O64M])),axis=1)
    dff[f'O64_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'O64_{year[-2:]}E'],x[f'O64_{year[-2:]}M'])),axis=1)
    
    dff[f'O65_{year[-2:]}E'] = df[O65[0]]+df[O65[1]]+df[O65[2]]
    dff[f'O65_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[O65M])),axis=1)
    dff[f'O65_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'O65_{year[-2:]}E'],x[f'O65_{year[-2:]}M'])),axis=1)
    
    dff[f'O85_{year[-2:]}E'] = df[O85]
    dff[f'O85_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[O85M])),axis=1)
    dff[f'O85_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'O85_{year[-2:]}E'],x[f'O85_{year[-2:]}M'])),axis=1)
    
    dff[f'Rtot_{year[-2:]}E'] = df[Rtot]
    dff[f'Rtot_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[RtotM])),axis=1)
    dff[f'Rtot_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'Rtot_{year[-2:]}E'],x[f'Rtot_{year[-2:]}M'])),axis=1)
    
    dff[f'R24_{year[-2:]}E'] = df[R24]
    dff[f'R24_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[R24M])),axis=1)
    dff[f'R24_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'R24_{year[-2:]}E'],x[f'R24_{year[-2:]}M'])),axis=1)
    
    dff[f'R34_{year[-2:]}E'] = df[R34]
    dff[f'R34_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[R34M])),axis=1)
    dff[f'R34_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'R34_{year[-2:]}E'],x[f'R34_{year[-2:]}M'])),axis=1)
    
    dff[f'R44_{year[-2:]}E'] = df[R44]
    dff[f'R44_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[R44M])),axis=1)
    dff[f'R44_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'R44_{year[-2:]}E'],x[f'R44_{year[-2:]}M'])),axis=1)
       
    dff[f'R54_{year[-2:]}E'] = df[R54]
    dff[f'R54_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[R54M])),axis=1)
    dff[f'R54_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'R54_{year[-2:]}E'],x[f'R54_{year[-2:]}M'])),axis=1)
    
    dff[f'R64_{year[-2:]}E'] = df[R64[0]]+df[R64[1]]
    dff[f'R64_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[R64M])),axis=1)
    dff[f'R64_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'R64_{year[-2:]}E'],x[f'R64_{year[-2:]}M'])),axis=1)
    
    dff[f'R65_{year[-2:]}E'] = df[R65[0]]+df[R65[1]]+df[R65[2]]
    dff[f'R65_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[R65M])),axis=1)
    dff[f'R65_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'R65_{year[-2:]}E'],x[f'R65_{year[-2:]}M'])),axis=1)
    
    dff[f'R85_{year[-2:]}E'] = df[R85]
    dff[f'R85_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[R85M])),axis=1)
    dff[f'R85_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'R85_{year[-2:]}E'],x[f'R85_{year[-2:]}M'])),axis=1)
    
    return dff


def poverty_housing_group(df, year):
    All = ['B17017_002E'] # all under poverty line
    AllM = ['B17017_002M']
    Couple = ['B17017_008E'] # married couples under poverty line, householder, age 65+
    CoupleM = ['B17017_008M']
    Single = ['B17017_014E','B17017_019E'] # male + female no spouse present, 65+
    SingleM = ['B17017_014M','B17017_019M']
    Nonfam = ['B17017_025E','B17017_030E'] # male + female non-family household, 65+
    NonfamM = ['B17017_025M','B17017_030M']
    
    var_list = ['GEO_ID']+All+AllM+Couple+CoupleM+Single+SingleM+Nonfam+NonfamM
    df_ = df[var_list].copy()
    
    for col in df_.columns[1:]:
        df_[col] = df_[col].astype(float)
    df_ = df_.replace([999999999, 555555555, 333333333, 222222222,\
                    666666666, 888888888, -999999999, -555555555,\
                    -333333333, -222222222, -666666666, -888888888],0)
    
    df = df_.copy()
    dff = pd.DataFrame()
    dff['GEO_ID'] = df['GEO_ID']
    
    dff[f'All_{year[-2:]}E'] = df[All]
    dff[f'All_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[AllM])),axis=1)
    dff[f'All_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'All_{year[-2:]}E'],x[f'All_{year[-2:]}M'])),axis=1)
    
    dff[f'Couple_{year[-2:]}E'] = df[Couple]
    dff[f'Couple_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[CoupleM])),axis=1)
    dff[f'Couple_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'Couple_{year[-2:]}E'],x[f'Couple_{year[-2:]}M'])),axis=1)
    
    dff[f'Single_{year[-2:]}E'] = df[Single[0]]+df[Single[1]]
    dff[f'Single_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[SingleM])),axis=1)
    dff[f'Single_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'Single_{year[-2:]}E'],x[f'Single_{year[-2:]}M'])),axis=1)
    
    dff[f'Nonfam_{year[-2:]}E'] = df[Nonfam[0]]+df[Nonfam[1]]
    dff[f'Nonfam_{year[-2:]}M'] = df.apply(lambda x: (calc.get_moe(x[NonfamM])),axis=1)
    dff[f'Nonfam_{year[-2:]}C'] = dff.apply(lambda x: (calc.get_cv(x[f'Nonfam_{year[-2:]}E'],x[f'Nonfam_{year[-2:]}M'])),axis=1)
    
    return dff
    
    
def change_columns(df, var, years):
    df[f'{var}_ChangeE'] = df[f'{var}_{years[1][-2:]}E']-df[f'{var}_{years[0][-2:]}E']
    df[f'{var}_Change%'] = (df[f'{var}_{years[1][-2:]}E']-df[f'{var}_{years[0][-2:]}E'])/df[f'{var}_{years[0][-2:]}E']
    df[f'{var}_ChangeM'] = ((df[f'{var}_{years[1][-2:]}M']**2)+(df[f'{var}_{years[0][-2:]}M']**2))**(1/2)
    df[f'{var}_ChangeC'] = df.apply(lambda x: (calc.get_cv(x[f'{var}_ChangeE'],x[f'{var}_ChangeM'])),axis=1)
    return df