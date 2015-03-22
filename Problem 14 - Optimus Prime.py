# Problem 14 - Optimus Prime

def isPrime(number):
    for i in range(2, number -1):
        if number % i == 0:
            return False  
    return True

def optimus(number):
    if isPrime(number) == True:
        return number
    else:
        bigPrime = 0
        for i in range(number, number + 10000):
            if isPrime(i) == True:
                bigPrime = i
                break
        smallPrime = 0
        for i in range(number, number -10000, -1):
            if i <= 0:
                break
            elif isPrime(i) == True:
                smallPrime = i
                break
        if number - smallPrime == bigPrime - number:
            return smallPrime, bigPrime
        elif number - smallPrime < bigPrime - number:
            return smallPrime
        else:
            return bigPrime

number = int(input("Please enter a number: "))

print (optimus(number))




