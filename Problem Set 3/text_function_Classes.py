import Classes

print(Classes.Echo("This is a string!"))
print("EXPECTED: 'This is a string!'")
print(Classes.Echo(25 + 2))
print("EXPECTED: 'Error'")
print(Classes.Echo("123"))
print("EXPECTED: '123'")
print(Classes.Echo(123))
print("Expected: 'Error'")

print(Classes.Box.put("Object"))
print("EXPECTED: 'False'") 
print(Classes.Box.open())
print("EXPECTED: 'True'")
print(Classes.Box.open())
print("EXPECTED: 'False'")
print(Classes.Box.put("Object"))
print("EXPECTED: 'True'")
print(Classes.Box.put("AnotherObject"))
print("EXPECTED: 'False'")
print(Classes.Box.close())
print("EXPECTED: 'True'")
print(Classes.Box.close())
print("EXPECTED: 'False'")
print(Classes.Box.peak())
print("EXPECTED: 'Object'")
print(Classes.Box.get())
print("EXPECTED: 'False'")
print(Classes.Box.open())
print("EXPECTED: 'True'")
print(Classes.Box.get())
print("EXPECTED: 'Object'")
print(Classes.Box.peak())
print("EXPECTED: 'None'")

steve = Classes.Dancer("Steve", "Dorah")
dorah = Classes.Dancer("Dorah", "Steve")
print(steve)
print("EXPECTED: 'Steve'")
print(dorah)
print("EXPECTED: 'Dorah'")
print(steve.dance())
print("EXPECTED: 'Steve dances with Dorah'")
print(dorah.dance())
print("EXPECTED: 'Dorah dances with Steve'")
cloe = Classes.Dancer("Cloe")
print(cloe.dance())
print("EXPECTED: 'Cloe dances on their own'")
print(steve.pair(cloe))
print("EXPECTED: 'False'")
bob = Classes.Dancer("Bob")
print(bob.pair(cloe))
print("EXPECTED: 'True'")
print(cloe.dance())
print("Expected: 'Cloe dances with Bob'")

code1 = Classes.Encryptor([1,2,3])
print(code1.encrypt("Abcde"))
print("EXPECTED: 0103050406")
print(code1.decrypt(code1.encrypt("EDCBa")))
print("EXPECTED: edcba")

carl = Classes.Employee("001", "Carl", "Nuclear Technician")
print(carl)
print("EXPECTED: 'ID: 001 NAME: Carl JOB TITLE: Nuclear Technician " \
      "MANAGER: None")
lenny = Classes.Employee("002", "Lenny", "Homer's boss")
print(lenny)
print("EXPECTED: 'ID: 002 NAME: Lenny JOB TITLE: Homer's boss " \
      "MANAGER: None")
print(carl.equals(lenny))
print("EXPECTED: 'False'")
smithers = Classes.Manager("101", "Smithers", "Burns' Assistant", "Mr. Burns", [carl.name, lenny.name])
print(smithers)
print("EXPECTED: 'ID: 101 NAME: Smithers Job Title: Burns' Assistant " \
      "MANAGER: Mr. Burns EMPLOYEES: Carl, Lenny")
homer = Classes.Employee("003", "Homer", "Idiot")
print(homer)
print("EXPECTED: ID: 003 NAME: Homer JOB TITLE: Idiot " \
      "MANAGER: None")
smithers.addEmployee(homer)
print(homer)
print("EXPECTED: ID: 003 NAME: Homer JOB TITLE: Idiot " \
      "MANAGER: Smithers")
grimes = Classes.Manager("102)", "Grimes", "Homer's temporary boss", "Smithers")
print(grimes)
print("EXPECTED: ID: 102 NAME: Grimes JOB TITLE: Homer's temporary " \
      "boss MANAGER: Smithers EMPLOYEES: None")
homer.setManager(grimes)
print(homer)
print("EXPECTED: ID: 003 NAME: Homer JOB TITLE: Idiot " \
      "MANAGER: Grimes")