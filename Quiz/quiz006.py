# Write a programme that asks the user’s age. If they are 18 or over, display the message “you can 
# vote”. If they are 17, display the message “You can learn how to drive”. If they are 16, display the 
# message “you can buy a lottery ticket” and if they are under 16, display the message “You can go 
# Trick-or-Treating”

def vote_age():
    age = int(input("please enter your age"))
    if age >= 18:
        print("You can vote")
    elif age == 17:
        print("You can learn how to drive")
    elif age == 16:
        print("You can buy a lottery ticket")
    else:
        print("You can go Trick-or-Treating")

vote_age()