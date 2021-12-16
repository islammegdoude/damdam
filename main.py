class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

pass


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        print(year)
    def welcoom(self):
        print("Welcoom",self.firstname, self.lastname,"to the class of", self.graduationyear)
pass

y = Student("islam", "Megdoude", 2020)
x = Person("salah eddine", "Megdoude")
y.welcoom()
"""
def myfunc(fname):
    print(fname + " islam")
    pass


myfunc("salah")
myfunc("megdoude")
myfunc("lamsi")

def myfunce(n):
  return lambda a : a * n

mydoubler = myfunce(2)
mytripler = myfunce(3)

print(mydoubler(11))
print(mytripler(11))

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
}

for x in thisdict.items():
    print(x)
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
}

print(myfamily)
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("***********")
for x in range(2, 30, 3):
    print(x)
print("*********")
for i in range(6):
    print(i)
else:
    print("islam ")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for i in [1, 2, 3]:
    pass
"""
