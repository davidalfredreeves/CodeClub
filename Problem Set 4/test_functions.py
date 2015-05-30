import functions

print(functions.inputint(4))
print("EXPECTED: 'Great, you succesfully entered an integer.'")
print(functions.inputint("4"))
print("EXPECTED: 'Great, you succesfully entered an integer.'")
print(functions.inputint(4.1))
print("EXPECTED: 'Not a valid integer! Please try again.'")
print(functions.inputint("fish"))
print("EXPECTED: 'Not a valid integer! Please try again.'")

print(functions.log("Test1"))
print("EXPECTED: 'You've entered 'Test1' to the log.'")

print(functions.daysold(28/5/15))
print("EXPECTED: 'False'")
print(functions.daysold("28/05/2015"))
print("EXPECTED: 'There have been 1 days since 28/5/15.'")
print(functions.daysold(28515))
print("EXPECTED: 'False'")

print(functions.parse_date("17/10/1987"))
print("EXPECTED: '17/10/1987'")
print(functions.parse_date(17/10/1987))
print("EXPECTED: 'Please enter a date in the dd/mm/yyyy format, and as a string.")
print(functions.parse_date(1255423525))
print("EXPECTED: 'Please enter a date in the dd/mm/yyyy format, and as a string.")

print(functions.randomSample(["1", "2", "3", "4", "5"], 3))

print(functions.get_files("testFolder"))
functions.bulk_rename("testFolder", "example")
print(functions.get_files("testFolder"))
