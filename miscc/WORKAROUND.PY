backpack = ["hot", "cold", "hello", "poo", "poo", "poo", "ks", "dd", "poo"]

# length of the list is 9
# list is from 0 to len()-1
for item in backpack[:]:
    if item.casefold() == "poo":
        backpack.remove(item)

new_backpack = backpack

print(new_backpack)


