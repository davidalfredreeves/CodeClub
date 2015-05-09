from collections import Counter

class Echo:
    """Returns the string entered into it, or returns an error
    if a non-string was entered."""
    def __init__(self, text):
        self.text = text

    def __str__(self):
        """Returns the string entered into it, or returns an error
        if a non-string was entered."""
        if type(self.text) == str:
            return self.text
        else:
            return "Error"

class Box:

    isOpen = "NO"
    contents = None
    image = None

    def put(thing):
        """Puts an object into the box"""
        if Box.isOpen == "NO":
            return False
        elif Box.contents != None:
            return False
        else:
            Box.contents = thing
            return True

    def open():
        """Open the box and returns true if it has, otherwise false"""
        if Box.isOpen == "NO":
            Box.isOpen = "YES"
            return True
        else:
            return False

    def close():
        """Close the box and returns true if it has, otherwise false"""
        if Box.isOpen == "YES":
            Box.isOpen = "NO"
            return True
        else:
            return False

    def peak():
        """Returns an image of what is in the box"""
        Box.image = Box.contents
        return Box.image

    def get():
        """Takes the object from the box"""
        if Box.isOpen== "NO":
            return False
        else:
            thing = None
            thing = Box.contents
            Box.contents = None
            return thing

class Dancer:

    def __init__(self, name, partner=None):
        self.name = name
        self.partner = partner

    def dance(self):
        """Shows whether the dancer has a partner"""
        if self.partner != None:
            return self.name + " dances with " + str(self.partner) + "."
        else:
            return self.name + " dances on their own."

    def pair(self, other):
        """Pairs a dancer with a partner, if possible"""
        if self.partner != None:
            return False
        else:
            self.partner = other
            other.partner = self
            return True
        
    def __str__(self):
        return self.name

class Encryptor:

    def __init__(self, key):
        self.key = key

    def encode(string):
        """Will return an encoded string"""
        codemap = {"a": "00",  
                   "b": "01",
                   "c": "02",
                   "d": "03",
                   "e": "04",
                   "f": "05",
                   "g": "06",
                   "h": "07",
                   "i": "08",
                   "j": "09",
                   "k": "10"}

        string = string.lower()
        codelist = [codemap[i] for i in string]
        string = ""
        for i in codelist:
            string += i
        return string

    def decode(string):
        """Will return a decoded string"""
        codemap = {0: "a",
                   1: "b",
                   2: "c",
                   3: "d",
                   4: "e",
                   5: "f",
                   6: "g",
                   7: "h",
                   8: "i",
                   9: "j",
                   10: "k"}

        if len(string) < 2:
            return False
        if len(string) == 2:
            return codemap[int(string)]
        else:
            return codemap[int(string[0:2])] + Encryptor.decode(string[2:])
        
    def encrypt(self, word):
        """Will encrpypt a string"""
        word = Encryptor.encode(word)
        result = ""
        keypointer = 0
        for i in range(0,len(word),2):
            token = int(word[i:i+2])
            token += int(self.key[keypointer])
            token = str(token)
            if len(token) == 1:
                token = "0"+token
            result += token
            if keypointer >= len(self.key)-1:
                keypointer = 0
            else:
                keypointer += 1
        return result

    def decrypt(self, word):
        """Will decrypt a string"""
        result = ""
        keypointer = 0
        for i in range(0,len(word),2):
            token = int(word[i:i+2])
            token -= int(self.key[keypointer])
            token = str(token)
            if len(token) == 1:
                token = "0"+token
            result += token
            if keypointer >= len(self.key)-1:
                keypointer = 0
            else:
                keypointer += 1
        return Encryptor.decode(result)


class Employee:

    def __init__(self, ID, name, job_title=None, manager=None):
        self.ID = ID
        self.name = name
        self.job_title = job_title
        self.manager = manager

    def __str__(self):
        return "ID: " + self.ID + " NAME: " + self.name \
               + " JOB TITLE: " + str(self.job_title) \
               + " MANAGER: " + str(self.manager)

    def equals(self, other):
        """Checks whether an employees ID is equal to anothers"""
        if self.ID == other.ID:
            return True
        else:
            return False

    def setManager(self, manager):
        """Set a manager to an employee"""
        self.manager = manager.name

class Manager(Employee):

    def __init__(self, ID, name, job_title, manager, underlings=[]):
        super().__init__(ID, name, job_title, manager)
        self.underlings = underlings

    def __str__(self):
        return super().__str__() + " EMPLOYEES: " + str(self.underlings)

    def addEmployee(self, employee):
        """Gives a new employee to a manager"""
        self.underlings.append(employee.name)
        employee.manager = self.name

class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.tempNumerator = self.numerator
        self.tempDenominator = self.denominator

    def lcm(x, y):
        """This function takes two integers and
        returns the lowest common multilpe."""
        if x > y:
            greater = x
        else:
            greater = y
        while(True):
            if ((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm

    def get_next_prime_factor(n):
        if n % 2 == 0:
            return 2
        for x in range(3,n//2,2):
            if n % x == 0:
                return x
        return n

    def all_prime_factors(number):
        primeList = []
        while number != 1:
            nextPrime = Fraction.get_next_prime_factor(number)
            primeList.append(nextPrime)
            number = number // nextPrime
        return primeList

    def remove_common_elements(list1, list2):
        a = Counter(list1)
        b = Counter(list2)
        c = list((a-b).elements())
        d = list((b-a).elements())
        return c, d

    def multiply(list):
        total = 1
        for each in list:
            total *= each
        return total

    def simplify(numerator, denominator):
        numList = Fraction.all_prime_factors(numerator)
        denList = Fraction.all_prime_factors(denominator)
        newNumList, newDenList = Fraction.remove_common_elements(numList, denList)
        newNumerator = Fraction.multiply(newNumList)
        newDenominator = Fraction.multiply(newDenList)
        return newNumerator, newDenominator

    def overload(number1, number2):
        if number1 >= number2:
            return True
        else:
            return False

    def reduce(numerator, denominator):
        count = 0
        while numerator >= denominator:
            numerator = numerator - denominator
            count += 1
        return count, numerator

    def __str__(self):
        self.tempNumerator, self.tempDenominator = Fraction.simplify(self.numerator
                                                            , self.denominator)
        if Fraction.overload(self.tempNumerator, self.tempDenominator) == False:
            return str(self.tempNumerator) + "/" + str(self.tempDenominator)
        else:
            integer = Fraction.reduce(self.tempNumerator, self.tempDenominator)[0]
            newNumerator = Fraction.reduce(self.tempNumerator, self.tempDenominator)[1]
            if newNumerator > 0:
                return str(integer) + " " + str(newNumerator) + "/" + str(self.tempDenominator)
            else:
                return str(integer)
    def total(numerator, denominator):
        numerator, denominator = Fraction.simplify(numerator, denominator)
        if Fraction.overload(numerator, denominator) == False:
            return str(numerator) + "/" + str(denominator)
        else:
            integer = Fraction.reduce(numerator, denominator)[0]
            newNumerator = Fraction.reduce(numerator, denominator)[1]
            if newNumerator > 0:
                return str(integer) + " " + str(newNumerator) + "/" + str(denominator)
            else:
                return str(integer)

    def __add__(self, other):
        if self.denominator == other.denominator:
            newDenominator = self.denominator
        else:
            newDenominator = Fraction.lcm(self.denominator, other.denominator)
        self.numerator = self.numerator * (newDenominator // self.denominator)
        other.numerator = other.numerator * (newDenominator // other.denominator)
        newNumerator = self.numerator + other.numerator
        self.numerator = self.tempNumerator
        self.denominator = self.tempDenominator
        return Fraction.total(newNumerator, newDenominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            newDenominator = self.denominator
        else:
            newDenominator = Fraction.lcm(self.denominator, other.denominator)
        self.numerator = self.numerator * (newDenominator // self.denominator)
        other.numerator = other.numerator * (newDenominator // other.denominator)
        newNumerator = self.numerator - other.numerator
        self.numerator = self.tempNumerator
        self.denominator = self.tempDenominator
        return Fraction.total(newNumerator, newDenominator)

    def __mul__(self, other):
        newNumerator = self.numerator * other.numerator
        newDenominator = self.denominator * other.denominator
        self.numerator = self.tempNumerator
        self.denominator = self.tempDenominator
        return Fraction.total(newNumerator, newDenominator)

    def __truediv__(self, other):
        newOtherNumerator = other.denominator
        newOtherDenominator = other.numerator
        newNumerator = self.numerator * newOtherNumerator
        newDenominator = self.denominator * newOtherDenominator
        self.numerator = self.tempNumerator
        self.denominator = self.tempDenominator
        return Fraction.total(newNumerator, newDenominator)

    def __gt__(self, other):
        if self.denominator == other.denominator:
            newDenominator = self.denominator
        else:
            newDenominator = Fraction.lcm(self.denominator, other.denominator)
        self.numerator = self.numerator * (newDenominator // self.denominator)
        other.numerator = other.numerator * (newDenominator // other.denominator)
        if self.numerator > other.numerator:
            self.numerator = self.tempNumerator
            self.denominator = self.tempDenominator
            return True
        else:
            self.numerator = self.tempNumerator
            self.denominator = self.tempDenominator
            return False

    def __ge__(self, other):
        if self.denominator == other.denominator:
            newDenominator = self.denominator
        else:
            newDenominator = Fraction.lcm(self.denominator, other.denominator)
        self.numerator = self.numerator * (newDenominator // self.denominator)
        other.numerator = other.numerator * (newDenominator // other.denominator)
        if self.numerator >= other.numerator:
            self.numerator = self.tempNumerator
            self.denominator = self.tempDenominator
            return True
        else:
            self.numerator = self.tempNumerator
            self.denominator = self.tempDenominator
            return False

    def __eq__(self, other):
        if self.denominator == other.denominator:
            newDenominator = self.denominator
        else:
            newDenominator = Fraction.lcm(self.denominator, other.denominator)
        self.numerator = self.numerator * (newDenominator // self.denominator)
        other.numerator = other.numerator * (newDenominator // other.denominator)
        if self.numerator == other.numerator:
            self.numerator = self.tempNumerator
            self.denominator = self.tempDenominator
            return True
        else:
            self.numerator = self.tempNumerator
            self.denominator = self.tempDenominator
            return False

    def __le__(self, other):
        if self.denominator == other.denominator:
            newDenominator = self.denominator
        else:
            newDenominator = Fraction.lcm(self.denominator, other.denominator)
        self.numerator = self.numerator * (newDenominator // self.denominator)
        other.numerator = other.numerator * (newDenominator // other.denominator)
        if self.numerator <= other.numerator:
            self.numerator = self.tempNumerator
            self.denominator = self.tempDenominator
            return True
        else:
            self.numerator = self.tempNumerator
            self.denominator = self.tempDenominator
            return False

    def __lt__(self, other):
        if self.denominator == other.denominator:
            newDenominator = self.denominator
        else:
            newDenominator = Fraction.lcm(self.denominator, other.denominator)
        self.numerator = self.numerator * (newDenominator // self.denominator)
        other.numerator = other.numerator * (newDenominator // other.denominator)
        if self.numerator < other.numerator:
            self.numerator = self.tempNumerator
            self.denominator = self.tempDenominator
            return True
        else:
            self.numerator = self.tempNumerator
            self.denominator = self.tempDenominator
            return False
