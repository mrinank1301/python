number = int(input("enter number:"))
factorial = 1
for i in range(1,number+1):
    factorial = factorial * i

print(factorial)

# with Recurssive funtion

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)

# result=fact(5)
# print(f"result is {result}")