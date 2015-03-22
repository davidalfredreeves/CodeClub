# Problem 3 - Maximising

numberList = []

while True:
    number = eval(input("Please enter a number: "))
    if number == -1:
        if len(numberList) < 1:
            print ("There are no numbers.")
            break
        print (max(numberList))
        break
    else:
        numberList.append(number)
