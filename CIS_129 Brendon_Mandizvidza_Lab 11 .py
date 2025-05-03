#Brendon Mandizvidza 
#05/02/2025
#Module 11 excercises 9.1-9.3

import csv
# Open file for writing
with open('grades.txt', 'w') as file:
    print("Enter grades (enter done to stop):")
    while True:
        grade = input("Grade: ")
        if grade.lower() == "done":
            break                # Exit if done is entered
        
        file.write(f"{grade}\n") # Write grade to file

# Display results
print("Grades saved to grades.txt")


# Execercise  9.2 Class Average reading grades from a plain text file
# Read grades from grade .txt  file and calculate statistics
with open('grades.txt', 'r') as f:
    # Read all grades from grade.txt file and float them
    grades = [float(line) for line in f] 
# Calculations 
total = sum(grades)         # add all grades
count = len(grades)         #number of grades
average = total / count     # Average grade

# Display results
print("Grades:", grades)    # Show all individual grades
print("Total:", total)      # Show sum of grades
print("Count:", count)      # Show number of grades
print("Average:", average)  # Show calculated average

# Execercise  9.3 Class Averagewriting students records to CSV file
with open('grades.csv', 'a', newline='') as csvfile:
    gradewriter = csv.writer(csvfile)
    
    while True:
        firstname = input("Enter student's first name (or 'done' to finish): ")
        if firstname.lower() == 'done':
            break
        lastname = input("Enter student's last name: ")
        exam1 = int(input("Enter exam 1 grade: "))
        exam2 = int(input("Enter exam 2 grade: "))
        exam3 = int(input("Enter exam 3 grade: "))
        
        gradewriter.writerow([firstname, lastname, exam1, exam2, exam3])

print(" records saved to grades.csv")



