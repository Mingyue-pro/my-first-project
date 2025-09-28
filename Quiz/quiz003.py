#Write a programme that asks the user to enter their first name. If the length of the first name is 
#under five characters, the programme should ask them to enter their surname and join them 
#together (without a space) and display the name in upper case. If the length of their first name is five 
#or more characters, display their first name in lower case.
def input_name():
    first_name = input("Please enter your first name: ")
    name_len = len(first_name)
    if name_len < 5:
        surname = str(input("Please enter your surname: "))
        print(f"{first_name.upper()}{surname.upper()}")
    else:
        print(f"{first_name.lower()}")

input_name()
