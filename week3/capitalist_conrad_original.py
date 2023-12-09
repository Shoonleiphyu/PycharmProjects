import random

number_of_days = 0 # day_count
MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0


price = INITIAL_PRICE
print(f"Starting price: ${price:,.2f}")

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is ${price:,.2f}")