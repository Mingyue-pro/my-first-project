# Write a programme that displays the following message:
# 1) Square
# 2) Triangle
# Enter a number:
# If a user enters 1, then it should ask them for the length of one of its sides and display the area. 
# If they select 2, it should ask for the base and height of the triangle and displays the area. If they 
# type in anything else, it should give them a suitable error.

def area():

    try:
       
        entered_message = int(input("Please enter the number(1/square 2/triangle): "))
        
        if entered_message == 1:
            square_side = float(input("Please input the length of the square: "))
            square_area = square_side * square_side
            print(f"The area of this square is: {square_area:.2f}")
        
        elif entered_message ==2:
            triangle_base = float(input("Please input the base of the triangle: "))
            triangle_height = float(input("Please input the height of the triangle: "))
            triangle_area = (triangle_base * triangle_height)/2
            print(f"The area of this triangle is: {triangle_area:.2f}")
        
        else:
            print("Your choice is not available")

    except ValueError:
        print("Error: Please enter the valid number")

area()