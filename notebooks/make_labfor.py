import utilcalcs as calc

col_s = 'group(B23001)'
col_d = 'GEO_ID,DP03_0002E,DP03_0002M,group(DP04)'

#Grouping variables/columns into lists to run calculations for a new table
#Population and LFor Force Participants by Different Age Cohorts
#Can be used for all ACS years

#Age 16 to 24 
Pop1624E = ['B23001_003E','B23001_010E','B23001_017E','B23001_089E','B23001_096E','B23001_103E']
Pop1624M = ['B23001_003M','B23001_010M','B23001_017M','B23001_089M','B23001_096M','B23001_103M']
LF1624E = ['B23001_004E','B23001_011E','B23001_018E','B23001_090E','B23001_097E','B23001_104E']
LF1624M = ['B23001_004M','B23001_011M','B23001_018M','B23001_090M','B23001_097M','B23001_104M']

#Age 25 to 34
Pop2534E = ['B23001_024E','B23001_031E','B23001_110E','B23001_117E']
Pop2534M = ['B23001_024M','B23001_031M','B23001_110M','B23001_117M']
LF2534E = ['B23001_025E','B23001_032E','B23001_111E','B23001_118E']
LF2534M = ['B23001_025M','B23001_032M','B23001_111M','B23001_118M']

#Age 35 to 44
Pop3544E = ['B23001_038E','B23001_124E']
Pop3544M = ['B23001_038M','B23001_124M']
LF3544E = ['B23001_039E','B23001_125E']
LF3544M = ['B23001_039M','B23001_125M']

#Age 45 to 54
Pop4554E = ['B23001_045E','B23001_131E']
Pop4554M = ['B23001_045M','B23001_131M']
LF4554E = ['B23001_046E','B23001_132E']
LF4554M = ['B23001_046M','B23001_132M']

#Age 25 to 54 (prime-age workforce)
Pop2554E = Pop2534E + Pop3544E + Pop4554E
Pop2554M = Pop2534M + Pop3544M + Pop4554M
LF2554E = LF2534E + LF3544E + LF4554E
LF2554M = LF2534M + LF3544M + LF4554M

#Age 55 to 64
Pop5564E = ['B23001_052E','B23001_059E','B23001_066E','B23001_138E','B23001_145E','B23001_152E']
Pop5564M = ['B23001_052M','B23001_059M','B23001_066M','B23001_138M','B23001_145M','B23001_152M']
LF5564E = ['B23001_053E','B23001_060E','B23001_067E','B23001_139E','B23001_146E','B23001_153E']
LF5564M = ['B23001_053M','B23001_060M','B23001_067M','B23001_139M','B23001_146M','B23001_153M']

#Over Age 65
PopO65E = ['B23001_073E','B23001_078E','B23001_083E','B23001_159E','B23001_164E','B23001_169E']
PopO65M = ['B23001_073M','B23001_078M','B23001_083M','B23001_159M','B23001_164M','B23001_169M']
LFO65E = ['B23001_074E','B23001_079E','B23001_084E','B23001_160E','B23001_165E','B23001_170E']
LFO65M = ['B23001_074M','B23001_079M','B23001_084M','B23001_160M','B23001_165M','B23001_170M']

#Age 55 and over
PopO55E = Pop5564E + PopO65E
PopO55M = Pop5564M + PopO65M
LFO55E = LF5564E + LFO65E
LFO55M = LF5564M + LFO65M

#Total LFor Force
LFE = LF1624E + LF2554E + LFO55E
LFM = LF1624M + LF2554M + LFO55M

#Total Pop
PopE = Pop1624E + Pop2554E + PopO55E
PopM = Pop1624M + Pop2554M + PopO55M

#List of all variables used for calculation + total population variables for spot checking aggregation
var_data = ['GEO_ID','B23001_001E','B23001_001M','DP03_0002E','DP03_0002M'] \
            + PopE + LFE + PopM + LFM

#Function calculate labor force summary variables in Year 0 & Year 1
def make_lf_vars(df,year):
    #Total Labor Force, MOE & CV
    df['Pop_YRE'] = df['B23001_001E']
    df['Pop_YRM'] = df['B23001_001M']
    df['Pop_YRC'] = df.apply(lambda x: (calc.get_cv(x['Pop_YRE'],x['Pop_YRM'])),axis=1)
    df['LF_YRE'] = df['DP03_0002E']
    df['LF_YRM'] = df['DP03_0002M']
    df['LF_YRC'] = df.apply(lambda x: (calc.get_cv(x['LF_YRE'],x['LF_YRM'])),axis=1)

    df['Pop1624_YRE'] = df.loc[:,Pop1624E].sum(axis=1)
    df['Pop1624_YRM'] = df.apply(lambda x: (calc.get_moe(x[Pop1624M])),axis=1)
    df['Pop1624_YRC'] = df.apply(lambda x: (calc.get_cv(x['Pop1624_YRE'],x['Pop1624_YRM'])),axis=1)
    df['LF1624_YRE'] = df.loc[:,LF1624E].sum(axis=1)
    df['LF1624_YRM'] = df.apply(lambda x: (calc.get_moe(x[LF1624M])),axis=1)
    df['LF1624_YRC'] = df.apply(lambda x: (calc.get_cv(x['LF1624_YRE'],x['LF1624_YRM'])),axis=1)

    df['Pop2554_YRE'] = df.loc[:,Pop2554E].sum(axis=1)
    df['Pop2554_YRM'] = df.apply(lambda x: (calc.get_moe(x[Pop2554M])),axis=1)
    df['Pop2554_YRC'] = df.apply(lambda x: (calc.get_cv(x['Pop2554_YRE'],x['Pop2554_YRM'])),axis=1)
    df['LF2554_YRE'] = df.loc[:,LF2554E].sum(axis=1)
    df['LF2554_YRM'] = df.apply(lambda x: (calc.get_moe(x[LF2554M])),axis=1)
    df['LF2554_YRC'] = df.apply(lambda x: (calc.get_cv(x['LF2554_YRE'],x['LF2554_YRM'])),axis=1)

    df['Pop5564_YRE'] = df.loc[:,Pop5564E].sum(axis=1)
    df['Pop5564_YRM'] = df.apply(lambda x: (calc.get_moe(x[Pop5564M])),axis=1)
    df['Pop5564_YRC'] = df.apply(lambda x: (calc.get_cv(x['Pop5564_YRE'],x['Pop5564_YRM'])),axis=1)
    df['LF5564_YRE'] = df.loc[:,LF5564E].sum(axis=1)
    df['LF5564_YRM'] = df.apply(lambda x: (calc.get_moe(x[LF5564M])),axis=1)
    df['LF5564_YRC'] = df.apply(lambda x: (calc.get_cv(x['LF5564_YRE'],x['LF5564_YRM'])),axis=1)

    df['PopO65_YRE'] = df.loc[:,PopO65E].sum(axis=1)
    df['PopO65_YRM'] = df.apply(lambda x: (calc.get_moe(x[PopO65M])),axis=1)
    df['PopO65_YRC'] = df.apply(lambda x: (calc.get_cv(x['PopO65_YRE'],x['PopO65_YRM'])),axis=1)
    df['LFO65_YRE'] = df.loc[:,LFO65E].sum(axis=1)
    df['LFO65_YRM'] = df.apply(lambda x: (calc.get_moe(x[LFO65M])),axis=1)
    df['LFO65_YRC'] = df.apply(lambda x: (calc.get_cv(x['LFO65_YRE'],x['LFO65_YRM'])),axis=1)

    df['Pop2534_YRE'] = df.loc[:,Pop2534E].sum(axis=1)
    df['Pop2534_YRM'] = df.apply(lambda x: (calc.get_moe(x[Pop2534M])),axis=1)
    df['Pop2534_YRC'] = df.apply(lambda x: (calc.get_cv(x['Pop2534_YRE'],x['Pop2534_YRM'])),axis=1)
    df['LF2534_YRE'] = df.loc[:,LF2534E].sum(axis=1)
    df['LF2534_YRM'] = df.apply(lambda x: (calc.get_moe(x[LF2534M])),axis=1)
    df['LF2534_YRC'] = df.apply(lambda x: (calc.get_cv(x['LF2534_YRE'],x['LF2534_YRM'])),axis=1)

    df['Pop3544_YRE'] = df.loc[:,Pop3544E].sum(axis=1)
    df['Pop3544_YRM'] = df.apply(lambda x: (calc.get_moe(x[Pop3544M])),axis=1)
    df['Pop3544_YRC'] = df.apply(lambda x: (calc.get_cv(x['Pop3544_YRE'],x['Pop3544_YRM'])),axis=1)
    df['LF3544_YRE'] = df.loc[:,LF3544E].sum(axis=1)
    df['LF3544_YRM'] = df.apply(lambda x: (calc.get_moe(x[LF3544M])),axis=1)
    df['LF3544_YRC'] = df.apply(lambda x: (calc.get_cv(x['LF3544_YRE'],x['LF3544_YRM'])),axis=1)

    df['Pop4554_YRE'] = df.loc[:,Pop4554E].sum(axis=1)
    df['Pop4554_YRM'] = df.apply(lambda x: (calc.get_moe(x[Pop4554M])),axis=1)
    df['Pop4554_YRC'] = df.apply(lambda x: (calc.get_cv(x['Pop4554_YRE'],x['Pop4554_YRM'])),axis=1)
    df['LF4554_YRE'] = df.loc[:,LF4554E].sum(axis=1)
    df['LF4554_YRM'] = df.apply(lambda x: (calc.get_moe(x[LF4554M])),axis=1)
    df['LF4554_YRC'] = df.apply(lambda x: (calc.get_cv(x['LF4554_YRE'],x['LF4554_YRM'])),axis=1)

    df['PopO55_YRE'] = df.loc[:,PopO55E].sum(axis=1)
    df['PopO55_YRM'] = df.apply(lambda x: (calc.get_moe(x[PopO55M])),axis=1)
    df['PopO55_YRC'] = df.apply(lambda x: (calc.get_cv(x['PopO55_YRE'],x['PopO55_YRM'])),axis=1)
    df['LFO55_YRE'] = df.loc[:,LFO55E].sum(axis=1)
    df['LFO55_YRM'] = df.apply(lambda x: (calc.get_moe(x[LFO55M])),axis=1)
    df['LFO55_YRC'] = df.apply(lambda x: (calc.get_cv(x['LFO55_YRE'],x['LFO55_YRM'])),axis=1)
    
    for col_name in df.columns:
        df.rename(columns={col_name:col_name.replace('YR',year[2:])},inplace=True) 
    return df


#Function to make labor force change variables
def make_lf_change(df,y0,y1):
    df[f'Pop_{y0[2:]}{y1[2:]}E'] = df[f'Pop_{y1[2:]}E'] - df[f'Pop_{y0[2:]}E']
    df[f'Pop_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'Pop_{y0[2:]}M'],\
                                                                             x[f'Pop_{y1[2:]}M']])),axis=1)
    df[f'Pop_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'Pop_{y0[2:]}{y1[2:]}E'],\
                                                                           x[f'Pop_{y0[2:]}{y1[2:]}M'])),axis=1)
    df[f'LF_{y0[2:]}{y1[2:]}E'] = df[f'LF_{y1[2:]}E'] - df[f'LF_{y0[2:]}E']
    df[f'LF_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'LF_{y0[2:]}M'],\
                                                                            x[f'LF_{y1[2:]}M']])),axis=1)
    df[f'LF_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'LF_{y0[2:]}{y1[2:]}E'],\
                                                                          x[f'LF_{y0[2:]}{y1[2:]}M'])),axis=1)

    df[f'Pop1624_{y0[2:]}{y1[2:]}E'] = df[f'Pop1624_{y1[2:]}E'] - df[f'Pop1624_{y0[2:]}E']
    df[f'Pop1624_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'Pop1624_{y0[2:]}M'],\
                                                                                 x[f'Pop1624_{y1[2:]}M']])),axis=1)
    df[f'Pop1624_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'Pop1624_{y0[2:]}{y1[2:]}E'],\
                                                                              x[f'Pop1624_{y0[2:]}{y1[2:]}M'])),axis=1)
    df[f'LF1624_{y0[2:]}{y1[2:]}E'] = df[f'LF1624_{y1[2:]}E'] - df[f'LF1624_{y0[2:]}E']
    df[f'LF1624_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'LF1624_{y0[2:]}M'],
                                                                               x[f'LF1624_{y1[2:]}M']])),axis=1)
    df[f'LF1624_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'LF1624_{y0[2:]}{y1[2:]}E'],\
                                                                              x[f'LF1624_{y0[2:]}{y1[2:]}M'])),axis=1)

    df[f'Pop2554_{y0[2:]}{y1[2:]}E'] = df[f'Pop2554_{y1[2:]}E'] - df[f'Pop2554_{y0[2:]}E']
    df[f'Pop2554_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'Pop2554_{y0[2:]}M'],\
                                                                                 x[f'Pop2554_{y1[2:]}M']])),axis=1)
    df[f'Pop2554_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'Pop2554_{y0[2:]}{y1[2:]}E'],\
                                                                               x[f'Pop2554_{y0[2:]}{y1[2:]}M'])),axis=1)
    df[f'LF2554_{y0[2:]}{y1[2:]}E'] = df[f'LF2554_{y1[2:]}E'] - df[f'LF2554_{y0[2:]}E']
    df[f'LF2554_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'LF2554_{y0[2:]}M'],\
                                                                               x[f'LF2554_{y1[2:]}M']])),axis=1)
    df[f'LF2554_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'LF2554_{y0[2:]}{y1[2:]}E'],\
                                                                              x[f'LF2554_{y0[2:]}{y1[2:]}M'])),axis=1)

    df[f'Pop5564_{y0[2:]}{y1[2:]}E'] = df[f'Pop5564_{y1[2:]}E'] - df[f'Pop5564_{y0[2:]}E']
    df[f'Pop5564_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'Pop5564_{y0[2:]}M'],\
                                                                                 x[f'Pop5564_{y1[2:]}M']])),axis=1)
    df[f'Pop5564_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'Pop5564_{y0[2:]}{y1[2:]}E'],\
                                                                              x[f'Pop5564_{y0[2:]}{y1[2:]}M'])),axis=1)
    df[f'LF5564_{y0[2:]}{y1[2:]}E'] = df[f'LF5564_{y1[2:]}E'] - df[f'LF5564_{y0[2:]}E']
    df[f'LF5564_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'LF5564_{y0[2:]}M'],\
                                                                                x[f'LF5564_{y1[2:]}M']])),axis=1)
    df[f'LF5564_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'LF5564_{y0[2:]}{y1[2:]}E'],\
                                                                             x[f'LF5564_{y0[2:]}{y1[2:]}M'])),axis=1)

    df[f'PopO65_{y0[2:]}{y1[2:]}E'] = df[f'PopO65_{y1[2:]}E'] - df[f'PopO65_{y0[2:]}E']
    df[f'PopO65_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'PopO65_{y0[2:]}M'],\
                                                                                x[f'PopO65_{y1[2:]}M']])),axis=1)
    df[f'PopO65_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'PopO65_{y0[2:]}{y1[2:]}E'],\
                                                                             x[f'PopO65_{y0[2:]}{y1[2:]}M'])),axis=1)
    df[f'LFO65_{y0[2:]}{y1[2:]}E'] = df[f'LFO65_{y1[2:]}E'] - df[f'LFO65_{y0[2:]}E']
    df[f'LFO65_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'LFO65_{y0[2:]}M'],\
                                                                               x[f'LFO65_{y1[2:]}M']])),axis=1)
    df[f'LFO65_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'LFO65_{y0[2:]}{y1[2:]}E'],\
                                                                             x[f'LFO65_{y0[2:]}{y1[2:]}M'])),axis=1)

    df[f'Pop2534_{y0[2:]}{y1[2:]}E'] = df[f'Pop2534_{y1[2:]}E'] - df[f'Pop2534_{y0[2:]}E']
    df[f'Pop2534_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'Pop2534_{y0[2:]}M'],\
                                                                                 x[f'Pop2534_{y1[2:]}M']])),axis=1)
    df[f'Pop2534_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'Pop2534_{y0[2:]}{y1[2:]}E'],\
                                                                               x[f'Pop2534_{y0[2:]}{y1[2:]}M'])),axis=1)
    df[f'LF2534_{y0[2:]}{y1[2:]}E'] = df[f'LF2534_{y1[2:]}E'] - df[f'LF2534_{y0[2:]}E']
    df[f'LF2534_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'LF2534_{y0[2:]}M'],\
                                                                                x[f'LF2534_{y1[2:]}M']])),axis=1)
    df[f'LF2534_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'LF2534_{y0[2:]}{y1[2:]}E'],\
                                                                              x[f'LF2534_{y0[2:]}{y1[2:]}M'])),axis=1)

    df[f'Pop3544_{y0[2:]}{y1[2:]}E'] = df[f'Pop3544_{y1[2:]}E'] - df[f'Pop3544_{y0[2:]}E']
    df[f'Pop3544_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'Pop3544_{y0[2:]}M'],\
                                                                                 x[f'Pop3544_{y1[2:]}M']])),axis=1)
    df[f'Pop3544_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'Pop3544_{y0[2:]}{y1[2:]}E'],\
                                                                               x[f'Pop3544_{y0[2:]}{y1[2:]}M'])),axis=1)
    df[f'LF3544_{y0[2:]}{y1[2:]}E'] = df[f'LF3544_{y1[2:]}E'] - df[f'LF3544_{y0[2:]}E']
    df[f'LF3544_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'LF3544_{y0[2:]}M'],\
                                                                                x[f'LF3544_{y1[2:]}M']])),axis=1)
    df[f'LF3544_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'LF3544_{y0[2:]}{y1[2:]}E'],\
                                                                             x[f'LF3544_{y0[2:]}{y1[2:]}M'])),axis=1)

    df[f'Pop4554_{y0[2:]}{y1[2:]}E'] = df[f'Pop4554_{y1[2:]}E'] - df[f'Pop4554_{y0[2:]}E']
    df[f'Pop4554_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'Pop4554_{y0[2:]}M'],\
                                                                                 x[f'Pop4554_{y1[2:]}M']])),axis=1)
    df[f'Pop4554_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'Pop4554_{y0[2:]}{y1[2:]}E'],\
                                                                               x[f'Pop4554_{y0[2:]}{y1[2:]}M'])),axis=1)
    df[f'LF4554_{y0[2:]}{y1[2:]}E'] = df[f'LF4554_{y1[2:]}E'] - df[f'LF4554_{y0[2:]}E']
    df[f'LF4554_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'LF4554_{y0[2:]}M'],\
                                                                                x[f'LF4554_{y1[2:]}M']])),axis=1)
    df[f'LF4554_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'LF4554_{y0[2:]}{y1[2:]}E'],\
                                                                              x[f'LF4554_{y0[2:]}{y1[2:]}M'])),axis=1)

    df[f'PopO55_{y0[2:]}{y1[2:]}E'] = df[f'PopO55_{y1[2:]}E'] - df[f'PopO55_{y0[2:]}E']
    df[f'PopO55_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'PopO55_{y0[2:]}M'],\
                                                                                x[f'PopO55_{y1[2:]}M']])),axis=1)
    df[f'PopO55_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'PopO55_{y0[2:]}{y1[2:]}E'],\
                                                                              x[f'PopO55_{y0[2:]}{y1[2:]}M'])),axis=1)
    df[f'LFO55_{y0[2:]}{y1[2:]}E'] = df[f'LFO55_{y1[2:]}E'] - df[f'LFO55_{y0[2:]}E']
    df[f'LFO55_{y0[2:]}{y1[2:]}M'] = df.apply(lambda x: (calc.get_moe([x[f'LFO55_{y0[2:]}M'],\
                                                                               x[f'LFO55_{y1[2:]}M']])),axis=1)
    df[f'LFO55_{y0[2:]}{y1[2:]}C'] = df.apply(lambda x: (calc.get_cv(x[f'LFO55_{y0[2:]}{y1[2:]}E'],\
                                                                             x[f'LFO55_{y0[2:]}{y1[2:]}M'])),axis=1)
    
    return df