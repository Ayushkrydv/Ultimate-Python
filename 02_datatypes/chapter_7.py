# Tuples

user = ("Ayush", "Manish", "Nitish")
(user1,user2,user3) = user

print(f"users : {user1}, {user2}, {user3}")

# we can swap the two variable without using #third variable
silver_ratio, gold_ratio = 3,4
print(f"Ratio is S : {silver_ratio} and G : {gold_ratio}")

#swap
silver_ratio, gold_ratio = gold_ratio,silver_ratio
print(f"Ratio is S : {silver_ratio} and G : {gold_ratio}")

# membership

print(f"Is Ayush in user ? {"Ayush" in user}")
# it is case sensitive you should write exactlly as you write in tuples