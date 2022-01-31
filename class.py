"""
ARITHMETIC OPERATORS

print(20//5)
print(21//5)
print(23//5)
print(24//5)
print(20//5)
print(21//5)
print(23//5)
print(25//5)
print(26//5)

"""
x = 50;
y = 5;

print("Arithmetic Operators \n :");
print("Addition: ", x + y);
print("Subtraction : ", x - y);
print("Multiplication : ", x * y);
print("Division: ", x / y);
print("Floor Division : ", x // y);
print("Modulous : ", x % y);
print("Exponent : ", x **y );

# program to check if a number is odd or even
print("Checking if a number is Odd or Even : \n")
number = int(input("Eneter a number :"));
#divisibility = number % 2;
if number % 2 == 0:
  print("Number is even");
else:
  print("NUmber is odd")

# program to check if a number is divisible by 5
five = int(input("Input the number"));
if five % 5 == 0 :
  print("Number is divisible by five");
else:
  print("Number isnt divisible by 5");

# program to check if a number is divisible by 5 and 7 

# Relational Operators
print("Relational Operators: ")
print(x > y);
print(x < y);
print(x == y);
print(x != y);
print(x >= y);
print(x <= y);

# program to give a 5 % bonus after buying goods worth 1000
print("# program to give a 5 % bonus after buying goods worth 1000 : \n");
item1 = int(input("Enter First Item : "))
item2 = int(input("Enter Second Item : "))
item3 = int(input("Enter Third Item : "))

total = item1 + item2 + item3;
if total >= 1000 :
  print("Total = ", total);
  print("5 % discount = ", 0.05 * total);
else :
  print("Discount  = ", 0);

# program to check if an individual's age is legible for voting
citizen = str(input("Enter the citizenship : ").lower());
print("=================\n");
age = int(input("Enter the age : "));
print("=================\n");

if citizen == "kenyan" and age >= 18:
  print("You are a legible voter");
  print("Proceed to vote: ")
elif citizen == "kenyan" and age < 18:
  print("You need to be above the age of 18 to be legible : ");
elif citizen != "kenyan" and age < 18:
  print("You need to be above the age of 18 and a Kenyan to be legible : ");
elif citizen != "kenyan" and age >= 18:
  print("You need to be a Kenyan to be legible : ");
else :
  print("Please check on the details Entered");

# membership operators
students = ["John", "Alice", "Alice", "Bob", "Jane"].lower();
if "john" in students:
  print("Present")
else :
  print("Absent")

"""
# if citizenship in county and age >=18
# country ["Kenya ", "Uganda" , "Tanzania"]
"""

# Assigmnemt operators
a = 5;
print ("a+=1 = a= a +1 = : ", a=+1);
