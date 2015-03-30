# Problem 2 - Naive Sorting

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
num3 = int(input("Please enter a third and final number: "))

if max(num1, num2, num3) == num1:
    print (str(min(num2, num3)) + ", " + str(max(num2, num3)) + ", " + str(num1))
elif max(num1, num2, num3) == num2:
    print (str(min(num1, num3)) + ", " + str(max(num1, num3)) + ", " + str(num2))
else:
    print (str(min(num1, num2)) + ", " + str(max(num1, num2)) + ", " + str(num3))
