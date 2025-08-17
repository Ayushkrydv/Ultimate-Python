# sets are knows for its uniquess
# sets themselves are mutable you can add or remove elements
# Elements of set must be immutable

essential_spices = {"ginger", "cardamon","cinnamon"}
optional_spices = {"clove","gingers","black pepper"}

common_spices = essential_spices & optional_spices
print(f"common species : {common_spices}")

all_spices = essential_spices | optional_spices
print(f"all species : {all_spices}")

only_in_essential = essential_spices - optional_spices
print(f"only in essential : {only_in_essential}")

# membership
print(f"IS black pepper present in essential spices? { 'black pepper' in essential_spices}")


