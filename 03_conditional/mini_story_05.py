# run online tea store

order_amount = int(input("enter the order amount: "))
delivery_fee = 0 if order_amount>300 else 30
print(f"delivery fee {delivery_fee} ")