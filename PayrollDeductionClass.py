#Write a class that represents a payroll deduction transaction. Each instance should have the 
# description, date, charge amount and employee ID as attributes. The class’s __init__ method 
# should accept an argument for each attribute. The class should have accessor methods for each 
# attribute. All attribute should be hidden.

class Transaction:
    def __init__(self, desc, date, charge, emp_ID):
        self.__trans_desc = desc
        self.__trans_date = date
        self.__charge = charge
        self.__emp_ID = emp_ID

    def get_desc(self):
        return self.__trans_desc
    def get_date(self):
        return self.__trans_date
    def get_charge(self):
        return self.__charge
    def get_emp_ID(self):
        return self.__emp_ID

        