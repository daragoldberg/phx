#https://housing.az.gov/sites/default/files/documents/files/2010_HOME-HTF_Rent-Income%2520Limits.pdf

#AMI BANDS
AMI_30pct = {'1':14000,'2':16000,'3':18000,'4':20000,'5':21600,'6':23200,
            '7':24800,'8':26400}
AMI_50pct = {'1':23350,'2':26650,'3':30000,'4':33300,'5':36000,'6':38650,
            '7':41300,'8':44000}
AMI_80pct = {'1':37350,'2':42650,'3':48000,'4':53300,'5':57600,'6':61850,
            '7':66100,'8':70400}
AMI_100pct = {'1':46688,'2':53313,'3':60000,'4':66625,'5':72000,'6':77313,
            '7':82625,'8':88000}
AMI_120pct = {'1':56025,'2':63975,'3':72000,'4':79950,'5':86400,'6':92775,
            '7':99150,'8':105600}

inc_lbl = ['u30_ami',
           '30_50_ami',
           '50_80_ami',
           '80_100_ami',
           '100_120_ami',
           'o120_ami']