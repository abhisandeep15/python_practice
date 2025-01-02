#WHAT IS REGEX IN THE PYTHON
'''
it stands for regular expressions
special search pattern to find and maniplate text
regex also can split into one or more sub patterns 

import re used to import the regex module

'''
#META CHARACTERS
'''
\  :: used to drop the special meaning of character following it

[] :: represent a character class

^ :: matches the beginning

$ ::matches the end

. ::matches any characters expect newline

| ::means ex:if we have the two conditions then it should satisfies one condition

? ::matches zero or one occurence

* ::matches any number of occurences 0 more than that

+ :: one or more occurences

{} ::indicate the number of occurences of a preceding regex to match

() ::enclose a group of regex

'''
#Exp1
'''
import re 
a= 'py is a coding language supports the low level language and the high level language and'
b='abhisheknaik24853@gmail.com'
c='hello'
d='xyz,xy,zxy,yzx,aa,yzx,xzy,ccx,xyb,xyz,zzy,xyz,xyyzz,xxyyzz'

match=re.search(r"\.",b)
print(match)

matches2=re.search(r'[i]',b)
print(matches2)

match=re.findall(r"[l]",a)
print(match)

match=re.search(r"^b",b)
print(match)

match=re.search(r"^abh",b)
print(match)

match=re.search(r"e$",a)
print(match)

match=re.search(r'l.a$',a)
print(match)

match=re.findall(r"lang|th",a)
print(match)


match=re.findall(r"the?",a)
print(match)

match=re.search(r"and*",a)
print(match)


match=re.search(r"xy+z",d)
print(match)

match=re.search(r"x{2,6}",d)
print(match)

match=re.findall(r"(x|y)yz",d)
print(match)
'''
#SPECIAL SEQUENCE IN REGEX
'''
SPECIAL SEQUENCE DO NOT MATCH FOR  THE ACTUAL CHARACTER IN THE STRING IT TELLS THE SPECIFIC LOCATION IN THE SEARCH STRING
 WHERE THE MATCH MUST  OCCUR
IT MAKES IT EASIER TO WRITE COMMONLY USED PATTERNS

\A :: Matches at the begining of the string

\b ::checks begining and ending charcters \b

\B :: It is opposite to \b

\d ::matches [0-9]

\D ::matches non-digits characters

\s ::matches any whitespace character

\S ::matches any non-whitespace characters

\w ::matches[a-z,A-Z,0-9]

\W :: matches any non-alphanumeric charcters

\Z ::matches if the string ends with the given regex

'''
#exp2
'''
a='Harry potter'
b='&abhishek15 #naik@23'

import re

match=re.search(r'\AHar',a)
print(match)

match=re.search(r'\AH',a)
print(match)

match=re.search(r'\bH',a)
print(match)

match=re.search(r'\Ba',a)
print(match)

match=re.search(r'Ha\B',a)
print(match)

match=re.findall(r'\d',b)
print(match)

match=re.findall(r'\D',b)
print(match)

match=re.findall(r'\s',b)
print(match)

match=re.findall(r'\S',b)
print(match)

match=re.findall(r'\w',b)
print(match)

match=re.findall(r'\W',b)
print(match)

match=re.search(r'23\Z',b)
print(match)
'''
#REGEX SETS
'''
A SET IS A A SET OF CHARACTERS INSIDE A PAIR OF SQUARE BRACKETS[] WITH A SPECIAL MEANING

[atx] :: Returns a matches where [a,t,or x] are present

[a-h] :: Returns a matches lower case charcters between [a,h]

[^atx] :: Returns a matches for any characters except [a,t,and x]

[0123] :: Returns a match where any sprcified digits [0,1,2 or 3] are  present

[0-9]  :: Returns a match for any digit between 0-9

[0-7] [0-9] :: Returns a match for any two digit numbers from 00 and 79

[a-zA-Z] :: Returns a match for any charcters alphabetically between a-z and A-Z

[+]  :: ex:[#] means it give sonly #

'''

#exp1
'''
import re

a='This the Regular Expression'
b='Boda 123 Abhs34ishek na@gamil.com &#'

match=re.findall(r'[atx]',a)
print(match)

match=re.findall(r'[^atx]',a)
print(match)

match=re.findall(r'[a-t]',a)
print(match)

match=re.findall(r'[0123]',b)
print(match)

match=re.findall(r'[0-9]',b)
print(match)

match=re.findall(r'[0-7][0-9]',b)
print(match)

match=re.findall(r'[a-zA-Z]',b)
print(match)

match=re.findall(r'[@]',b)
print(match)
'''
#FUNCTIONS IN REGEX
'''
re.findall() :: returns all non overlapping matches of patterns in string as a list of strings .the string is
scanned left-right and matches are returned in the order found

re.compile() :: regular expressions are compiled into pattern objects which have methods for various operations such as searching for pattern
matches or performing string substitutions

re.spilt()  :: spilt string by the occurences of a characters or a characters or a pattern, upon finding that pattern,
the reaming characters from the string are returned as part of the resulting list

re.sub()  :: the method returns a string where matched occurences are replaced with the content of replace variable

re.subn()  :: subn() is similar to sub() in all ways ,expect in its way of providing output .it returns a tuple with  a count of 
the total of replacement and the new string rather than just string

re.escape()  :: returns string with all non alphanumerics backslashed ,this is useful if you want to match an arbitary literal string 
that may haave the expressions metacharacters in it

re.search() ::this method either returns none [if the pattern doesnt match],or a re. this method stops after the first match,
so this is best suited for testing a reular expressions more than extracting data

'''
#exp1
'''
import re

text="""
    JHON has scored 58 marks
    Lisa has scored 89 marks
    david has scored 84 marks
    """

#print(re.findall(r'\d',text))
#print(re.findall(r'\d+',text))
#print(re.findall(r'[a-zA-Z]*',text))

p=re.compile('[a-d]')
print(re.findall(p,text))

p=re.compile('[0-9]')
print(re.findall(p,text))

p=re.compile('[\d+]')
print(re.findall(p,text))
             
print(re.split('\d+',text))

print(re.subn('\S+','',text))
print(re.sub('\S+','@@',text))

print(re.escape(text))
print(re.search('\d+',text))
'''
#MATCH OBJECT IN REGEX
'''
a match object contains all the information about the search and the result and if there is no match found then none will be returned

'''
#exp1
'''
import re

a='Jhon has scored 89 marks'

match=re.search('\d+',a)
print(match)
print(match.re)
print(match.string)
print(match.end())
print(match.start())
print(match.group())
'''

#PHONE NUMBER AND EMAIL VERIFICATION AND WEB SCRAPPING USING REGEX

import re

phone='763-357-3874'

phone = re.sub(r'[^0-9-]', '', phone)
if re.fullmatch(r'\d{3}-\d{3}-\d{4}', phone):
    print('It is the verified number:', phone)
else:
    print('Incorrect number format')


import re
email= 'abhishek2475@gmail.com abhi@gmai.com sandeep@gmail.com'

print(re.findall('[\w.-%][0-25]@[\w-].[A-Za-z]{2-3}',email))












































