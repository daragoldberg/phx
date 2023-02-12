# Variables needed for ACS analysis
# lists of estimates and margins of error needed for various data pulllls

## RENT-BURDEN ##
# B25070 GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME IN THE PAST 12 MONTHS

#variable groupings and reassignments - less than 30%, 30-50%, 50%+ on rent
r_tot_e = ['B25070_001E']
r_tot_m = ['B25070_001M']
r_u30_e = ['B25070_002E','B25070_003E','B25070_004E','B25070_005E','B25070_006E']
r_u30_m = ['B25070_002M','B25070_003M','B25070_004M','B25070_005M','B25070_006M']
r_3050_e = ['B25070_007E','B25070_008E','B25070_009E']
r_3050_m = ['B25070_007M','B25070_008M','B25070_009M']
r_o50_e = ['B25070_010E']
r_o50_m = ['B25070_010M']
r_na_e = ['B25070_011E']
r_na_m = ['B25070_011M']

rent_vars = r_tot_e + r_tot_m + r_u30_e + r_u30_m + r_3050_e + r_3050_m + r_o50_e + r_o50_m + r_na_e + r_na_m



## OWNER COST-BURDEN ##
# B25091 MORTGAGE STATUS BY SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME IN THE PAST 12 MONTHS

#variable groupings and reassignments - less than 30%, 30-50%, 50%+ on owner costs (with/without mortgage)
tot_e = ['B25091_001E']
tot_m = ['B25091_001M']

#with a mortgage
om_tot_e = ['B25091_002E']
om_tot_m = ['B25091_002M']
om_u30_e = ['B25091_003E','B25091_004E','B25091_005E','B25091_006E','B25091_007E']
om_u30_m = ['B25091_003M','B25091_004M','B25091_005M','B25091_006M','B25091_007M']
om_3050_e = ['B25091_008E','B25091_009E','B25091_010E']
om_3050_m = ['B25091_008M','B25091_009M','B25091_010M']
om_o50_e = ['B25091_011E']
om_o50_m = ['B25091_011M']
om_na_e = ['B25091_012E']
om_na_m = ['B25091_012M']

#without a mortgage
on_tot_e = ['B25091_013E']
on_tot_m = ['B25091_013M']
on_u30_e = ['B25091_014E','B25091_015E','B25091_016E','B25091_017E','B25091_018E']
on_u30_m = ['B25091_013M','B25091_014M','B25091_015M','B25091_016M','B25091_017M','B25091_018M']
on_3050_e = ['B25091_019E','B25091_020E','B25091_021E']
on_3050_m = ['B25091_019M','B25091_020M','B25091_021M']
on_o50_e = ['B25091_022E']
on_o50_m = ['B25091_022M']
on_na_e = ['B25091_022M']
on_na_m = ['B25091_023M']

#all owners combined
o_tot_e = om_tot_e + on_tot_e
o_tot_m = om_tot_m + on_tot_m
o_u30_e = om_u30_e + on_u30_e
o_u30_m = om_u30_m + on_u30_m
o_3050_e = om_3050_e + on_3050_e
o_3050_m = om_3050_m + on_3050_m
o_o50_e = om_o50_e + on_o50_e
o_o50_m = om_u30_m + on_o50_m
o_na_e = om_na_e + on_na_e
o_na_m = om_na_m + on_na_m


own_vars = tot_e + tot_m + o_tot_e + o_tot_m + o_u30_e + o_u30_m + o_3050_e + o_3050_m + \
           o_o50_e + o_o50_m + o_na_e + o_na_m