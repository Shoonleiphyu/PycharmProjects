import random


MAX_INCREASE = 0.175 # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
new_file="OUTPUT_FILE"

def calculate_price():
    price = INITIAL_PRICE
    number_of_days = 0
    print(f"Starting price: ${price:,.2f}")

    out_file= open(new_file,'w')
    print("${:,.2F}".format(price), file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1
        price_change = 0
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:

            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        print(f"On day {number_of_days} price is ${price:,.2f}", file=out_file)

    out_file.close()
calculate_price()