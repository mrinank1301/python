import random

list =[random.randint(1,100) for i in range(10)]
print(list)
avg = sum(list)/len(list)
print(avg)