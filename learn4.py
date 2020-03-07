import PyMySQL

class Employe:

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employe.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employe.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

emp1 = Employe("Zara", 2700)
emp2 = Employe("Manni", 3000)

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee %d" % Employe.empCount)