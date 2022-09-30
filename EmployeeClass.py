#Write a class named Employee that holds the following data about an employee in attributes: 
# name, ID number, department, job title and monthly salary.The Employee class’s __init__ method 
# should accept an argument for each attribute. The Employee class should have accessor methods 
# for each attribute. All attribute should be hidden.

class Employee:
    #initialize class
    def __init__(self, name, id, dept, job, salary):
        self.__name = name
        self.__id = id
        self.__dept = dept
        self.__job = job
        self.__salary = salary
    
    #individual attributes
    def emp_name(self):
        return self.__name
        
    def emp_id(self):
        return self.__id

    def emp_dept(self):
        return self.__dept

    def emp_job(self):
        return self.__job
        
    def emp_salary(self):
        return self.__salary

        