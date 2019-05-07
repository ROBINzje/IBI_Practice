# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:29:48 2019

@author: ROBIN
"""
import time
start=time.clock()
from itertools import combinations



times0=0
sign=['+','-','/-','*','/','//']
numbers=list(input('give me a sequense of number: '))

class Calculator:
    
    def _init_(self, object):
        pass
       
    def division(self,x,times):                
        if len(x[0])>1:
           times+=1
           parallel=[] 
           for ic in x:                    
               select2=list(combinations(ic,2))
               for twonumbers in select2:
                   i=ic.copy()
                   lp1=list(twonumbers)
                   i.remove(lp1[0])   
                   i.remove(lp1[1])    
                   try:
                       for j in sign:
                           group=[]
                           if j=='+':
                               group=i+[lp1[0]+lp1[1]] 
                               
                               parallel.append(group)
                           elif j=='-':
                               group=i+[lp1[0]-lp1[1]]
                                   
                               parallel.append(group)
                           elif j=='/-':
                               group=i+[lp1[1]-lp1[0]]
                                   
                               parallel.append(group)
                           elif j=='*':
                               group=i+[lp1[0]*lp1[1]]
                                       
                               parallel.append(group)
                           elif j=='/':
                               group=i+[lp1[0]/lp1[1]]
                           
                               parallel.append(group)
                           elif j=='//':
                               group=i+[lp1[1]/lp1[0]]
                                   
                               parallel.append(group)
                   except ZeroDivisionError: continue
           self.division(parallel,times)        
                   
        elif len(x[0])==1: 
            for j in x:              
                if j ==[24.0]or j==[24]:
                    return(print('yes'+str(times)))                   
            return(print('nosolution'))

    def solution(self,x):
        overalllist=[x]        
        return(self.division(overalllist,0))
        
c=Calculator()    
c.solution(numbers)
end=time.clock()
print(end-start)
           
    
