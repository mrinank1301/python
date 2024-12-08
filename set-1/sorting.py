import random

list = [random.randint(0, 100) for i in range(10)]
print(list)
list.sort()
print(f"asending order :{list}")
list.sort(reverse=True)
print(f"descending order :{list}")