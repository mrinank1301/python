userInput= input("enter string:")

if userInput == userInput[::-1]:    #we can also write userInput == userInput.reverse()
    print("palindrome") 
else:
    print("not palindrome")