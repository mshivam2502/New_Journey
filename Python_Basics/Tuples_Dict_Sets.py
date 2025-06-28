# # A tuple cannot be modified it is immutable unlike a List
# a_tuple = ("apple", "banana", "cherry")

######################################################################################
# Dictonary is a list of key value pairs

# self_info = {"name": "Shiva", "Age": "20","Salary":20000}

# self_info["name"] = "Daksh"

# print(self_info.get("name"))
# print(self_info["Salary"])

# # Conert all items into alist
# print(list(self_info.items()))

# #you can directly add to the dictionary
# self_info["fav food"] = "Sweets"

# del self_info["Salary"] #can delete the entry

# print(list(self_info.items()))

########################################################################################
# Sets are like tuples but mutable look like dict but dont have a key value pair
# Sets are not ordered they are automatically sorted, no duplicate values allowed,they are sets in maths

# Intersection of a set
set1 = {"Shiva","Mayur","Neha"}
set2 = {"Neha"}

intersect = set1 & set2

print(intersect)

# Union of a set
set3 = {"Rishi"}
uni = set1 | set3

print(uni)

# Difference b/w the set
dif = set1-set2

print(dif)

# Subset
isSubset = set1 > set2
print(isSubset)