#-*- encoding: gb18030 -*-
'''
Created on 2019幄1�7朄1�7旄1�7

@author: sanoi

'''
 
def anonymous(x):
    return x**2 + 1
def integrate(fun, start, end):
    step = 1
    intercept = start
    area = 0
    while intercept < end-1:
        intercept += step
        
        ''' your work here '''
        if intercept%3==0 or intercept%5==0:
            print(intercept)
            area=intercept+area;
        
    return area
        
print(integrate(anonymous, 0, 1000))