import functions

## Problem 2 - Remove
print(functions.remove([1,2,3,4,5,6,7], 5)) #Expect [5,6,7]
print(functions.remove([7,6,5,4,3,2,1], 5)) #Expect [7,6,5]
print(functions.remove([1,1,1,1], 1)) #Expect [1,1,1,1]
print(functions.remove([1,1,1,1], 2)) #Expect []
print(functions.remove([-3,-2,-1,0,1,2,3], 0)) #Expect [0,1,2,3]

## Problem 3 - copyElements
print(functions.copyElementsUnder([1,2,3,4,5,6,7], 5)) #Expect [5,6,7]
print(functions.copyElementsUnder([7,6,5,4,3,2,1], 5)) #Expect [7,6,5]
print(functions.copyElementsUnder([1,1,1,1], 1)) #Expect [1,1,1,1]
print(functions.copyElementsUnder([1,1,1,1], 2)) #Expect []
print(functions.copyElementsUnder([-3,-2,-1,0,1,2,3], 0)) #Expect [0,1,2,3]

## Problem 4 - removeByList
print(functions.removeByList([1,2,3,4,5], (2,3,4))) #Expect [1,5]
print(functions.removeByList([-3,-2,-1,0,1,2,3], (-4,-3,-2,-1,7))) #Expect [0,1,2,3]
print(functions.removeByList([1,2,3], (1,2,3))) #Expect []
print(functions.removeByList([1,2,3], [1,2,3])) #Expect []
print(functions.removeByList([1,2,3], {1,2,3})) #Expect []
print(functions.removeByList([1,2,3,4], {2,3,4,5})) #Expect [1]

## Problem 5 - removeDuplicates
print(functions.removeDuplicates([1,1,2,2,3,3,])) #Expect [1,2,3]
print(functions.removeDuplicates([3,3,2,1,2,1,])) #Expect [1,2,3]
print(functions.removeDuplicates([1,1,1,1,1])) #Expect [1]
print(functions.removeDuplicates([1])) #Expect [1]
print(functions.removeDuplicates([])) #Expect []

## Problem 6 - listOverlap
print(functions.listOverlap([1,2,3],[3,4,5])) #Expect [3]
print(functions.listOverlap([1,2,3],[1,2,3,])) #Expect [1,2,3]
print(functions.listOverlap([1,2,3],[4,5,6])) #Expect []
print(functions.listOverlap((1,2,3),(3,4,5))) #Expect [3]
print(functions.listOverlap((1,2,3),(1,2,3))) #Expect [1,2,3]
print(functions.listOverlap((1,2,3),(4,5,6))) #Expect []
print(functions.listOverlap({1,2,3},[3,4,5])) #Expect [3]
print(functions.listOverlap((1,2,3),{1,2,3})) #Expect [1,2,3]
print(functions.listOverlap([1,2,3],{4,5,6})) #Expect []

## Problem 7 - createList
print(functions.createList(1,10,1)) #Expect [1,2,3,4,5,6,7,8,9]
print(functions.createList(1,10)) #Expect [1,2,3,4,5,6,7,8,9]
print(functions.createList(-5,6)) #Expect [-5,-4,-3,-2,-1,0,1,2,3,4,5]
print(functions.createList(-5,6,2)) #Expect [-5,-3,-1,1,3,5]
print(functions.createList(1,1,1)) #Expect []
print(functions.createList(1,2)) #Expect [1]
print(functions.createList(5,1)) #Expect []

## Problem 8 - clubEntry
guestList = {"Jamie": True, "Tomas" : False}
print(functions.clubEntry("Jamie", guestList)) #Expect True
print(functions.clubEntry("Tomas", guestList)) #Expect False
print(functions.clubEntry("Sally", guestList)) #Expect False

## Problem 9 - hanoi

## Problem 10 - encode
print(functions.encode("abcdefghij")) # 00010203040506070809
print(functions.encode("jihgfedcba")) # 09080706050403020100
print(functions.encode("ababab")) # 000100010001
print(functions.encode("abadidea")) # 0001000308030400
print(functions.encode("abcdefghij")) # 00010203040506070809
print(functions.encode("thisisafullandcompletesentence")) # t0708s08s0005ull00n0302ompl04t04s04nt04n0204

## Problem 11 - decode
print(functions.decode("00010203040506070809")) # abcdefghi
print(functions.decode("09080706050403020100")) #jihgfedcba
print(functions.decode("000100010001")) # ababab
print(functions.decode("0001000308030400")) # abadidea
print(functions.decode("00010203040506070809")) # abcdefghij
print(functions.decode("t0708s08s0005ull00n0302ompl04t04s04nt04n0204")) # thisisafullandcompletesentence

## Problem 12 - encrypt
print(functions.encrypt("01020304", (4,5,1,2))) # 05070406
print(functions.encrypt("07030509", (2))) # 090507011

## Problem 13 - decrypt
print(functions.decrypt("05070406", (4,5,1,2))) # 01020304
print(functions.decrypt("090507011", (2))) # 07030509
