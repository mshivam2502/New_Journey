# Sorting a list

# Way 1 changes the original list

items = ["bob", "Baile", "Regurd"]

items.sort(key = str.lower) # set the sorting to case insensitive

print(items)

# Way 2 without cahnging original list

items2 = ["bob", "Baile", "Regurd"]
print(sorted(items2,key = str.lower))