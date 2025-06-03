print("Welcome to the shop")

items = []
prices = []

while True:
    item = input("Enter the item you want to buy (q to quit): ")
    if item != "q" and item != "" and item != " " and item != "\n" and item != "Q":
        price = float(input(f'Enter the price of {item} '))
        items.append(item)
        prices.append(price)
    else:
        break

total = sum(prices)
print(f'Your items are: \n{items} \nand your total is: \n{total:.2f}  ')
