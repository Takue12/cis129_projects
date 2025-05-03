#Brendon Mandizvidza 
#05/02/2025
# Execercise  9.2 Class Average reading grades from a plain text file


import csv

with open('grades.csv', 'a', newline='') as csvfile:
    gradewriter = csv.writer(csvfile)
    
    while True:
        firstname = input("Enter student's first name (or 'done' to finish): ")
        if firstname.lower() == 'done':
            break
        print(f'{"firstname":<10}{"Name":<10}{"exam":>10}')
        lastname = input("Enter student's last name: ")
        exam1 = int(input("Enter exam 1 grade: "))
        exam2 = int(input("Enter exam 2 grade: "))
        exam3 = int(input("Enter exam 3 grade: "))
        
        gradewriter.writerow([firstname, lastname, exam1, exam2, exam3])

print(" records saved to grades.csv")



