#Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If 
#a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay
#banana becomes ananabay, and aardvark becomes aarvarkway. Create a programme that will 
#ask the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in 
#lower case.

def pig_latin():
    word = input("Please enter a word:").strip().lower()
    if word[0] in ('a','e','i','o','u'):
        print(f"The new word is: {word}way")
    else:
        print(f"The new word is: {word[1:]}{word[0]}ay")

pig_latin()