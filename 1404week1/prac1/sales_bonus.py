sales = float(input("Enter sales: $"))
if sales < 1000:
    print("You get 10% bonus")
    total = sales * 10 / 100
    print(f"your bonus is {total:}")
    print(f"Your total amount is {sales - total:} ")
elif sales >= 1000:
    print("You get 15% bonus")
    total = sales * 15 / 100
    print(f"your bonus is {total:}")
    print(f"Your total amount is {sales - total:} ")

