"""
Ask for number of items
get the price for each
add prices of items together
see if price is more than 100 for 10% discount
print price
"""

number_of_items = int(input("Please enter number of items: "))
total_cost = 0

while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Please enter number of items: "))

for i in range(number_of_items):
    cost = float(input('Enter price of item: '))
    total_cost += cost

if total_cost > 100:
    total_cost = 0.9 * total_cost

print(total_cost)
