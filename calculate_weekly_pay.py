def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay


    total_pay = 0
    if hours_worked <= standard_hours:
        total_pay = hours_worked * regular_rate
    else:
        regular_pay = standard_hours * regular_rate
        overtime_hours = hours_worked - standard_hours
        overtime_pay = overtime_hours * overtime_rate
        
        total_pay = regular_pay + overtime_pay

    return total_pay
    
# # Code Example
overtime_pay = calculate_weekly_pay(36) # return 438 i.e, 438 in pounds per week.
print(overtime_pay)
