# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:22:10 2020

@author: KARTH
"""
import os
import psutil
import time

from VedicM import VedicM

vm=VedicM()





print(vm.complement('0005',True))

print(vm.subtract('482649534595734','482649534595704',True))





#start = time.process_time()
print(vm.mul11('482649534595734983493434989834321342532668578697454351481293048120348',True) )  
#print(time.process_time() - start)

#start = time.process_time()
#print(vm.test() )  
#print(time.process_time() - start)

print("Multiply by 12")
print(vm.mul12('26154',True) )  
print(26154*12)      

#print(time.process_time())
print(vm.mul9('482649534595734983493434989834321342532668578697454351481293048120348','999999999999999999999999999999999999999999999999999999999999999999999','True'))     

print(482649534595734983493434989834321342532668578697454351481293048120348 * 999999999999999999999999999999999999999999999999999999999999999999999)
#print(time.process_time())



print(482649534595734983493434989834321342532668578697454351481293048120348*999999999999999999999999999999999999999999999999999999999999999999999)     
 

print(vm.mul9('46972','99',True))  
print(46972*99)  



print(vm.mul2d('98','97',True))  

print(98*97)
                
#in the command line of ipython

# %load_ext memory_profiler
# from VedicM import VedicM
# number=5670
#number1='482649534595734'
#number2='3'
# %mprun -f VedicM.mul11 VedicM.mul11(number1)       
#%mprun -f VedicM.test VedicM.test()       
            
            
            


