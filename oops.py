# OOPS:: OBJECT OREIENTED PROGRAMMING 
'''
IT IS NOT A NEW PROGRAMMING 
IT IS NOT SEPRATE PROGRAMMING
IT IS BASED ON THE REAL LIFE COMPUTER PROGRAMS
OOPS PRINCIPLES
1]ABSTRACTION
2]ENCAPSULATION 
3]INHERITANCE
4]POLYMORPHISM
'''

#ENCAPSULATION
'''
CLASS AND OBJECTS
IT SAYS EVERY PRODUCT(OBJECT) HAS TWO THINGS 
1] DATA HAS INPUT
2] FUNCTIONALITY HAS OUTPUT
EX:: MARKER PEN
DATA HAS INPUT
INK COLOR 
INK QUANTITY
FUNCTIONALITY AS USAGE(OUTPUT)
WRITING ON THE WHITE BOARD
IN PY WE DO ENCAPLUSTION WITH THE CLASS AND OBJECTS
CLASS::CLASS IS THE BLUE PRINT TO CREATE OBJECTS
OBJECT:: ANYTHING THAT HAS STATE AND BEHAVIOUR IS CALLED OBJECT
CLASS IS NOTHING BUT MODEL
OBJECT IS  NOTHING BUT END PRODUCT

# VARIABLES ARE 3TYPES 
1]INSTANCE
2]STATIC
3]LOCAL
#METHODS ARE 3TYPES
1] INSTANCE
2] STATIC
3]CLASS

'''
'''
#ex1
class car:
    def __init__(self,modelname,year,month):
        self.modelname=modelname
        self.year=year
        self.month=month
    def display(self):
        print(self.modelname,self.year,self.month)
c1=car('Honda','2000','August')        
c1.display()

#exp2

class student:
    def __init__(self):
        self.name="Boda Abhishek Naik"
        self.roll_no="200"
        self.clg="jnr"
    def display(self):
        print(self.name)
        print(self.roll_no)
        print(self.clg)
s1=student()        
s1.display()

#exp3

class notesbooks:
    def __init__(self):
        telugu=int(input('enter the telugu pages::'))
        hindi=int(input('enter the hindi pages::'))
        english=int(input('enter the english pages'))
    def display(self):
        print('here the telugu book::',self.telugu)
        print('here the hindi book::',self.hindi)
        print('here the english pages::',self.english)
books=notesbooks()
books.display()
'''

#CONSTRUCTOR
'''
IT IS SPECIAL METHOD IN A CLASS 
IT'S NAME IS --INIT--(SELF)
IT IS EXECUTED AUTOMATICALLY WHEN THE OBJECTS IS CREATED 
IT'S MAIN PURPOUSE IS DECLARE AND INITIALIZE
IT IS  EXECUTED ONLY ONCE PER OBJECT
IT IS OPTIONAL IN THE CLASS,IF IT NOT PROVIDED ,PYTHON PROVIDES DEFAULT CONSTRUCTOR

'''
#exp1:
'''
class student:
    def __init__(self,r,n,wt):
        self.rollno=r
        self.name=n
        self.weight=wt
    def display(self):
        print(self.rollno,'\n',self.name,'\n',self.weight) 
s1=student('22','Abhsihek','56')
s1.display()
print()
print('details of the student2')
s2=student('23','San','55')
s2.display()
'''
#DIFFERANCE BETWEEN CONSTRUCTORS AND METHODS OF A CLASS
'''
constructor name is fixed name --init--()
method can be any user defined name
2]
constructor is called and executed automatically when the object is created
method is called manully  and executed 
3]
constructor is called only once per object
method can be called and executed any no of times per object 

4]
constructor is used to declare and initialize instance variables
method is used to writing logics in a class

'''
#TYPES OF VARIABLES IN PY CLASS
'''
INSTANCE VARIABLE::SEPRATOR FOR EVERY OBJECT
STATIC VARIABLE::COMMON FOR ALL OBJECTS
LOCAL VARIABLES:: DEFINE INSIDE A CLASS METHOD ONLY
CLASS VARIABLES:: INSIDE CLASS METHODS
'''
#INSTANCE VARIABLES
'''
INSTANCE MEANS OBJECT
SEPRATE COPY FOR EVERY OBJECT
DEFINE THEM INSIDE CONSTRUCTOR WITH SELF VARIABLES
'''
# STATIC VARIABLES
'''
COMMON VARIABLES 
FOR ALL OBJECTS ONLY ONE COPY IN THE MEMORY
DEFINE DIRECTLY INSIDE A CLASS (WITHOUT CONSTRUCOR WITHOUT METHOD )

note::ANY CHANGES DONE IT IS UPDATED TO ALL THE OBJECTS
ANY CHANGES DONE TO INSTANCE VARIABLES,IT IS UPDATED TO PARTICULAR OBJECT
'''

#EXP1
'''
class stasticvar:
    e='welcome'
    def __init__(self):
        self.x=20
        self.y=30
    def display(self):
        print(self.x,self.y,self.e)

a=stasticvar()
a.display()
print()
print('another object')

b=stasticvar()
b.e='hello world'
b.display()
print()
print('object no3')

c=stasticvar()
c.x=200
c.y=300
c.e='Sucessfully modified the values'
c.display()
'''
#LOCAL VARIABLES
'''
defined inside a particular class
also called method variables
they can acces inside a method only 
'''
#exp1
'''
class local_variables:
    def m1(self):
        print('inside the m1 of the class')
        x=10
        print(x)
        
    def m2(self):
        print('inside m2 of the class')
        y=20
        print(y)
 #       print(x)   (Name Error)

a=local_variables()
a.m1()
a.m2()
'''
#TYPES OF METHODS IN THE PYTHON CLASSES
'''
3types of the methods
1] instance methods(object methods)
2]static methods (common methods)
3] class methods(sepecial methods with class var)
'''
#instance methods
'''
instance means object methods 
methods whose functionality (work)is different/separate for every object are called instance methods
for instance methods we pass self variable as it's 1st para

'''
#exp1
'''
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        for m in self.marks:
            sum=0
            sum+=m
            print(self.name,'\n',self.marks,'the avg marks::',sum/3)
s1=student('Abhishek',[22,33,44])
s1.get_avg()
'''
#exp2
'''
class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print(self.name)
        print(self.roll_no)
        print(self.marks)
    def grades(self):
        if self.marks >=75:
            print('congratulations A+ grade:')
        elif self.marks >=65:
            print('congratulations A grade:')
        elif self.marks >=45:
            print('Well try D grade')
        else:
            print('Better luck next time :)::')

s1=student('Abhishek',2,3)
s1.display()
s1.grades()
print()
print('student number2')

s2=student('Abhi',4,75)
s2.display()
s2.grades()
'''
#STATIC METHODS 
'''
they are general common methods 
they have common functionality for all objects
no self variables (input parameteres) required
use @staticmethod decorator (before the method definition)
here no need to pass self parameter as input 
'''
#Exple:1 and exp:2 are correcct
'''
class staticmethod_aa:
    
    def sum(x,y):
        print('Addition of the x and y is::',x+y)
    
    def sub(x,y):
        print('Substraction of x and y is::',x-y)
    
    def mult(x,y):
        print('Multiplication of x and y is::',x*y)
    
    def divi(x,y):
        print('Division of x and y is::',x/y)

staticmethod_aa.sum(29,3)
staticmethod_aa.sub(23,444)
staticmethod_aa.mult(83,398)
staticmethod_aa.divi(33783,883)
'''
#try this it the type error code
'''
a=staticmethod_aa(20,5)
a=staticmethod_aa(67,3)
a=staticmethod_aa(689,9708)
a=staticmethod_aa(46,97)
a.sum()
a.sub()
a.mult()
a.divi()
these is type error code 

'''
#exple1 and 2 are correct
'''
class staticmethod_aa:
    @staticmethod
    def sum(x,y):
        print('Addition of the x and y is::',x+y)
    @staticmethod
    def sub(x,y):
        print('Substraction of x and y is::',x-y)
    @staticmethod
    def mult(x,y):
        print('Multiplication of x and y is::',x*y)
    @staticmethod
    def divi(x,y):
        print('Division of x and y is::',x/y)

staticmethod_aa.sum(29,3)
staticmethod_aa.sub(23,444)
staticmethod_aa.mult(83,398)
staticmethod_aa.divi(33783,883)
print()
print('with different method')
obj=staticmethod_aa()
obj.divi(23,45)
'''
#CLASS METHOD
'''
we use @classmethod decorator
no self input parameter
class variables used to create objects and access instant constant
class variable used to access static content
'''

#ex1
'''
class classmethods:
    c=112
    def __init__(self):
        self.x=10
        self.y=20

    
    def show():
        print('static show::')

    def show2():
        print('instant method x,and y::',self.x,self.y)

    @classmethod
    def show3(classvar):
        print('static var','classmethod',classmethods.c,classvar.c)
        classmethods.show()
        classvar.show()
a=classmethods
a.show3()
'''
#PASSING OBJECT OF ONE CLASS TO ANOTHER CLASS
'''
PASSING OBJECT AS PARAMETER TO METHOD
WE CAN PASS OBJECT OF ONE CLASS TO ANOTHER CLASSS AND ACCESS ITS MEMBERS IN ANOTHER CLASS USING OBJECT AS PARAMETER TO METHOD
ADVANTAGE IS REUSABILITY OF CODE
RE USE ONE CLASS MEMBERS IN ANOTHER CLASS
'''
#explame:2,the height will be updated 
'''
class student:
    def __init__(self,name,height,age):
        self.name=name
        self.height=height
        self.age=age
    def display(self):
        print(self.name,self.age,self.height)

class demo:
    @staticmethod   #without these also we can write code
    def update(s2):
        s2.height+=0.5
        s2.display()

        s2.age-=47
        s2.display()

s1=student('ak',5.6,66)
s1.display()

demo.update(s1)
'''
#INNER CLASS IN PYTHON
'''
DEFINING ONE CLASS INSIDE ANOTHER IS CALLED AS INNER CLASS[CLASS WITHIN CLASS]
INNER CLASS ARE PART OF OUTER CLASS
HENCE INNER CLASS OBJ IS CREATED USING OUTER CLASS OBJECT

'''

'''
class outer:
    def __init__(self):
        print('outer class!..')
    class inner:
        def __init__(self):
            print('inner class!..')
        def m1(self):
            print('inner m1 method!..')

#case:1
out=outer()
inn=out.inner()
print()
#case2
print('another case....')
inn2=outer().inner()
inn2.m1()

print()
print('&&& another case3 &&&')
#case3
outer().inner().m1()
'''
#INHERTANCE (IS A RELATIONSHIP)
'''
GETTING DATA PROPERTIES(VARIABLES),METHODS AND CONSTRUCTOR FROM PARENT CLASS TO CHILD CLASS IS CALLED INHERITANCE
HENCE PARENT CLASS MEMBERS ARE RE-USED IN THE CHILD CLASS
CHILD CLASS EXTENDS PARENTS CLASS FUNCTIONALITY
CHILD CLASS IS MORE POWERFUL THAN PARENT CLASS FUNCTIONALITY
ADVANTAGE IS REUSEABILITY OF THE CODE WITHOUT PARENT CLASS OBJECTS
'''

#exp1
'''
class p:
    a=10
    def __init__(self):
        self.b=30
    def m1(clsvar):
        print('parent class inhertance m1...')
    def m2(self):
        print('parent class inheritance m2......')
class c(p):
    pass

cobj=c()
print(cobj.a)
print(cobj.b)
print()
print('parent class;;;')
pa=p()
print(pa.a)
print(pa.b)
'''
#case2
'''
class parent:
    def m1(self):
        print('parent class m1()...')
class child(parent):
    def m2(self):
        print('child class...')
    
obj=child()    
obj.m2()
obj.m1()
'''

#super.--init-- it indictes 1st parent class constructor later child class .if you wont write the super.--init-- the parent class constructor
# wont appear
#case3
'''

class pclass:
    def __init__(self):
        self.x=20
  m1(self):
        print('parent class m1 methpd::',self.x,self.y)
class cclass(pclass):
    def __init__(self):
       super().__init__()
       self.p=200
       self.q=300
    def m2(self):
        print('child class::',self.p,self.q)

obj=cclass()
obj.m2()
obj.m1()
'''
#parent class child class constructors
'''
special cases inheritance
whenever we are creating child class objects then child class constructor is executed 
if there is no child class constructor then parent class constructor is executed auto

from the child class constructor,we can reuse parent class constructor using super()function
super()::it is special function
it is used in child class only(inhertance concept)
using super() we can reuse parent class members in child class

'''
#TYPES OF INHERITANCE 
'''
python has 5types of iheritance they are 
1]single inheritance
2] multi-level inheritance
3]heirarchical inheritance
4]multliple inheritance
5] hybrid inheritance

'''
#SINGLE INHERITANCE
'''
single parent class giving derivation to single child class
'''
'''
class A:
    def __init__(self):
        self.a='hello'
        self.b='welcome'
    def m1(self):
        print('parent class A in m1()..',self.a,self.b)
class B(A):
    def __init__(self):
        super().__init__()
        self.p='hello di'
        self.q='child'
    def m2(self):
        print('this is child class',self.p,self.q)
obj=B()
obj.m2()
obj.m1()
'''
#MULTI-LEVEL INHERITANCE
'''
IN THIS IT IS EXTENSION OF SINGLE INHERITANCE IN WHICH CHILD CLASS ACTS A PARENT CLASS FOR NEXT DERIVATION (NEXT CHILD CLASS)
'''
#exp 1
'''
class pclass:
    def __init__(self):
        self.a=20
        self.b=30
    def m1(self):
        print('this parent class::',self.a,self.b)
class cclass(pclass):
    def __init__(self):
        super().__init__()
        self.c='the value of a is 20:'
        self.d='the value of d is 30:'
    def m2(self):
        print('this is child class::',self.d,self.c)
class subclass(cclass):
    def __init__(self):
        super().__init__()
        self.e='this is subclass of e::'
        self.f='this is subclass of f::'
    def m3(self):
        print('this is subclass of m3::',self.e,self.f)

obj=subclass()
obj.m1()
obj.m2()
obj.m3()
'''
#HIERARCHICAL INHERITANCE
'''
in this single parent class gives derivation to multiple child classes
'''
#exp1
'''

class A:
    def __init__(self):
        self.a='This is parent class a::30'
        self.b='This is parent class b::300'
    def m1(self):
        print('This is parent class of A::',self.a,self.b)
class B(A):
    def __init__(self):
        super().__init__()
        self.c='This is child class::hello'
        self.d='This is child class::welcome'
    def m2(self):
        print('This is child class::',self.c,self.d)
class C(A):
    def __init__(self):
        super().__init__()
        self.e='This subchild::all ok'
        self.f='This is 2nd child::all fine'
    def m3(self):
        print('This is 2nd child of parent class::',self.e,self.f)
obj=C()
obj.m3()
obj.m1()
print('...The end...')
print()

obj2=B()
obj2.m2()
obj2.m1()
'''
#multiple inheritance
'''
in this multiple parent classes gives derivation to single child class
here 1st priority is given to 1st parent only
whenever we have same method name in multiple parent classes it takes only 1st parent method but not 2nd parent method
'''
#exp1
'''
class A_parent:
    def __init__(self):
        self.a=300
        self.b=600
    def m1(self):
        print('This parent class::',self.a,self.b)
class B_parent:
    def __init__(self):
        self.x=2
        self.y=3
    def m2(self):
        print('This is parent class of B::',self.y,'\n',self.x)
class C(B_parent,A_parent):
    def __init__(self):
        super().__init__()
        self.o='Congrats'
        self.s='Well done'
    def m3(self):
        print('This is child class::',self.o,'\n',self.s)
obj=C()
obj.m3()
obj.m1() #this comes error because in child class first priority is given to B_parent so..
obj.m2()
'''
#HYBRID INHERITANCE
'''
this is the combination of two or more single,multiple,hirarchical,multiple,inheritance
'''
#POLYMORPHISM
'''
POLY MEANS MANY 
MORPHISM MEANS FORMS
SINGLE OBJECT IN MULTIPLE FORMS BASED ON THE SOME CONDITIONS
IN PYTHON WE DO POLYMORPHISM DO IN THREE WAYS
1]DUCK TYPING 
2]OVERLODING ::3WAYS OPERATOR,METHOD,CONSTRUCTOR
3]OVERRIDING ::2WAYS METHOD ,CONSTRUCTOR
'''
#DUCK TYPING 
'''
here we decide method input parameter data type at runtime
in py we have dynamic typed language
'''
#exp1:; here we can access the code directly by using the function and create a function and call it 
'''

class student:
    def display(self):
        print('Details of the Student::')
class coustomer:
    def display(self):
        print('Details of the coustomer')
class employee:
    def display(self):
        print('Details of the employee')
def m1(obj):
    obj.display()

s1=student()
c1=coustomer()
e1=employee()
m1(s1)
m1(c1)
m1(e1)
'''
#OVERLOADING IN POLYMORPHISM
'''
it is done in three ways 
1] operator overloading 2] method overloading 3] constructor overloading 
'''
#operator overloading 
'''
single operator multiple behavior/purpose
performing operations in class is  not possible directly ex::b1+b2
however we can make it possible with operation overloading magic methods ex:def --add--(self,other) 
'''
#exp1
'''
class book:
    def __init__(self,pages):
        self.pages=pages
    def diplay(self):
        print('The pages of the book is::',self.pages)
b1=book(200)
b1.diplay()

b2=book(300)
b2.diplay()

#print(b1+b2)

b3=book(b1.pages+b2.pages)
b3.diplay()
'''
#WITH MAGIC METHODS::__add__(self,other),__sub__(self,other)
'''
magic methods are pre defined methods with operator overloading objects
'''
'''
class book:
    def __init__(self,pages):
        self.pages=pages 
    def display(self):
        print('The total pages of the book is::',self.pages)
    def __add__(self,other):
        return('addition::',self.pages+other.pages)  #or we can print also
b1=book(200)
b1.display()

b2=book(3000)
b2.display()

b3=b1+b2
print('the end..')
print(b1+b2)
'''
#exp2
'''
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return(self.marks>other.marks)
    def __le__(self,other):
        return(self.marks<=other.marks)

s1=student('and',29)
s2=student('or',84)
print(s1>s2)
print(s1<s2)
print(s1==s2)
print(s2!=s1)
'''
# METHOD OVERLOADING
'''
same method and multiple usages
2 or more methods with same name in same class but atleast 1difference in method signature
no.of args
order of args
dtype of args

note:: but in python method overloading is not possible
trying to declare mutliple methods with same name and differnt in method signature then python takes only 1st method 
into consideration
method signature means no of args ,order of args, dtype of args

however we perform method overloading indirectly in two ways
1] method with default args
2] method with variable length arguments
'''
#method with default args 
#general case not possible
#exp
'''
class demo:
    def m1(self):
        print('0 arguments m1()..')
    def m2(self):
        print('1 arguments m2()...')
    def m3(self):
        print('3 arguments m3().....')

obj=demo()
obj.m1(2)
obj.m2(2,3)
obj.m3(4,4,5)
'''
#case 1 with default args
'''
class demo:
    def sum(self,a=2,b=33,c=55):
        result=a+b+c
        print('the sum of ::',result)
obj=demo()
obj.sum(33,44,55)
obj.sum(99,77,66)
obj.sum()
'''
# case 2 method with variable len(no) of args
'''
class demo:
    def sum(self,*nums):
        print('sum ::',sum(nums))
obj=demo()
obj.sum(39,1)
obj.sum(300,400,700)
obj.sum()
'''
#CONSTRUCTOR OVERLOADING 
'''
it is also not possible in python
2 or more mutliple constructors with same name in same class but atleast 1 diffference in constructor signature

however we can do indirectly in 2 ways
1]constructor with default args
2] consturctor with variable length args
'''
'''
class demo:
    def __init__(self):
        print('0 args constructor..')
    def __init__(self, x):
        print('1 args constructor::',x)
    def __init__(self, x,y):
        print('2 args constructor',x,y)
obj=demo()
obj2=demo(2,3)
obj3=demo(3)
'''
#case1
# constructor with default args 
'''
class demo:
    def __init__(self,*nums):
        print('1 args constructor..',sum(nums))
obj=demo()
obj=demo(2,3,4)
obj=demo(3)
'''
#overriding in python polymorphism
'''
related to inheritance pc and cc
it is done in two ways
1] method overriding
2] constructor overriding
'''
'''
1] method overriding::
this concept is related to inheritance  
parent class members are available to child class
re defining parent class methods in child class with same name and same signature is called method overriding
(here no args,dtype of args,order of args are same)
hence always child class methods are methods are more powerful than parent class methods 

'''
#exp
'''
class pclass:
    def m1(self):
        print('parent class method')
class cclass(pclass):
    def m1(self):
        super().m1()
        print('child class')
obj=cclass()
obj.m1()
'''
#exp2
'''
class pclass:
    def __init__(self):
        print('parent class constructor')
class cclass(pclass):
    def __init__(self):
        super().__init__()
        print('child class constructor')

obj=cclass()
'''
#Abstraction
'''
HIDING UNCESSARY THINGS IN AN OBJECT AND EXPOSING ONLY NECCESSARY THINGS OUTSIDE THE OBJECT
EX::
MARKER PEN
HIDE(INK,REFILL)
EXPOSE(BODY,CAP,NIB)
IN PYTHON ABSTRACTION IS DONE IN TWO WAYS
1]ABSTRACT CLASSES (WITH ABSTRACT METHOD)
2] INTERFACES (WITH ABSTRACT METHODS)
'''
#1]ABSTRACT CLASSES WITH ABSTRACT METHODS
'''
THESE METHODS ARE USED INSIDE A CLASS
COMPLETE METHODS:: AMETHOD WITH BODY IS CALLED COMPLETE METHOD
ABSTRACT METHOD:: A METHOD WITHOUT BODY(INCOMPLETE METHOD)(PASS)
FOR THESE METHODS WE USE @ABSTRACTMETHODS DECORATORS(COMPULSARY)
@ABSTRACTMETHOD IS ABC MODULE TO USE THESE FIRST WRITE FROM ABC IMPORT*

'''
#ABSTRACT CLASS(COMPLETE CLASS)
'''
A CLASS WITH ATLEAST ONE ABSTRACT METHOD IS CALLED ABSTRACT CLASS
SUCH CLASS INHERITED FROM ABC PARENT CLASS
HERE WE CANNOT CREATE OBJECT OF ABSTRACT CLASSES (ERROR)..REASON::INCOMPLETE CLASS
'''
#exp 1:
'''
from abc import *
class A(ABC):
    @abstractmethod
    def m1(self):
        print('hello') # or  pass by the @bstractmethod we can get the values of child class ex:
                        #when we use @bstractmethod we have same m1 in parent and child then to get the value of child only use this.

    def m2(self):
        print('this is parent class..')

class B(A):
    def m1(self):
        print('this is known as the child class with the same name in the parent class')

    def m3(self):
        print('the child class')

obj=B()
obj.m1()
obj.m2()
obj.m3()
'''










































































































































































































































































































































































































