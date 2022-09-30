#Write a class that represents a payroll deduction transaction. Each instance should have the 
# description, date, charge amount and employee ID as attributes. The class’s __init__ method 
# should accept an argument for each attribute. The class should have accessor methods for each 
# attribute. All attribute should be hidden.

class Transaction:
    def __init__(self, desc, date, charge, id):
        self.__desc = desc
        self.__date = date
        self.__charge = charge
        self.__id = id

    def get_desc(self):
        return self.__desc

    def get_date(self):
        return self.__date

    def get_charge(self):
        return self.__charge

    def get_id(self):
        return self.__id

        