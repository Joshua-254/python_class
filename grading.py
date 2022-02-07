# Grding system
print("\n Grading system")
subject_1 = int(input("Enter first subject Score : "))
subject_2 = int(input("Enter Second subject Score : "))
subject_3 = int(input("Enter Third subject Score : "))
subject_4 = int(input("Enter Fourth subject Score : "))
subject_5 = int(input("Enter Fifth subject Score : "))

subject_total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5

subject_mean = subject_total / 5

if subject_mean >= 70 and subject_mean <= 100 :
  print(subject_mean,"\n")
  print("Grade is A")
elif subject_mean >= 60 and subject_mean <= 69 :
  print(subject_mean,"\n")
  print("Grade is B")
elif subject_mean >= 50 and subject_mean <= 59 :
  print(subject_mean,"\n")
  print("Grade is C")
elif subject_mean >= 40 and subject_mean <= 49 :
  print(subject_mean,"\n")
  print("Grade is D")
elif subject_mean >= 0 and subject_mean <= 39 :
  print(subject_mean,"\n")
  print("Grade is Fail")
else :
  print("Enter a valid mark")
  