my_cart = ["apple","bananas","milk"]
print(f"Grocery list: {my_cart}")

my_cart.append("bread")
print(f"Grocery list: {my_cart}")

my_cart.insert(0,"ketchup")
print(f"Grocery list: {my_cart}")

my_cart.remove("bananas")
print(f"Grocery list: {my_cart}")

removed_item=my_cart.pop()
print(f"removed_item: {removed_item}")

ingredient  = ["rice","butter"]
my_cart.extend(ingredient)
print(f"Grocery list: {my_cart}")

my_cart.sort()
print(f"Grocery list: {my_cart}")

reversed_item = my_cart.reverse()
print(f"reversed_item list: {my_cart}")

sweet_ingrwdient = ["juice","jam"]
resulting_list = my_cart + sweet_ingrwdient
print(f"Grocery list: {my_cart}")

duliplicate = my_cart * 2
print(f"duliplicate : {duliplicate}")

string =  "tomato cucumber spinach"

newString = bytearray(b"tomato cucumber spinach")
print(f"converted list : {newString}")