#------------------------library import------------------------
from numpy import random,sqrt,log,sin,cos,pi
import numpy as np

#----------------------------------------------------
#------------------------1-a-------------------------
#----------------------------------------------------
def gaussian_data_generator(mean,var):
    """
        <<1-a>>    
        CLT
    """
    '''
        input mean and var
        Z~gaussian(0,1)-> Z=X-mean / std    
        X~gaussian(mean,var) -> X=Z*std+mean
    '''
    std=sqrt(var)
    random_data=np.sum(np.random.uniform(size = 12))-6
    #------------------------------------
    #------------calculate random data-------------
    #------------------------------------
    print('\n')
    random_data=random_data*std+mean
    return(random_data)


"""
    Problem2
"""
print('########Problem 2 ########')
print('########Enter Problem 2 input based on 1-a:########')
print('Enter mean:')
mean=float(input())
print('Enter var:')
var=float(input())

'''
    Setting:
            new_mean=old_mean + sum_of_new_data_point/new_data_deominator
            new_var=old_var + var_of_new_data
'''
print('Data point source function : N(%f,%f)' %(mean,var))
new_data_num=0
old_mean=mean
old_var=var
threshold=0.0001

while(True):
    new_data=gaussian_data_generator(mean,var)
    new_data_num+=1
    
    #Update mean
    new_mean=(old_mean*new_data_num+new_data)/(new_data_num+1)
    change_of_mean=abs(mean-new_mean)
    
    #Update var
    new_var = (old_var + (new_data-new_mean)**2/(new_data_num+1) - old_var/(new_data_num))
    change_of_var=abs(new_var-old_var)
    
    #show the result
    print('Add data point: %f' %(new_data))
    print('Mean=%f Var=%f' %(new_mean,new_var))
    
    #Update old_mean
    old_mean=new_mean
    old_var=old_var
    #Convergance or not 
    if change_of_mean<threshold and  change_of_var<threshold:
        break