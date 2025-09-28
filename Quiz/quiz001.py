#bakery sells loaves of bread for £ 3.49 each. Day old bread is discounted by 60 percent. Write a 
#programme that begins by reading the number of loaves of day old bread being purchased from the 
#user. Then your programme should display the regular price for the bread, the discount because it is 
#a day old, and the total price. Each of these amounts should be displayed on its own line with an 
#appropriate label. All of the values should be displayed using two decimal places, and the decimal 
#points in all the numbers should be aligned when reasonable values are entered by the user.

def loan_bread_price() :
    loaves_price = 3.49
    discount_rate = 0.60

    loaves = int(input("Please enter the number of loaves: "))
    
    regular_price = loaves * loaves_price
    discount_price = loaves * loaves_price * discount_rate
    total_price = regular_price - discount_price

    print(f"regular_price: £{regular_price:>8.2f}")
    print(f"discount_price: £{discount_price:>8.2f}")
    print(f"total_price: £{total_price:>8.2f}")

loan_bread_price()