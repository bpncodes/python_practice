#normal input
print("Hello there !")
name=input("Please enter your name : ")
age=input(f"Hello {name} what is your age : ") #this is formatted string
if(int(age)<18):
    print(f"You are not eligible {name}")
else:
    print(f"You are eligible {name}")

a=input("Enter a numner")
print(type(a)) #This is a string
a=int(a) #Now this is a integer
print(f"The number is {a} ")
print(type(a))
