def toBase10(num,base):
    return int(num,base)

def fromBase10(num,base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num==0:
        return "0"
    result = ""
    while num>0:
        result = digits[num%base] + result
        num = num//base
    return result

number = int(input("enter number:"))
sourceBase= int(input("enter the base of the number:"))
targetBase = int(input("enter the target base:"))

base10Number = toBase10(number,sourceBase)
convertedNumber=fromBase10(base10Number,targetBase)
print(f"{number} in base {sourceBase} is {convertedNumber} in base {targetBase}")
