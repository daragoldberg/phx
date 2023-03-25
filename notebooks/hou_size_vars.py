# Variables needed for ACS analysis
# lists of estimates and margins of error needed for various data pulls

## HOUSING BY BUILDING SIZE ##
# B25024 UNITS IN STRUCTURE (universe = housing units)

#Housing unit variables we want from table DP04:
#- 001 = total units
#- 002 = 1 unit detached
#- 003 = 1 unit attached
#- 004 = 2 units
#- 005 = 3 or 4 units
#- 006 = 5 to 9 units 
#- 007 = 10 to 19 units
#- 008 = 20-49 units
#- 009 = 50+ units
#- 010 = Mobile home
#- 011 = RV, boat, other

hou_rename = {'B25024_001E':'u_tot_E','B25024_001M':'u_tot_M','B25024_006E':'u_59_E',\
              'B25024_006M':'u_59_M','B25024_007E':'u_1019_E','B25024_007M':'u_1019_M',\
              'B25024_008E':'u_2049_E','B25024_008M':'u_2049_M','B25024_009E':'u_o50_E',\
              'B25024_009M':'u_o50_M',}

#Create separate lists for estimates and MOEs for aggregation
U1E = ['B25024_002E','B25024_003E']
U1M = ['B25024_002M','B25024_003M']
U24E = ['B25024_004E','B25024_005E']
U24M = ['B25024_004M','B25024_005M']
U520E = ['B25024_006E','B25024_007E']
U520M = ['B25024_006M','B25024_007M']
Uo20E = ['B25024_008E','B25024_009E']
Uo20M = ['B25024_008M','B25024_009M']
UOthE = ['B25024_010E','B25024_011E']
UOthM = ['B25024_010M','B25024_011M']

#all variables we want to delete after usee
hou_vars = U1E+U1M+U24E+U24M+UOthE+UOthM