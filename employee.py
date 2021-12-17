class Employee:
    def __init__(self, name, age, department, is_manager, rating, salary):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager
        self.rating = rating
        self.salary = salary
    pass
    def is_exellent(self):
        if self.rating >= 4.5:
            return True
        else:
            return False
    pass
    def bonus(self):
        if self.age >=50 and self.age <= 60 :
            self.salary += 500
            print("Salary increased to " + str(self.salary))
        else:
            print("no bonus added, salary is still " + str(self.salary))
    pass
pass
