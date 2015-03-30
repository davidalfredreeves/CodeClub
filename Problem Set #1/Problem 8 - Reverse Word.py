# Problem 8 - Reverse Word

userString = input("Please enter a string: ")
newString = ""

for i in range(0, len(userString)):
    newString += userString[(i*-1) - 1]

print (newString.title())
