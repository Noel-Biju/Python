employees=[
    ("joel","cse",12000),
    ("james","ad",8000),
    ("shaju","ec",15000),
    ("biju","cse",9000)
]
salary_threshold=10000
total_annual_expense=0
for employee in employees:
    employee_name,department,monthly_salary=employee
    if monthly_salary>salary_threshold:
        print(employee)
    total_annual_expense+=monthly_salary
print(f"The total annual payroll expense is {total_annual_expense}")
