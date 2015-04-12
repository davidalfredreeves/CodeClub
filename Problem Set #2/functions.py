## List of functions for Problem Set #2

## Problem 2 - Remove
def remove(someList, someNumber):
    collection = []
    for each in someList:
        if each < someNumber:
            collection.append(each)
    for each in collection:
        if each in someList:
            someList.remove(each)
    return someList

## Problem 3 - Copy Element
def copyElementsUnder(someList, someNumber):
    newList = []
    for elements in someList:
        if elements >= someNumber:
            newList.append(elements)
    return newList

## Problem 4 - Remove By List
def removeByList(someList, collection):
    for each in collection:
        if each in someList:
            someList.remove(each)
    return someList

## Problem 5 - Remove Duplicates
def removeDuplicates(someList):
    newList = []
    for each in someList:
        if each not in newList:
            newList.append(each)
    return sorted(newList)

## Problem 6 - List Overlap
def listOverlap(collection1, collection2):
    sharedList = []
    for each in collection1:
        if each in collection2:
            sharedList.append(each)
    return sharedList

## Problem 7 - Create List
def createList(start,stop,step=1):
    newList = []
    for i in range(start, stop, step):
        newList.append(i)
    return newList

## Problem 8 - Club Entry
def clubEntry(name, guestList):
    if name in guestList:
        return guestList[name]
    else:
        return False

## Problem 9 - Hanoi
##base case = 1
def hanoi(number):
    if number == 1:
        return 1
    else:
        return 2* (hanoi(number-1)) + 1
    
## Problem 10 - Encode
encryptKey = {"a":"00", "b":"01", "c":"02", "d":"03", "e":"04", "f":"05", "g":"06", "h":"07", "i":"08", "j":"09"}
decryptKey = {"00":"a", "01":"b", "02":"c", "03":"d", "04":"e", "05":"f", "06":"g", "07":"h", "08":"i", "09":"j"}
    
def encode(string):
    newString = ""
    for each in string.lower():
        if each in encryptKey:
            newString = newString + encryptKey[each]
        else:
            newString = newString + each
    return newString

## Problem 11 - Decode
def decode(string):
    newList = []
    newString = ""
    while len(string) > 0:
        newList.append(string[0:2])
        string = string[2:]
    #return string, newList
    for each in newList:
        if each in decryptKey:
            newString = newString + decryptKey[each]
        else:
            newString = newString + each
    return newString

## Problem 12 - Ecrypt
def encrypt(word, key):
    if type(key) is int:
        (key) = (key,)
    while len(key) < len(word):
        key *= 2
    stringKey = ""
    for each in key:
        stringKey += str(each)
    newList = []
    count = 0
    count2 = 0
    while count < len(word):
        if word[count] == "0":
            newList.append(word[count])
        else:
            newList.append(int(word[count]) + int(key[count2]))
            count2 += 1
        count += 1
    newWord = ""
    char = ""
    for each in newList:
        if type(each) is str:
            newWord = newWord + each
        else:
            newWord = newWord + str(each)
    return newWord

## Problem 13 - Decrypt
def decrypt(word, key):
    if type(key) is int:
        (key) = (key,)
    while len(key) < len(word):
        key *= 2
    stringKey = ""
    for each in key:
        stringKey += str(each)
    newList = []
    count = 0
    count2 = 0
    while count < len(word):
        if word[count] == "0":
            newList.append(word[count])
        else:
            newList.append(int(word[count]) - int(key[count2]))
            count2 += 1
        count += 1
    newWord = ""
    char = ""
    for each in newList:
        if type(each) is str:
            newWord = newWord + each
        else:
            newWord = newWord + str(each)
    return newWord

## Problem 14 - Hailstone numbers
def hailNum(number):
    if number == 1:
        return [1]
    if number % 2 == 0:
        return [number] + hailNum(number//2)
    else:
        return [number] + hailNum((number * 3)+1)

    
