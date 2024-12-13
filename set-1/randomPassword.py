import random
import string

length = int(input("Enter the length of the password: "))
characters = string.ascii_letters # + string.digits + string.punctuation can also be written
password = "".join(random.choice(characters) for i in range(length))
print(password)