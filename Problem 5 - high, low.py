# Problem 5 - You said high, I said low...

numberList = []

while True:
    number = int(eval(input("Please enter a number: ")))
    if number == -1:
        condition = False
        for e in range(0,len(numberList)- 1):
            if numberList[e] == numberList[e+1] + 1:
                print (numberList[e])
                condition = True
            elif numberList[e] == numberList[e+1] - 1:
                print (numberList[e])
                condition = True
        if condition == True:
            print ("Yes")
            break
        else:
            print ("No")
            break
    else:
        numberList.append(number)
