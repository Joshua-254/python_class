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