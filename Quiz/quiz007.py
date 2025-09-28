# Write a programme that reads an integer from the user. 
# Then your programme should display a message indicating whether the integer is even or odd

def integer():
    integer = int(input("please enter an integer: "))
    if integer%2 == 0:
        print(f"{integer} is even")
    else:
        print(f"{integer} is odd")

integer()