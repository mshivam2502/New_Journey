# Loops

# # While Loops
# while condition == True:
#     print("While Loop")

count = 0
while count<5 :
    print("while: " + str(count))
    count +=1

#for loop
items = [1,2,3,4]
for item in items:
    print("for: " + str(item))

for x in range(3,6):
    print("for in range: " + str(x))

# Break and Continue
# Break stops the entire loop whereas continue stops current iteration and moves onto the next iteration
for item in items:
    if item == 2:
        continue
    if item == 3:
        break
    print("for: " + str(item))


