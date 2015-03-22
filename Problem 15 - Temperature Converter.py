# Problem 15 - Temperature Converter

def toCelsius(number):
    number = ((number) - 32) * (5/9.0)
    number = round(number,2)
    return str(number) + "C"

def toFahrenheit(number):
    number = (number) * (9/5.0) + 32
    number = round(number,2)
    return str(number) + "F"

temp = input("Please enter a temperature to convert: ")

if temp[-1].upper() == "F":
    temp = temp[0:-1]
    temp = float(temp)
    print (toCelsius(temp))
else:
    temp = temp[0:-1]
    temp = float(temp)
    print (toFahrenheit(temp))

