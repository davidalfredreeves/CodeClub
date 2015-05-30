import datetime
import random
from os import walk
from os import rename
import os

def inputint(number):
    while True:
        try:
            n = number
            if n == float(n):
                return("Not a valid integer! Please try again.")
            n = int(n)
            break
        except ValueError:
            return("Not a valid integer! Please try again.")
    return("Great, you successfully entered an integer!")


def log(message):
    l = open("log.txt", "a")
    l.write(message)
    l.write("\n")
    l.close()
    return("You've entered " + "'" + message + "'" + " to the log.")

def daysold(date):
    try:
        now = datetime.datetime.now()
        newNow = now.date()
        then = datetime.datetime.strptime(date, "%d/%m/%Y")
        diff = newNow - then.date()
        return("There have been " + str(diff.days) + " days since " + date + ".")
    except TypeError:
        return("False.")

def parse_date(entry):
    try:
        date = datetime.datetime.strptime(str(entry), "%d/%m/%Y")
        newDate = date.strftime("%d/%m/%Y")
        return(newDate)
    except ValueError:
        return("Please enter a date in the dd/mm/yyyy format, and as a string.")

def randomSample(aList, size):
    if size > len(aList):
        return("The size of sample you have requested is greater than the list")
    sample = random.randint(1, size)
    count = size
    newList = []
    while count > 0:
        number = random.randint(0, len(aList)-1)
        newList.append(aList[number])
        aList.remove(aList[number])
        count = count - 1
    return(newList)

def get_files(path):
    files = []
    for (dirpath, dirnames, filenames) in walk(path):
         files.extend(filenames)
         break
    return(files)

def bulk_rename(folder, name):
    files = get_files(folder)
    #print(files)
    os.chdir(folder)
    i = 1
    for file in files:
        #print(file)
        rename(file, name + str(i) + ".txt")
        i += 1
    os.chdir("..")


