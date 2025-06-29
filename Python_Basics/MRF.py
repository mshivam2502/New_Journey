#map(), filter(), reduce()

#MAP
numbers = [1, 2, 3]
result = map(lambda a: a*2, numbers)
print(list(result))

#FILTER
numbers2 = [1,2,3,4,5,6]
result = filter(lambda n : n %2 == 0, numbers2)
print(list(result))

#REDUCE

from functools import reduce

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

total = reduce(lambda acc, item: acc + item[1], expenses, 0)
print(total)
