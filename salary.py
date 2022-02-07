salary = int(input("Enter the salary " ))
period = int(input( "Enter the years of servce :"))
if period > 10 :
  total_salary_bonus =  salary + (0.1 * salary)
  print("The total salary bonus is : ",total_salary_bonus)
elif period >= 6 and period <=10 :
  total_salary_bonus =  salary + (0.08 * salary)
  print("The total salary bonus is : ", total_salary_bonus)
else :
  total_salary_bonus =  salary + (0.05 * salary)
  print("The total salary bonus is : ",total_salary_bonus)
