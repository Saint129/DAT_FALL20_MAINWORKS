# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:18:44 2020

@author: Avit_
"""

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]



def show_icon():
    for image in picture:
      for pixel in image:
        if (pixel):
          print('#', end ="")
        else:
          print(' ', end ="")
            
      print('')
      
#print('****************************')  
   
def show_icon_enlarged():
    times = 2
    for image in picture:
        for repeat in range(0,times):
            for pixel in image:
                if pixel == 0:
                    print(' '*times, end='')
                else:  
                    print('#'*times, end='')              
            print('\r')

print('\r')
print('\r')

def show_icon_inverted():
    for image in picture:
        for pixel in image:
            if pixel == 0:
                print('#', end='')
            else:  
                print(' ', end='')
        print('\r')

   
show_icon()
show_icon_enlarged()
show_icon_inverted()