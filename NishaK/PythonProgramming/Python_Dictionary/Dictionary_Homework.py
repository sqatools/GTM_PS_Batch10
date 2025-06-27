# write a python program to calculate the bill amount of fruit purchased
fruit_inventory = {'Apple': 100, 'Mango': 500, 'Banana': 300, 'Lichi': 250}
fruits_with_price = {'Apple': 20, 'Mango': 60, 'Banana': 30, 'Lichi': 50}
purchased_fruits = {'Apple': 5, 'Mango': 6, 'Banana': 12, 'Lichi': 10}
# updated
# fruit_investory = {'Apple': 95, 'Mango': 494, 'Banana': 288, 'Lichi': 240}

Total_bill = 0
for fruit, price in fruits_with_price.items():
    pur_fruits = purchased_fruits[fruit]
    fruit_bill = pur_fruits * price
    print(fruit, "|", price, "|", pur_fruits, "|", fruit_bill)
    Total_bill = Total_bill + fruit_bill
    fruit_inventory[fruit] = fruit_inventory[fruit] - pur_fruits

print("Total bill :", Total_bill)
print("Remaining Fruits :", fruit_inventory)


