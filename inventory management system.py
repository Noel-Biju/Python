inventory=[
    ("Laptop",5,30000.0),
    ("Headphones",15,500.0),
    ("Mouse",50,150.0),
    ("Keyboard",20,150.0),
    ("Monitor",10,3000.0)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=quantity*unit_price
    print(f"Item Name:{item_name},Total value:{stock_value}")
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print(f"Highest stock value is {highest_stock_value}")
print(f"Item with highest stock value is {item_with_highest_stock_value}")
