
item_prices = []

num_items = int(input('Number of items: '))

for i in range (0, num_items):
   price = float(input('Enter price of item:'))
   item_prices.append(price)
   total = sum(item_prices)

if total >100:
   subtotal = total-total*10/100
   print(f"Your total amount is: {subtotal: .2f}")
else:
   print(f"Your total amount is: {total}")

