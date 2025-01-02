
#FILE I/O IN PYTHON [INPUT /OUTPUT] :: PYTHON CAN BE USED TO PERFORM OPERATIONS ON A FILE (READ,WRITEDATA)
# TYPES OF ALL FILES
'''
TWO TYPES OF FILES
1] TEXT FILES::TXT,DOC,LOG ETC..
2] BINARY FILES::MP4,MOV,PNG,JPEG ETC
'''
#TEXT FILEs
'''
stores data in the form of characters-data[strings]ex:hello
'''
#BINARY FILES
'''
STORES DATA IN THE FORM OF BINARY CODES[0,1]LINE EX:IMAGES, AUDIO,VIDEO,SETUP FIKES,ETC 
'''
#3STEPS FOR FILE STORING
'''
1] OPENING THE FILE
2] PERFORMING THE OPERATIONS ON THE FILE(WRITE,READ,APPEND)
3]CLOSE FILE
'''
#OPENING THE FILES IN THE PROGRAM
'''
FOR OPENING THE FILE WE USE THE FUNCTION OPEN()
SYNTAX:F1=OPEN(FILENAME,FILEMODE)
EX:F1=OOPEN['ABC.TXT','R']
'''
#FILE MODES[3TYPES]
'''
1]READ:[R]
OPENS A FILE FOR READ-MODE [READING PURPOSE]
IT IS DEFAULT MODE
INSIDE THE FILE,FILE PRINTER[CURSOR] IS PLACED AT BEGINNING
IF FILE IS NOT EXITS THEN WE GET 'FILE NOT FOUND' ERROR[EXCEPTION]

2]WRITE:[W]
opens a file for write mode[WRITING PURPOSE]
if files already exists there than it will over ride[***] the file
if file is not exists then it will be created

3]APPEND:[A]
opens an existing file for append mode {adding the data from the end of the file}
inside the file,FILE PRINTER[CURSOR] IS PLACED AT THE END OF THE FILE 
if the file is not exists then it will  create a new file
'''
#note:
'''
all modes are applicable for text files
add or suffix 'b' at end then it become binary files mode[use 'b' at end]
ex:rb,wb,ab
'''
#3 closing the file
'''
after completing file operations ,we close the file using close() function
Ex:f1.close()
'''
#file object properties[vars]
'''
in python everything is object,including file

once file is opened in program,we have to work  with files for read|write|append purpose
to work with file operations,we have different properties
1]name::name of the opened file Ex:f1.name
2]mode::mode in which file is opened
3]closed::checks for files open or closed [true/false]
4]readable::checks for file is readable or not [true/false]
5]writeable::checks for the file is writeable or not [true/false]
'''
#writing data of text files
'''
it is dom]ne with 2methods 
1]write[str]#writes given str data on file
2]write lines [list of lines]
#writes given list data as multi lines on files 

'''
#READING CHAR DATA FROM TEXT-FILES
'''
TO read char data from text files we use below methods  
1]read():reads total data at a time from a file
2]read(n): reads n chars from a file
3]readline(): Reads 1-line at a time
4] readlines():reads all lines at a time into a list
'''
#SPECIAL CASE OF OPEN()
'''
WITH STATEMENT TO OPEN A FILE
IT IS  HEAADER-STATEMENT TO OPEN A FILE
IT PROVIDES SUITES TO PERFORM DIFFERENT OPERATIONS ON A FILE
EX: WITH OPEN(FNAME,"W")AS F1:
WE CAN ALSO USE WITH STATEMENT TO OPEN THE FILE
ADVANTAGE IT CLOSES THE FILE AFTER ALL OPERATIONS ARE DONE ,EVEN IF EXCEPTIONS OCCURS NOT NEED TO CLOSE EXPLICITLY
'''

#CHECKING FOR FILE EXISTS OR NOT 
'''
FOR THIS WE CAN USE AS LIBRARY TO GET INFO ABOUT FILES IN OUR COMPUTER
'OS' MODULE HAS PATH SUB-MODULE IT CONTAINS ISFILE(),USING WHICH WE CAN CHECK FILE EXISTS OR NOT
'''
#WORKING WITH THE OS DIRECTORIES/FOLDERS
'''
some common operations on directoroies are [folders]
a] current working directoy
b]create new directory
c] remove existing directory
d] rename a directory
e] list contents of directory etc
*for this we use 'os' module to perform above opertions
'''


#OPEN,READ AND CLOSE FILE
'''
F=OPEN('FILE_NAME','MODE')
FILE_NAME=SAMPLE_TXT ::DEMO.DOCX
MODE=R:READ MODE ,W:WRITE MODE
DATA=F.READ()
F.CLOSE()
'''
#EXP1

f1=open('C:\python practices\demo.txt','r')
data=f1.read()
print(data)



















































































































