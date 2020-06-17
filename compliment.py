# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:56:13 2020

@author: KARTH
"""

from VedicM import VedicM
class compliment:
    def compliment(inpCompliment,learn=False):
        if learn:
            VedicM("compliment")
            
        #print(inpCompliment)
        rarr=[]
        lastdigit=0
        if str(inpCompliment).isnumeric():
            #strinp=str(inpCompliment)
            #print(strinp)
            
            for idx,idigit in enumerate(reversed(inpCompliment)):
                if idx==0:
                    if idigit!='0':
                        rarr.append(10-int(idigit))
                    else:
                        lastdigit=1
                        rarr.append(0)
                else:
                    if lastdigit==1 and idigit !='0':
                        rarr.append(10-int(idigit))
                        lastdigit=2
                    elif lastdigit==1 and idigit=='0':
                        rarr.append(0)                  
              
                        
                    else:
                        rarr.append(9-int(idigit))
            str_nums = [str(x) for x in reversed(rarr)]
            print(''.join(str_nums))
                    
        
            

    
