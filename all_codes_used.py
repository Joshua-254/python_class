#Loops
i = 1;
while i<6:
  print(i)
  i += 1
# break statement
# stops executing the statement when the if break stateent is used
i = 1;
while i<6:
  if i == 3:
    break
  print(i)
  i += 1
#continue statement
# when the if condition is reached, it will not be executed bt then the program will be executed
i = 0
while i < 6:
  i +=1
  if i == 3:
    continue
  print(i)
# else statement
i = 1;
while i<6:
  print(i)
  i += 1
else:
  print("I is no longer less than 6")

# for loop
fruits = ["apple","mango","banana"]
for x in fruits:
  print(x)
  
# break statement 
print("\n Statement 1 ")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print(" \n Statement 2 ")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# Range function
print("\n Range Function \n ==============")
for x in range(2, 30 , 3):
  print(x)

# nested Loops
print("\n Nested Loops\n ==============")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

# Pass statement
print("\n Pass Statement \n ==============")
for x in [0,1,2]:
  pass
#  print(x)

# program to find the sum of all numbers stored in a list
numbers = [1,2,3,4,5,6,7,8]
# Python program to find sum of elements in list
sum = 0
# Iterate each element in numbers list
# and add them in variable sum
for x in range(0, len(numbers)):
    sum = sum + numbers[x]
 
# printing sum value
print("The sum is: ", sum)

# sample 2
numbers = [1,2,3,4,5,6,7,8]
sum = 0
for x in numbers:
  sum = sum + x
print("Sum = ", sum)

# question 2
print("\n Question 2 \n =========")
genre = ["pop","rock","jazz"]
for i in range(len(genre)):
  print("I like ", genre[i])