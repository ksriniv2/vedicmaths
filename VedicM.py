# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:53:32 2020

@author: KARTH
"""

class VedicM:
    
    
   
    def complement(inpComplement,learn=False):
        if learn:
            VedicM("compliment")
            
        #print(inpComplement)
        rarr=[]
        lastdigit=0
        if str(inpComplement).isnumeric():
            #strinp=str(inpComplement)
            #print(strinp)
            
            for idx,idigit in enumerate(reversed(inpComplement)):
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
        
    def subtract(inpNumerator,inpDenominator,learn=False):
        if learn:
            VedicM("subtract")
            
        #print(inpComplement)
        rarr=[]
        complement=0
        swap=0
        
        
        if str(inpNumerator).isnumeric() and str(inpDenominator).isnumeric():
            
            if float(inpNumerator) < float(inpDenominator):
                swap=inpNumerator
                inpNumerator=inpDenominator
                inpDenominator=swap
                swap=1
                
            
            lenNumerator=len(inpNumerator)
            lenDenominator=len(inpDenominator)
            
            lstNumerator=list(reversed(inpNumerator))
            lstDenominator=list(reversed(inpDenominator))
        #print(lstNumerator)
        #print(lstDenominator)
            
            if lenNumerator-lenDenominator > 0:
                for i in range(lenNumerator-lenDenominator):
                    lstDenominator.append('0')
            if lenDenominator-lenNumerator > 0:
                for i in range(lenDenominator-lenNumerator):
                    lstNumerator.append('0')
            #print(lstNumerator)
            #print(lstDenominator)
            for idx,indigit in enumerate(lstNumerator):
                cachesub=int(indigit) - int(lstDenominator[idx])
                if (cachesub > 0) and complement==0:
                    rarr.append(cachesub)
                elif (cachesub > 0) and complement==1:
                    rarr.append(cachesub-1)
                    complement=0
                elif(cachesub < 0) and complement==0:
                    rarr.append(10 - abs(cachesub))
                    complement=1
                elif(cachesub < 0) and complement==1:
                    rarr.append(9 - abs(cachesub))
            str_nums = [str(x) for x in reversed(rarr)]
            #print(str_nums)
            if swap > 0:
               return('-'+ ''.join(str_nums))
            else:
                return(''.join(str_nums))
                    
    
    def __init__(self,method=False):
        print("Entering the world of Vedic Maths")
        
        if method=='complement':
            print("Sutra is : Nikhilam Navatascarmam Dasatah")
            print("Meaning : All from nine and last from ten")
        elif method=='subtract':
            print("Sutra is : Nikhilam Navatascarmam Dasatah")
            print("Meaning : All from nine and last from ten")
            print("There is no carry over in this method")
            print("1. Do normal subtraction when the numerator digit is bigger than lower digit")
            print("2. Go to complements when the lower digit is bigger than upper digit")
            print("3.First time complement has to be from 10 and later on with 9")
            print("4. When the numerator digit is bigger again, come out of complement and subtract extra 1 and later start the new complement from 10 for subsequent digits")
            
        