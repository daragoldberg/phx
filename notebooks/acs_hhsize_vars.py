# Variables needed for ACS analysis
# lists of estimates and margins of error needed for various data pulls

## POPULATION BY TENURE ##
# B25008 TOTAL POPULATION IN OCCUPIED HOUSING UNITS BY TENURE (universe = population)

ten_rename={'B25008_001E':'p_tot_E','B25008_001M':'p_tot_M',\
            'B25008_002E':'p_o_E','B25008_002M':'p_o_M',\
            'B25008_003E':'p_r_E','B25008_003M':'p_r_M'}


## TENURE BY HOUSEHOLD SIZE ##
# B25009 TENURE BY HOUSEHOLD SIZE (universe = occupied housing units)

hh_rename={'B25009_001E':'h_tot_E','B25009_001M':'h_tot_M','B25009_002E':'h_otot_E',\
           'B25009_002M':'h_otot_M','B25009_003E':'h_o1_E','B25009_003M':'h_o1_M',\
           'B25009_004E':'h_o2_E','B25009_004M':'h_o2_M','B25009_010E':'h_rtot_E',\
           'B25009_010M':'h_rtot_M','B25009_011E':'h_r1_E','B25009_011M':'h_r1_M',\
          'B25009_012E':'h_r2_E','B25009_012M':'h_r2_M'}

#owner occupied 
h_o35_E = ['B25009_005E','B25009_006E','B25009_007E']
h_o5p_E = ['B25009_008E','B25009_009E']
h_o35_M = ['B25009_005M','B25009_006M','B25009_007M']
h_o5p_M = ['B25009_008M','B25009_009M']

own_vars  = h_o35_E + h_o5p_E + h_o35_M + h_o5p_M

#renter occupied
h_r35_E = ['B25009_013E','B25009_014E','B25009_015E']
h_r5p_E = ['B25009_016E','B25009_017E']

h_r35_M = ['B25009_013M','B25009_014M','B25009_015M']
h_r5p_M = ['B25009_016M','B25009_017M']

rent_vars  = h_r35_E + h_r5p_E + h_r35_M + h_r5p_M