# Variables needed for ACS analysis
# lists of estimates and margins of error needed for various data pulls

# B17001 POVERTY STATUS IN THE PAST 12 MONTHS BY SEX BY AGE

col_pov = 'GEO_ID,NAME,B17001_001E,B17001_001M,B17001_002E,B17001_002M,B17001A_001E,B17001A_001M,B17001A_002E,B17001A_002M,B17001B_001E,B17001B_001M,B17001B_002E,B17001B_002M,B17001C_001E,B17001C_001M,B17001C_002E,B17001C_002M,B17001D_001E,B17001D_001M,B17001D_002E,B17001D_002M,B17001E_001E,B17001E_001M,B17001E_002E,B17001E_002M,B17001F_001E,B17001F_001M,B17001F_002E,B17001F_002M,B17001G_001E,B17001G_001M,B17001G_002E,B17001G_002M,B17001H_001E,B17001H_001M,B17001H_002E,B17001H_002M,B17001I_001E,B17001I_001M,B17001I_002E,B17001I_002M'


oth_e = ['B17001E_001E','B17001F_001E','B17001G_001E']
oth_m = ['B17001E_001M','B17001F_001M','B17001G_001M']
oth_pov_e = ['B17001E_002E','B17001F_002E','B17001G_002E']
oth_pov_m = ['B17001E_002M','B17001F_002M','B17001G_002M']

oth = oth_e + oth_m + oth_pov_e + oth_pov_m

pov_rename = {'B17001_001E':'tot_E','B17001_001M':'tot_M','B17001_002E':'tot_pov_E',\
      'B17001_002M':'tot_pov_M','B17001A_001E':'whi_E','B17001A_001M':'whi_M',\
      'B17001A_002E':'whi_pov_E','B17001A_002M':'whi_pov_M',\
      'B17001B_001E':'bla_E','B17001B_001M':'bla_M','B17001B_002E':'bla_pov_E',\
      'B17001B_002M':'bla_pov_M','B17001C_001E':'ame_E','B17001C_001M':'ame_M',\
      'B17001C_002E':'ame_pov_E','B17001C_002M':'ame_pov_M','B17001D_001E':'asi_E',\
      'B17001D_001M':'asi_M','B17001D_002E':'asi_pov_E','B17001D_002M':'asi_pov_M',\
      'B17001H_001E':'whnon_E','B17001H_001M':'whnon_M','B17001H_002E':'whnon_pov_E',\
      'B17001H_002M':'whnon_pov_M','B17001H_001E':'whnon_E','B17001H_001M':'whnon_M',\
      'B17001H_002E':'whnon_pov_E','B17001H_002M':'whnon_pov_M','B17001I_001E':'his_E',\
      'B17001I_001M':'his_M','B17001I_002E':'his_pov_E','B17001I_002M':'his_pov_M'}




#total pop
col_tot = 'NAME,B17001_001E,B17001_001M,B17001_002E,B17001_002M,B17001_031E,B17001_031M'
#white alone
col_whi = 'NAME,B17001A_001E,B17001A_001M,B17001A_002E,B17001A_002M,B17001A_031E,B17001A_031M'
#black alone
col_bla = 'NAME,B17001B_001E,B17001B_001M,B17001B_002E,B17001B_002M,B17001B_031E,B17001B_031M'
#american indian alone
col_ame = 'NAME,B17001C_001E,B17001C_001M,B17001C_002E,B17001C_002M,B17001C_031E,B17001C_031M'
#asian alone
col_asi = 'NAME,B17001D_001E,B17001D_001M,B17001D_002E,B17001D_002M,B17001D_031E,B17001D_031M'
#hawaiian alone
col_haw = 'NAME,B17001E_001E,B17001E_001M,B17001E_002E,B17001E_002M,B17001E_031E,B17001E_031M'
#other alone
col_oth = 'NAME,B17001F_001E,B17001F_001M,B17001F_002E,B17001F_002M,B17001F_031E,B17001F_031M'
#two or more
col_two = 'B17001G_001E,B17001G_001M,B17001G_002E,B17001G_002M,B17001G_031E,B17001G_031M'
#white non hispanic
col_whnon = 'NAME,B17001H_001E,B17001H_001M,B17001H_002E,B17001H_002M,B17001H_031E,B17001H_031M'
#hispanic
col_his = 'NAME,B17001I_001E,B17001I_001M,B17001I_002E,B17001I_002M,B17001I_031E,B17001I_031M'

