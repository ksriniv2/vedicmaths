# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:22:10 2020

@author: KARTH
"""
import os
import psutil
import time

from VedicM import VedicM


print(VedicM.complement('5670',False))

print(VedicM.subtract('482649534595734','482649534595733',False))


print(482649534595734 - 482649534595733)


start = time.process_time()
print(VedicM.mul11('482649534595734983493434989834321342532668578697454351481293048120348',True) )  
print(time.process_time() - start)

start = time.process_time()
print(VedicM.test() )  
print(time.process_time() - start)


print(VedicM.mul12('26154',True) )        
     
                
                
#in the command line of ipython

# %load_ext memory_profiler
# from VedicM import VedicM
# number=5670
#number1='482649534595734'
#number2='3'
# %mprun -f VedicM.mul11 VedicM.mul11(number1)       
#%mprun -f VedicM.test VedicM.test()       
            
            
            


