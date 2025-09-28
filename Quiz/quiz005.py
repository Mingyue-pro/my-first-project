#Write a programme that asks the user if it is raining and convert their answer to lower case so that it 
#doesn’t matter what case they type in. If they answer “yes”, ask if it is windy. If they answer “yes” to 
#the second question, display the answer “It’s too windy for an umbrella”, otherwise display the 
#message “Take an umbrella”. If they did not answer “yes” to the first question, display the answer 
#“Enjoy your day”

def raining_weather():
    first_question = input("Is it raining(yes/no)? ").strip().lower()
    if first_question == 'yes' :
        second_question = input("Is it windy(yes/no)? ").strip().lower()
        if second_question == 'yes' :
            print("It's too windy for an umbrella")
        else :
            print("take an umbrella")
    else :
        print("Enjoy your day")

raining_weather()