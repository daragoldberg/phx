import math
import numpy as np

def get_se(per_wt,rep_weights):
    result = math.sqrt((sum(map(lambda x: (x-per_wt)**2,rep_weights))/40))
    return result

def get_moe(se):
    return se*1.645 #90% confidence interval

def get_agg_moe(m):
    result = math.sqrt(sum(map(lambda x: x**2, m)))
    return result
                       
def get_cv(est,m):
    if est == 0:
        return 0
    else:
        return (np.absolute(m/1.645/est))*100

def get_cv_from_se(est,se):
    if est == 0:
        return 0
    else:
        return (np.absolute(se/est))*100
    
#def get_se_2(per_wt,rep_weights):
#    result = math.sqrt((sum(map(lambda x: (x-per_wt)**2,rep_weights))/20)
#    return result