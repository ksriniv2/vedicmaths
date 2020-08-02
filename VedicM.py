# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:53:32 2020

@author: KARTH
"""

class VedicM:
    
    

    def complement(self,inpComplement,learn=False):
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
        
    def subtract(self,inpNumerator,inpDenominator,learn=False):
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
                elif (cachesub==0 and complement==0):
                    rarr.append(0)
                elif (cachesub==0 and complement ==1 ):
                    rarr.append(9)
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
    def mul11(self,inpMultiply,learn=False):
        if learn:
                VedicM("Multiply11")
                
            #print(inpComplement)
        carryover=0
        rarr=[]
        lstMultiply=[]
        
        if str(inpMultiply).isnumeric():
            
            lstMultiply=list(reversed(inpMultiply))
            lstMultiply.append('0')
            lstMultiply=['0']+lstMultiply
            #print(lstMultiply)
            for idx,iDigit in enumerate(lstMultiply):
                if idx < len(lstMultiply)-1:
                    cacheadd=int(iDigit) + int(lstMultiply[idx +1])
                    #print(cacheadd)
                    if (cacheadd+carryover ) > 10:
                        rarr.append(cacheadd-10+carryover)
                        carryover=1
                    elif (cacheadd+carryover ) == 10:
                        rarr.append(cacheadd-10+carryover)
                        carryover=1
                    else:
                        rarr.append(cacheadd+carryover)
                        carryover=0
            str_nums = [str(x) for x in reversed(rarr)]
            return(''.join(str_nums))
                    
    def mul12(self,inpMultiply,learn=False):
        if learn:
                VedicM("Multiply12")
                
            #print(inpComplement)
        carryover=0
        rarr=[]
        lstMultiply=[]
        
        if str(inpMultiply).isnumeric():
            
            lstMultiply=list(reversed(inpMultiply))
            lstMultiply.append('0')
            lstMultiply=['0']+lstMultiply
            #print(lstMultiply)
            for idx,iDigit in enumerate(lstMultiply):
                if idx < len(lstMultiply)-1:
                    cacheadd=int(iDigit) + (2 * (int(lstMultiply[idx +1])))
                    #print(cacheadd)
                    if (cacheadd+carryover ) > 10:
                        rarr.append(cacheadd-10+carryover)
                        carryover=1
                    elif (cacheadd+carryover ) == 10:
                        rarr.append(cacheadd-10+carryover)
                        carryover=1
                    else:
                        rarr.append(cacheadd+carryover)
                        carryover=0
            str_nums = [str(x) for x in reversed(rarr)]
            return(''.join(str_nums))
        
        
    def mul9 (self,inpMultiplicand,inpMultiplier,learn=False):
        
        eqdigit=''
        if learn:
            VedicM("Multiply9")
            
        if str(inpMultiplier).isnumeric() and str(inpMultiplicand).isnumeric():
            if len(str(inpMultiplier))==len(str(inpMultiplicand)):
                step1=self.subtract(inpMultiplicand,'1')
                step2=self.complement(inpMultiplicand)
                return(step1+step2)
            elif len(str(inpMultiplier)) > len(str(inpMultiplicand)):
                step0=len(str(inpMultiplier)) - len(str(inpMultiplicand))
                for iter in range(step0):
                    eqdigit=eqdigit+'0'
                inpMultiplicand=eqdigit+inpMultiplicand
                step1=self.subtract(inpMultiplicand,'1')
                step2=self.complement(inpMultiplicand)
                return(step1+step2)
            elif len(str(inpMultiplier)) < len(str(inpMultiplicand)):
                
                inpMultiplicandleft= ''.join(list(inpMultiplicand)[:(len(str(inpMultiplicand)) - len(str(inpMultiplier)))])
                
                inpMultiplicandright=''.join(list(inpMultiplicand)[-1*len(inpMultiplier):])
                
                inpMultiplicandleft=str(int(inpMultiplicandleft) +1)
                step1=self.subtract(inpMultiplicand,inpMultiplicandleft)
                step2=self.complement(inpMultiplicandright)
                return(step1+step2)
          
    def mulcross2d (self,inplMultiplicand,inplMultiplier):
        return(int(inplMultiplicand[0])* int(inplMultiplier[1]) + (int(inplMultiplicand[1])* int(inplMultiplier[0])))

    def mulcross3d (self,inplMultiplicand,inplMultiplier):
        return(int(inplMultiplicand[0])* int(inplMultiplier[2]) + (int(inplMultiplicand[2])* int(inplMultiplier[0])))            

                                                
        
    def mul2d (self,inpMultiplicand,inpMultiplier,learn=False):
        
       if learn:
            VedicM("Multiply2digit")
        
       if str(inpMultiplier).isnumeric() and len(inpMultiplier)==2 and  len(inpMultiplicand)==2 and str(inpMultiplicand).isnumeric():
          lstMultiplicand=list(reversed(inpMultiplicand)) 
          lstMultiplier=list(reversed(inpMultiplier)) 
          
          step1=int(lstMultiplicand[0]) * int(lstMultiplier[0])
          #print(step1)
          
          step2=self.mulcross2d(lstMultiplicand,lstMultiplier) + int(list(str(step1))[0] if len(str(step1)) > 1 else 0)
          #print(step2)
          step2Carry=list(str(step2))[0] if len(str(step2)) == 2 else list(str(step2))[0]+list(str(step2))[1] if len(str(step2)) == 3  else 0
          #print(step2Carry)
          step3=int(lstMultiplicand[1]) * int(lstMultiplier[1]) + int(step2Carry)
          #print(step3)
          
          return(str(step3)+list(str(step2))[-1]+list(str(step1))[-1])
          
                 
    def mul3d(self,inpMultiplicand,inpMultiplier,learn=False):
        if learn:
            VedicM("Multiply3digit")
            
        if str(inpMultiplier).isnumeric() and len(inpMultiplier)==3 and  len(inpMultiplicand)==3 and str(inpMultiplicand).isnumeric():
            lstMultiplicand=list(reversed(inpMultiplicand)) 
            lstMultiplier=list(reversed(inpMultiplier)) 
            step1=int(lstMultiplicand[0]) * int(lstMultiplier[0])
            print(step1)
            step2=self.mulcross2d(lstMultiplicand,lstMultiplier) + int(list(str(step1))[0] if len(str(step1)) > 1 else 0)
            print(step2)
            step2Carry=list(str(step2))[0] if len(str(step2)) == 2 else list(str(step2))[0]+list(str(step2))[1] if len(str(step2)) == 3  else 0
            print(step2Carry)
            step3_vm=int(lstMultiplicand[1]) * int(lstMultiplier[1])
            step3_cm=self.mulcross3d(lstMultiplicand,lstMultiplier)
            step3=step3_cm+step3_vm+int(step2Carry)
            print(step3)
            step3Carry=list(str(step3))[0] if len(str(step3)) == 2 else list(str(step3))[0]+list(str(step3))[1] if len(str(step3)) == 3  else 0
            print(step3Carry)
            step4=self.mulcross2d(lstMultiplicand[1:],lstMultiplier[1:])+int(step3Carry)
            print(step4)
            step4Carry=list(str(step4))[0] if len(str(step4)) == 2 else list(str(step4))[0]+list(str(step4))[1] if len(str(step4)) == 3  else 0
            print(step4Carry)
            step5=int(lstMultiplicand[2]) * int(lstMultiplier[2])+int(step4Carry)
            return (str(step5)+list(str(step4))[-1]+list(str(step3))[-1]+list(str(step2))[-1]+list(str(step1))[-1])
            
        
        
    
        
        

        
    def test(self):
        print(482649534595734983493434989834321342532668578697454351481293048120348 * 11)
    
    def __init__(self,method=False):
        print("Entering the world of Vedic Maths")
        print("*********************************")
        
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
            
            
        elif method=='Multiply11':
            print("Sutra is : Antyayoreva")
            print("Meaning : Only the last two digits")
            print("Add only the last two digits at a time from base10. We dont need to any multiplication")
            
        elif method=='Multiply12':
            print("Sutra is : Sopaantyadvayamantyam")
            print("Meaning : The ultimate and twice the penultimate")
            print("Add only the last digit with twice the penultimate at a time from base10. We dont need to any multiplication")
            
            
        elif method=='Multiply9':
            print("Sutra is : Nikhilam Navatascarmam Dasatah")
            print("Meaning : All from nine and last from ten")
            print('Subtract 1 from the multiplicand')
            print('Obtain complement of the multiplicand')
            print('concatenate the values together')
        elif method=='Multiply2digit':
            print("Sutra is : Urdhvatiryabhyaam")
            print("Meaning : Vertical and cross wire")
            print('Vertically multiply digits of first column on right')
            print('Cross multiply the digits across')
            print('Vertically multiply digits of first column on right')
            print('In each step, carry over the other digits')
            
        elif method=='Multiply3digit':
            print("Sutra is : Urdhvatriyagbhyaam")
            print("Meaning : Vertical and cross wire")
            print('Vertically multiply digits of first column on right')
            print('Cross multiply the digits across')
            print('Combine Vertical and cross multiply')
            print('Cross multiply the digits across')
            print('Vertically multiply digits of first column on right')
            print('In each step, carry over the other digits')
        
    
            
        
            
            
        
