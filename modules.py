'''
module means .py files[ module contains variables ,functions ,classes]
module is a library file
2types of modules files
1]predefined module::MEANS available in the py software ex:py,math,random.py etc..
2]userdefined module::means userdefined files

Example ::
creating  a module process
1]create a 2.py files example mod file and abhi file
2] write a code in abhi file
3]import the abhi in the mod file
4]run the mod file

note there are 4ways to import module 
1] import abhi [imports all we need to write a abhi]
2]alias name ::import abhi as abhi1[need to write abhi1. and remaining]
3]import specific function ::from abhi import add[no need to write module name]
4]import all function ::from abhi import *[no need to write module name]

'''


#module 1
'''
import abhimod1 

print(abhimod1.sum(2,4))
print(abhimod1.multiple(34,44))
'''

#module 2
'''
import abhimod1 as a

print(a.sum(23,34))
print(a.multiple(234,44))
'''

#module 3
'''
from abhimod1 import sum
print(sum(2200,34))
'''

#module 4
'''
from abhimod1 import *

print(sum(10,33))
print(multiple(334,5))
'''




































































































