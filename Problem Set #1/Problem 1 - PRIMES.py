#Prime Numbers

number = int(input("Enter a number: "))

def isPrime(number):
    for i in range(2, number -1):
        if number % i == 0:
            return False  
    return True

if isPrime(number) == True:
    print (str(number) + " is prime.")
else:
    print (str(number) + " is not prime.")
