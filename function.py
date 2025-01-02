#FUNCTIONS
'''
function is indented block of code which is used to perform the specific task in the program
define once and call any no. of times
code resuability

2types of functions
pre-defined function::they are inbuilt in py library/software ex::print,input,sqrt etc
user-defined function:: define in our program as per requirement
'''
#exp1
'''
def a():
    print('hello')
    print('welcome')
    print('bye')
a()
print()
print('again show the values')
a()
'''
#function with parameter args
#EXP1
'''
def a(name):
    print('hello::',name)
    print('bye::',name)

obj=a('Abhishek Naik')
print()
a('AAB')
'''
#function with multiple return values
# exp1
#difference between return and print is while using print again we won't print the values..
# while using the return values we need to print the values otherwise we wont get the values
#exp1
'''
def sum(a,b):
    c=a+b
    return c
result=sum(4,6)
print(result)

def sum(x,y):
    p=x+y
    print('the value of x and y is::',p)

o=sum(55,44)
'''
#TYPES OF FUNCTION ARGUMENTS 4
'''
1] POSITIONAL ARUGUMENT
2] KEYWORD ARGUMENT
3] DEFAULT ARGUMENT
4]VARIABLE LENGTH ARGUMENT
'''
# POSTIONAL ARGUMENTS:: based on the input of positional args the output changes 
# exp1
'''
def sub(a,b):
    c=a-b
    return c
x=22
y=11

result=sub(5,3)
print(result)

print()
print(sub(x,y))
'''
# KEYWORD ARGUMENTS::means input  parameters names:: if order changes also we get the correct output
# exp1
'''
def user(name,password):
    return('The name::',name,'\n','The password::',password)

result=user('Abhishek Naik','@4dgw7')
print(result)

result2=user(password='@54fgge',name='Abhi')
print(result2)
'''
# DEFAULT ARGUMENTS:: means here it takes default values when we pass less or  no  input arguments 
'''
def values(a=2,b=44,c=55):
    return('The sum of  a,b,c is::',a+b+c)

result=values(100,200,300)
print(result)

rs=values()
print(rs)
'''
# VARIABLE LENGTH ARGUMENTS:: means here we can pass zero or one or  more values
#exp1
'''
def adding_sum(*args):
    return sum(args)

result=adding_sum(55)
print(result)

result2=adding_sum(44,55)
print(result2)

result3=adding_sum(404,403)
print(result3)
'''
# SPECIAL CASE VARIABLE LENGTH ARGUMENTS :: VARIABLES NAME IT IS DICT KEY VALUE PAIR
# exp1
'''
def a(**nums):
    return nums
result=a(d=1,b=2,c=3)
print(result)

print('rollno=101','name=ASd','Course=Degree')
'''
# FUNCTIONS TYPES OF VARIABLES
'''
1] GLOBAL VARAIBLE::DEFINE OUTSIDE A FUNC:: FULL ACCESS IN ALL FUNC IN PROGRAM
2] LOCAL VARIABLE:: DEFINE INSIDE A FUNC:: ONLY LOCAL ACCESS INSIDE A FUNC
'''
#EXP1
'''
a=20
def aa():
    print(a)
def c():
    print(a)
aa()
c()
'''
#exp2
'''
y=100
def yy():
    return y
def d():
    return y

result=yy()
print(result)

result2=d()
print(result2)
'''
#LOCAL VARIABLE
'''
def nam():
    a=20
    print(a)
def  nam2():
    b=202
    #print(a)
    print(b)
nam()
nam2()
'''
#BOTH LOCAL AND GLOBAL VARIABLES ::1st preferance will be given to local variables
'''
a=200
def global_var():
    a=10
    print(a)
def local_var():
    print(a)
global_var()
local_var()
'''
#LAMBDA FUNCTION
'''
LAMBDA KEYWORD IS USED 
USES::THESE ARE INSTANTLY USED FUNCTION
NO DEF RETURN KEYWORD
'''
#exp 
'''
def nam(x):
    return x*x
print(nam(4))
'''
#using lambda
#exp2
'''
A=lambda x:x*x
print(A(10))
'''
#exp:1
'''
C=lambda e,d:e+d
print(C(45,65))
'''
# function as object
'''
in py everything is obj
function is also obj
'''


#every function is object
#exp 1
'''
def a():
    print('hello')
a()
print(a)
print(id(a))
'''

















































































