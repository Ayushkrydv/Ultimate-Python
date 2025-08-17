# chai price calculator

cup_size = input("What size of cup u want (small/medium/large) ").lower()
print(f"user take : {cup_size}")
if cup_size == "small":
    print(f"Rs 10 for {cup_size}")
elif  cup_size == "large" :
    print(f"Rs 20 for {cup_size}")
elif  cup_size == "Medium":    
    print(f"Rs 15 for {cup_size}")
else:
    print("unknow cup size")

