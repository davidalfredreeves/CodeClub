# Problem 11 - All the primes up to 1,000

for i in range(2, 1000):
    for each in range(2, i):
        if i % each == 0:
            break
    else:
        print (i)


