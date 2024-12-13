userInput= input("enter string:")
lowercase=userInput.lower()

if lowercase == lowercase[::-1]:  
    print("palindrome") 
else:
    print("not palindrome")


