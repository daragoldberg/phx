#AMI BANDS
AMI_30pct = {'1':18550,'2':21200,'3':23850,'4':27750,'5':32470,'6':37190,
            '7':41910,'8':46630}
AMI_50pct = {'1':30950,'2':35350,'3':39750,'4':44150,'5':47700,'6':51250,
            '7':54750,'8':58300}
AMI_80pct = {'1':49500,'2':56550,'3':63600,'4':70650,'5':76350,'6':82000,
            '7':87650,'8':93300}
AMI_100pct = {'1':62200,'2':71050,'3':79950,'4':88800,'5':95950,'6':103050,
            '7':110150,'8':117250}
AMI_120pct = {'1':74600,'2':85250,'3':95950,'4':106560,'5':115100,'6':123650,
            '7':132150,'8':140700}

#Housing costs affordable to different AMI bands based on household size

## FIX ALL OF THESE
affordable_rent = {'1':[0,415,691,1106,1383,1659,1000000000],
              '2':[0,475,790,1265,1580,1896,1000000000],
              '3':[0,549,888,1423,1775,2133,1000000000],
              '4':[0,663,988,1580,1975,2370,1000000000],
              '5':[0,776,1068,1708,2135,2562,1000000000],
              '6':[0,890,1146,1834,2293,2751,1000000000],
              '7':[0,1003,1225,1960,2450,2940,1000000000],
              '8':[0,1117,1304,2450,2608,3129,1000000000]}

inc_lbl = ['u30_ami',
           '30_50_ami',
           '50_80_ami',
           '80_100_ami',
           '100_120_ami',
           'o120_ami']