#1. Input student name and scores 
student_name = input("Enter student name: ")
score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: ")) 
score3 = float (input("Enter third score: "))

#2.  Calculate total and average 
total = score1 + score2 + score3
average = total / 3 

#3. Print results 
print("\n---Students Results ---")
print("Name:", student_name)
print("Total:", Total)
Print("Average:", average)

#4. Grade conditions 
if average >= 85:
  print("Grade: Excellent")
elif average >= 85:
  print("Grade: Very Good")
elif average >= 50:
  print("Grade: Passed")
else:
  print("Grade: Failed")
