'''print('hello wello to \n the python programing \t languge')

print("Boda Abhishek Naik"'\n'*10)

print('welcome to '+'Vscode ')'''

# py variables:: variables are used to stores the values 

# SEPARATOR 
'''
a='py', 'supports','low','level','and', 'high','level','language'
print(a,sep="*&")                                                     #output it wont changes 

print("py supports low level",end=" ,")
print("high level lang")

print('python' ,'is', 'the', 'programing lang',sep=" @ ")
'''
# String operator
'''
name="python"
print(name)
'''
# Accessing the string characters in python
'''
a="javascript is used for logical building in website"
print(a[2])
print(a[15])
print(a[3495])  #index error
print(a[-9])
print(a[-34])
print(a[2000])  #index error
'''
# py string is immutable  
'''
messages="welcome"
messages[3]='do'
print(messages)  #Type error
'''
# python multiline string
'''
h="""
 python is programming language
 sql is used for the database 
 html and css used in fronted 
"""
print(h)
'''
# Compare Two Strings
'''
str1="py,js"
str2="css,css"
str3='py,js'
print(str1==str2)
print(str2==str3)
print(str1==str3)
'''
# Join Two or more strings
'''
greet= "hello"
name="Abhi"
c=greet+name
print(c)

lang="javascript"
person="Jhon"
D=lang+person
print(D)
'''
# Iterate through a python string
'''
greet="hello boys"
for letter in greet:
    print(greet)
'''
# python string length
'''
greet="py is a programing lang"
print(len(greet))
c="javascript"
print(len(c))
'''

# String membership 
'''
a="hail the song"
print('a' in {a})
print('d' not in{a})
print('at' in{a})
print('hail' in {a})

print("a"in "python and")
print("cd" in "rx c100d 200a")
print("aa"in "dvd ab aa")
'''
# python string formatting
'''
a= " python"
b= "javascript"
print(f'there are different different programming languages example{a  }and the{  b}')

a='to welcome'
print(a.capitalize())
print(a.upper())
'''

# List in the python
#it is ordered 
# Allows duplicate
#  mutable
# Create a python list
'''
ages=[19,26,23,44,23,44]
print(ages)

languages=['python','sql','javascript','c++','c']
print(languages[2])
print(languages[-2])
print(languages[0])
print(languages[-9])   #index error : list index out of the range
'''
#Add elements to python list
'''
subjects=['Telugu','Hindi','English','Tamil','Malayalam']
print('orginal subjects:::',subjects)

#Using the append operator
subjects.append('Bengali')
print('Updated list::',subjects)
'''
#Change list items
'''
Colors=['Green','Rad','Blu','Viot']
print(Colors)
Colors[1]='Red'
Colors[2]='Blue'
Colors[3]='Violet'
print('Changed color list::',Colors)
'''
# Remove items from the list
'''
numbers=[2,4,5,6,8,9,10]
print(numbers)
numbers.remove(2)
numbers.remove(5)
print('Removed elements::',numbers)
'''
#python list length
'''
jobs=['IT','non-IT','Driving','Banking','Lawyer']
print(len(jobs))
print(jobs.len())   #Attribute error:: list objects has no attribute len
'''
# Iterators through the list
'''
name=input('Enter a name::')
for x in name:
    print('yes congrats')
    break
'''
#list constructor()
'''
thelist=list(('Apples','Cakes','Drinks'))
print(thelist)
print(type(thelist))
'''
#Set
# set stores multiple items in a single variable,types of datatypes are used to store the data types 1]list,2]set,3]Dictornay
#unordered,unchangeable,not allows duplicate items
'''
thisset={'apple','ball','cat'}
print(thisset)
print(type(thisset))

set_numbers={1,2,4,2,5,0,True,False}
print(set_numbers)
print(type(set_numbers))

a={'the set length',2,'and',3}
print(len(a))
print(type(a))
'''
#SET constructor
'''
thisset=set({'apple','Bat','Cat'})
print(thisset)
print(type(thisset))

b=set(3,4,3)
'''
b={2,4,5,6,}
c={12,45,6}
b.update(c)
print(b)
print(c)
c.update(b)
print(c)

























































































































































































