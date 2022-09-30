#Write a program that will create the following employees (Table 1) as well as the payroll deductions (Table 2):

import EmployeeClass as ec
import PayrollDeductionClass as pdc

def main():  

    #create employee
    employee = ec.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)

    #initialize transactions
    transaction1 = pdc.Transaction('Food Court', '8/14/2022', 22.50, 39119)
    transaction2 = pdc.Transaction('Gift Contribution', '8/12/2022', 25.00, 58475)
    transaction3 = pdc.Transaction('Food Court', '8/17/2022', 15.25, 21547)
    transaction4 = pdc.Transaction('Vending Machine', '8/22/2022', 3.00, 58475)
    transaction5 = pdc.Transaction('Vending Machine', '8/5/2022', 2.75, 58475)

    transactions = [transaction1, transaction2, transaction3, transaction4, transaction5]
   
    #display employee info
    print('\n*** Employee Pay ***')
    print('Name:', ec.Employee.emp_name(employee).title())
    print('ID:', ec.Employee.emp_id(employee))
    print('Department:', ec.Employee.emp_dept(employee))
    print('Job Title:', ec.Employee.emp_job(employee))
    print('Gross Pay:', '${:0,.2f}'.format(ec.Employee.emp_salary(employee)), sep = ' ')

    #display employee transactions
    
    deduction = 0
    for record in transactions:
        if record.get_id() == employee.emp_id():
            deduction = deduction + record.get_charge()

    pay = employee.emp_salary() - deduction

    #display net pay    
    print('Net Pay:', '${:0,.2f}'.format(pay, '<5,.2f'), sep = ' ')

#for loop through table 2, hardcode

main() 