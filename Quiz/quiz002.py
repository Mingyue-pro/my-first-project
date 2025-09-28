#write a programme that asks the user to type in the first line of their favourite song and display the 
#length of that string. The programme should also ask a starting number and an ending number and 
#then display just that section of the text.
def song_name():

    first_line = str(input(f"Please type the first line of your favourate song: "))
    length = int(len(first_line))
    starting_number = int(input(f"Please type the starting number: "))
    ending_number = int(input(f"Please type the ending number: "))
    section = first_line[starting_number-1:ending_number]

    print(f"The length of fiirst line is: {length}")
    print(f"The section of the Text is: {section}")

song_name()

