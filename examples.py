# WRITE A PROGRAM TO ADD TWO NUMBERS IN PYTHON
'''
num=eval(input('Enter a number1::'))
num2=eval(input('enter a number2::'))
a=num+num2
print('sum of two number is::',a)
'''
#WRITE A PROGRAM TO PRINT HELLO WORLD
'''
print('hello world')
'''
#WRITE A PYTHON PROGRAM TO FIND THE SQUARE ROOT
'''
num=eval(input('enter the Squareroot number::'))
#s=num**1/2
s=num**0.5
print('square root of number is::',s)
'''
'''
import math
num=eval(input('Enter the number::'))
s=math.sqrt(num)
print('the square root::',s)
'''
#WRITE A PROGRAM TO CALCULATE THE AREA OF A TRIANGLE
'''
ht=eval(input('Enter the height  of triangle::'))
base=eval(input('Enter the base of triangle::'))
area=(0.5*base*ht)
print('the area of  triangle is::',area)
'''
#WRITE A PROGRAM TO SWAP TO SWAP TWO VARIABLES
'''
a=int(input('Enter a number1::'))
b=int(input('Enter a number2::'))
a,b=b,a
print('the value of a is::',a)
print('the value of b::',b)
'''
#WRITE A PROGRAM TO CHECK IF A NUMBER IS POSITIVE ,NEGATIVE OR ZERO
'''
num=int(input('Enter the number1::'))
if num>0:
    print('number is positive::',num)
elif num==0:
    print('The number given is  zero::',num)
else:
    print('The  number is negative::',num)
'''
#WRITE A PROGRAM TO CHECK IF A NUMBER IS EVEN OR ODD
'''
num=int(input('Enter the number1::'))
if num%2==0:
    print('The given number is even::',num)
else:
    print('The  given number is odd::',num)
'''
#WRITE A PROGRAM TO CHECK LEAP YEAR
'''
year=int(input('Enter the year::'))

if year%400==0 and year%100==0:
    print('It is a leap year')
elif  year%4==0 and year% 100!=0:
    print('it is a leap year')
else:
    print('It is not a leap year')
'''
#WRITE A PROGRAM TO FIND THE LARGEST AMONG THREE NUMBERS
'''
num1=int(input('Enter a number1::'))
num2=int(input('Enter a number2::'))
num3=int(input('Enter a number3::'))

if num1>num2 and num1>num3:
    print(num1,'::The largest number is num1')
elif num2>num3 and num2>num3:
    print(num2,'::The largest number is num2')
else:
    print(num3,'::The  largest number is num3')
'''
#WRITE A PYTHON PROGRAM TO CHECK PRIME NUMBER
'''
num=int(input('Enter a number hereL::'))

if  num==1:
    print('It is not a prime number')
if num>1:
    for  i in range(2,num):
        if num%i==0:
            print('It is not a prime number')
            break
        else:
            print('It is a prime number')
            break
'''
#WRITE A PROGRAM TO GENERATE A RANDOM NUMBER
'''
import random 
num=random.randint(0,200)
print('the random number is::',num)
'''
#WRITE A PROGRAM TO PRINT ALL  THE PRIME NUMBERS IN AN INTERVAL
'''
lower=int(input('enter a number lower::'))
upper=int(input('enter a number is upper::'))

for num in range (lower,upper+1):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                print(num,'::the prime numbers ')
                break
'''
#WRITE A PYTHON PROGRAM TO PRINT A MULTIPLICATION TABLE 7X1=7
'''
num=int(input('enter a number:'))
for i in range(1,11):
    print(num,'X',i,'=',num*i)
'''

#WRITE A PYTHON PROGRAM THE SUM OF NATURAL NUMBER 
'''
num=eval(input('Enter a number::'))
if num<0:
    print('please enter a positive number')
else:
    sum=0
    while num>0:
        sum+=num
        num-=1
        print(sum)

'''
##WRITE A PYTHON PROGRAM TO PRINT OUTPUT WITHOUT A NEWLINE
'''
print('hello welcome to ',end='')
print('python basic program')
'''
#WRITE A PYTHON PROGRAM TO GET A SUBSTRING OF A STRING
'''

a='hello this coding language of python'
c=a[-9:-7]
print(c)
'''
































































