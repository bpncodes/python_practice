#Functions and files
from sys import argv

def read(file_var):
    file=open(file_var)
    print(file.read())
    file.close()

def readline(file_var):
    file=open(file_var)
    print(1,file.readline())
    print(2,file.readline())
    file.close()

def rewind(file_var):
    file=open(file_var)
    file.seek(0)

script,file_var=argv
read(file_var)
#file=open(file_var)
#line=1
#readline(line+1,file_var)      So inorder to readline youve to open the file only once outside the function
#readline(line+2,file_var)
readline(file_var)
