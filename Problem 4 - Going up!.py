# Problem 4 - Going up!

numberList = []

while True:
    number = int(eval(input("Please enter a number: ")))
    if number == -1:
        condition = False
        for e in range(0,len(numberList)- 1):
            if numberList[e] < numberList[e+1]:
                condition = True
        if condition == True:
            print ("Yes")
            break
        else:
            print ("No")
            break
    else:
        numberList.append(number)
