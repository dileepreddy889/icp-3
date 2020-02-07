class Employee():
    employeeCount =0
    salary =0
    def __init__(self,name,family,salary,department):
        self.name=name
        self.family=family
        Employee.salary+=salary
        self.department=department
        Employee.employeeCount=Employee.employeeCount+1
    def printAllEmployees(self):
        print('Name: '+self.name+' Family: '+self.family+' Department: '+self.department)

    def averageSalary(self):
        self.avgSalary=Employee.salary/Employee.employeeCount
        print ('The average salary of the employees is')
        print (self.avgSalary)

class FullTimeEmployee(Employee):
    def __init__(self):
        Employee.averageSalary(self)



e1=Employee('Dileep','P',5000,'Software')
e1.printAllEmployees()

e2=Employee('raj','l',4000,'Accounting')
e2.printAllEmployees()

e3=Employee('rajeem','l',4000,'artist')
e3.printAllEmployees()

f=FullTimeEmployee()