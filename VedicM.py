# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:53:32 2020

@author: KARTH
"""

class VedicM:
    
    
   
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
            return(''.join(str_nums))
                    
    
    def __init__(self,method=False):
        print("Entering the world of Vedic Maths")
        
        if method=='compliment':
            print("Sutra is : Nikhilam Navatascarmam Dasatah")
            print("Meaning : All from nine and last from ten")
            
        
