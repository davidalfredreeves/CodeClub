# Problem 9 - No Vowels

vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

string = "This is a sentence about strings"
for v in vowels:
    string = string.replace(v, "")
print (string)

