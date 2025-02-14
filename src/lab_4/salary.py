"""
    Calculate the salary of an employee of a company in terms of the basic pay,
    dearness allowance (DA), and house rent allowance (HRA). The DA and HRA
    are set as a certain percentage of the basic pay.
    Further, the company deducts 12% of the basic pay for PF.
    Compute the salary that would be received by an employee given the basic pay,
    percentage of basic pay for DA, and percentage of basic pay for HRA and print it,
    rounded off to the nearest integer. (Salary = Basic Pay + DA + HRA - PF)
"""

def calculate_salary(basic_pay, da_percentage, hra_percentage):
    da = (da_percentage / 100) * basic_pay
    hra = (hra_percentage / 100) * basic_pay
    pf = 0.12 * basic_pay
    salary = basic_pay + da + hra - pf
    return round(salary)

def main():
    basic_pay = float(input("Enter basic pay: "))
    da_percentage = float(input("Enter percentage of basic pay for DA: "))
    hra_percentage = float(input("Enter percentage of basic pay for HRA: "))
    salary = calculate_salary(basic_pay, da_percentage, hra_percentage)
    print(f"The salary of the employee is: {salary}")

if __name__ == "__main__":
    main()
