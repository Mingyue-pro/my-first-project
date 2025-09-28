# Write a programme that determines the name of a shape from its number of sides. Read the 
# number of sides from the user and then report the appropriate name as part of a meaningful 
# message. Your programme should support shapes with anywhere from 3 to up to (and including) 10 
# sides. If a number of sides outside of this range is entered then your programme should display an 
# appropriate error message.

def shape_name():
    sides_num = int(input("Please input the number of sides: "))
    shape_name = {
        3: "triangle",
        4: "Quadrilateral",
        5: "Pentagonal",
        6: "Hexagon",
        7: "Heptagonal",
        8: "Octagonal",
        9: "Nonagon",
        10: "Decagonal"

    }
    if sides_num < 3 or sides_num > 10:
        print("the shape is not available")
    else:

        appropriate_shape = shape_name[sides_num]
        print(f"The shape name is {appropriate_shape}")

shape_name()
