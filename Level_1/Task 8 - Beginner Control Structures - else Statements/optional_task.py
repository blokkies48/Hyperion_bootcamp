#Asking user to state employee type
employee = input("Enter 1 for salesperson and enter 2 for manager: ")

#Statements to calculate salaries and setting employee variable to the employee type.
if employee == "1":
    employee = "Salesperson"
    salary = 2000.00
    ##
    sales = float(input("What is the total gross sales amount: "))
    salary += (sales * 0.08)
else:
    employee = "Manager"
    #Setting rate and normal hours in variable so it can be changed throughout the code easliy if it changes
    hourly_rate = 40
    this_month_normal_hours = 160
    ##
    hours = float(input("How many hours did you work: "))
    salary = hourly_rate * hours

    #Added overtime just for fun
    if hours > this_month_normal_hours:
        salary = (hourly_rate * this_month_normal_hours) + ((hourly_rate * 1.5) * (hours - this_month_normal_hours)) 

#Printing salary rounded to 2 decimal place and employee type 
print(f"{employee}: gross salary is: R{round(salary, 2)}")