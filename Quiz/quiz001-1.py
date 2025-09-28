def loaves_bread():
    loaves_price = 3.49
    discount_rate = 0.60

    loaves = int(input("Please enter the number of bread: "))

    regular_price = loaves_price * loaves
    discount_price = loaves_price * loaves * discount_rate
    total_price = regular_price - discount_price

    print(f"The regular price is : £{regular_price:>8.2f}")
    print(f"The discount price is : £{discount_price:>8.2f}")
    print(f"The total price is : £{total_price:>8.2f}")

loaves_bread()


