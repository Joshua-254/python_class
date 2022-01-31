# assignment exercise
# python program to compare the height of thre students and return the tallest of the three

print("Enter the height of the students to check on the heights: ");
student1_name = input("Enter the name: ");
student1_height = int(input("Enter the height"));

student2_name = input("Enter second student: ");
student2_height = int(input("Enter the height"));

student3_name = input("Enter the name: ");
student3_height = int(input("Enter the height"));

if student1_height > student2_height and student1_height > student3_height:
  print(student1_name , student1_height,  "\n");
  print(student2_name , student2_height,  "\n");
  print(student3_name , student3_height,  "\n");
  print(" The tallest is ", student1_name, "\n");
elif student2_height > student1_height and student2_height > student3_height:
  print(student1_name , student1_height,  "\n");
  print(student2_name , student2_height,  "\n");
  print(student3_name , student3_height,  "\n");
  print(" The tallest is ", student2_name, "\n");
elif student3_height > student1_height and student3_height > student2_height:
  print(student1_name , student1_height,  "\n");
  print(student2_name , student2_height,  "\n");
  print(student3_name , student3_height,  "\n");
  print(" The tallest is ", student3_name, "\n");
else :
  print("Enter the correct details for the check.");