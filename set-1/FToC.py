userInput =int(input("enter number to change:")) 
change = input("F/C?:")

if change == "C" or change == "c":
    celsius = (userInput-32)* (5/9)
    print(f"celsius is {celsius}")
elif change == "F" or change == "f":
    fahrenheit = (userInput+32)*(9/5)
    print(f"fahrenheit is {fahrenheit}")
else:
    print("wrong input can't change please try again") 



