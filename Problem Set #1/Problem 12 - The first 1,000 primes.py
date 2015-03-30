# Problem 12 - THe first 1,000 prime numbers

def findPrimes(target):
    count = 0
    primes = []
    for i in range(2, 100000):
        for each in range(2, i):
            if i % each == 0:
                break
        else:
            primes.append(i)
            count = count + 1
            if count == target:
                return primes


print (findPrimes(1000))
