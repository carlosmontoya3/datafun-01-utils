'''
This module provides a reusable byline for KC Sports Analytics 
Last updated 1.14.2024 '''

import math
import statistics

def main(): #The function that will display byline
    print(byline)
    
#Define Variables
company_name: str = "KC Sports Analytics"
count_employees: int = 20
has_internship_opportunity: bool = True
average_employee_statisfaction: float = 4.86
pro_teams: list = ["Chiefs", "Royals", "Sporting KC", "Current"]
stadium_capacity: list = [76416,37903,18467,11500]

#f-strings from variables
count_employees_string: str = f"There are {count_employees} employees currently on our team."
has_internship_string: str = f"Do we have available internships? {has_internship_opportunity}"
employee_statisfaction_string = f"Our average employee satisfaction score is {average_employee_statisfaction} out of 5."
pro_teams_string: str = f"There are {len(pro_teams)} professional teams in Kansas City."

#Calculation of statistics
lowest = min(stadium_capacity)
highest = max(stadium_capacity)
total = sum(stadium_capacity)
mean = statistics.mean(stadium_capacity)
standard_deviation = statistics.stdev(stadium_capacity)

#Formatted Byline string
byline: str = f"""
{company_name}
{count_employees_string}
{employee_statisfaction_string}
{has_internship_string}
{pro_teams_string}
Max stadium capacity: {highest}
Average stadium capacity: {mean}
"""

#Execute main function
if __name__ == "__main__":
    main()
