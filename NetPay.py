#Write a program that will create the following employees (Table 1) as well as the payroll deductions (Table 2):

import EmployeeClass as ec
import PayrollDeductionClass as pdc

def main():
    employee = create_employee()
    transactions = enter_transactions()
    display_pay(employee, transactions)

def create_employee():
    #initialize employee attributes
    emp_ID = 58475
    employee_name = 'Jimmy Smith'
    department =  'Information Systems'
    job_title = 'Developer'
    monthly_salary = 6800
    
    #create employee
    employee = ec.Employee(emp_ID, employee_name, department, job_title, monthly_salary)
    return employee


def enter_transactions():
    #initialize transactions
    transaction1 = pdc.Transaction('Food Court', '8/14/2022', 22.50, 39119)
    transaction2 = pdc.Transaction('Gift Contribution', '8/12/2022', 25.00, 58475)
    transaction3 = pdc.Transaction('Food Court', '8/17/2022', 15.25, 21547)
    transaction4 = pdc.Transaction('Vending Machine', '8/22/2022', 3.00, 58475)
    transaction5 = pdc.Transaction('Vending Machine', '8/5/2022', 2.75, 58475)

    transactions = [transaction1, transaction2, transaction3, transaction4, transaction5]

    return transactions


def display_pay(employee, transactions):
   
    #display employee Info
    print('\n*** Employee Pay ***')
    print('Name:', ec.Employee.get_name(employee).title())
    print('ID:', ec.Employee.get_ID(employee))
    print('Department:', ec.Employee.get_dept(employee))
    print('Job Title:', ec.Employee.get_job(employee))
    print('Gross Pay:', '${:0,.2f}'.format(ec.Employee.get_salary(employee)), sep = ' ')

    #display employee transactions
    i = 0
    total = 0.0
    for row in transactions:
        if transactions[i].get_emp_ID() == employee.get_ID():
            transaction = transactions[i].get_desc()
            date = transactions[i].get_date()
            charge = transactions[i].get_charge()
            print()
            print('Transaction:', transaction)
            print('Date:', date)
            print('Charge: $', format(charge, '<5,.2f'), sep = '')
            print()
            total += charge
            i += 1

    #display net pay    
    print('Net Pay:', '${:0,.2f}'.format(total, '<5,.2f'), sep = ' ')




main() 