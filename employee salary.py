class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def display(self):
        print("Manager:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):
    def display(self):
        print("Developer:", self.name)
        print("Salary:", self.salary)


employees = [
    Manager("Arun", 50000),
    Developer("Anu", 45000)
]

for employee in employees:
    employee.display()
    print()
    