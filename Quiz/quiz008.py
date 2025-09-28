# In the exercise, you will create a programme that reads a letter of the alphabet from the user. If the 
# user enters a, e, i, o or u then your programme should display a message indicating that the 
# entered letter is a vowel. If a user enters y then your programme should display a message 
# indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise, your 
# programme should display a message indicating that the letter is a consonant

def letter():
    entered_letter = input("Please enter the letter: ").strip().lower()
    if entered_letter in ('a','e','i','o','u'):
        print(f"{entered_letter} is a vowel")
    elif entered_letter == 'y':
        print(f"{entered_letter} sometines is vowel, and sometimes is a consonant")
    else:
        print(f"{entered_letter} is a consonant")

letter()