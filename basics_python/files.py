from sys import argv
script,file_name=argv


file=open(file_name,'w')
temp_line=input("Enter any line that you want to add in the file")
file.write(temp_line)
file.close()

file=open(file_name)
print("The details are",file.read())
file.close()

file=open(file_name,'w')
print("I am now truncating all the elements of file")
file.truncate()
file.close()

file=open(file_name)
print(f"details are : \n")
print(file.read())
file.close()
