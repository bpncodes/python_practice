from sys import argv
script,first,second=argv
def greater(first,second):
    if(first>second):
        print(f"The greater number is {first}")
    elif(second>first):
        print(f"The greater number is {second}")
    else:
        print("Both are equal")
greater(first,second)
