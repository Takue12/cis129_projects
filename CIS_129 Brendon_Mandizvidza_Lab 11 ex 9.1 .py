#Brendon Mandizvidza 
#05/02/2025
# Execercise  9.2 Class Average reading grades from a plain text file


# Read grades from grade .txt  file and calculate statistics
with open('grades.txt', 'r') as f:
    # Read all grades from grade.txt file and float them
    grades = [float(line) for line in f] 
# Calculations 
total = sum(grades)      # add all grades
count = len(grades)      #number of grades
average = total / count  # Average grade

# Display results
print("Grades:", grades)  # Show all individual grades
print("Total:", total)    # Show sum of grades
print("Count:", count)    # Show number of grades
print("Average:", average) # Show calculated average