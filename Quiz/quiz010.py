# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All 
# three sides of an equilateral triangle have the same length. And isosceles triangle has two sides that 
# are all the same length and a third side that is a different length. If all of the sides have different 
# lengths then the triangle is scalene.
# Write a programme that reads the lengths of the three sides of a triangle from the user. Then display 
# a message that states the triangle’s type

def triangle_name():
    side_a = float(input("enter the length of the first side: "))
    side_b = float(input("enter the length of the second side: "))
    side_c = float(input("enter the length of the third side: "))
   
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        print("These sides cannot form a triangle")
        return

    if side_a == side_b == side_c:
        print("This is an equilateral triangle")
    elif side_a == side_b or side_a == side_c or side_b == side_c :
        print("This is a isosceles triangle")
    else:
        print("This is a scalene triangle")

triangle_name()

