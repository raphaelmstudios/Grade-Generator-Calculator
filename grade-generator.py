# We are going to be creating a simple grade calculator that can calculate the GPA and the wieghted grades of different subjects
# A function for validating the grade if it meets the criteria
def valid_grade():
    while True:
        try : 
            grade = float(input("Enter your grade (0 - 100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("PLease enter a valid number")

# Function to validate if the category meets the criteria of 'FA' or 'SA'
def valid_category():
    while True:
        try:
            category = input("Enter category (FA/SA): ").upper()
            if category == "FA" or category == "SA":
                return category
            else:
                print("Invalid category.Please enter FA or SA")
        except ValueError:
            print("Invalid format. Please enter FA or SA")

# Function to validate if the weight for the grade is a positive
def valid_weight():
    while True:
        try:
            weight = float(input("Enter weight: "))
            if weight > 0:
                return weight
            else:
                print("Weight must be a positive value")
        except ValueError:
            print("Please enter a valid number")

# Creating an empty list to store all assignments
assignments = []
# A loop to ensure that we collect multiple assignments
while True:
    print("\n********Adding New Assignment********")
    
    #create a dictionary for this assignment
    assignment = {
        'name' : input("Enter assignment name: "),
        'category' : valid_category(),
        'grade' : valid_grade(),
        'weight' : valid_weight()
    }

    assignments.append(assignment)

    # Asks the user if they want to input another assignment
    while True:
        new_assignment = input("********Do you want to add another assignment?(y/n): ").lower()
        if new_assignment in ['yes', 'y']:
            break
        elif new_assignment in ['no', 'n']:
            break
        else:
            print("Invalid input.....please enter y or n")

    if new_assignment in ['no', 'n']:
        break

# Showing all the available assignments
print("\n********All Assignments********")
for assignment in assignments:
    name = assignment['name']
    grade = assignment['grade']
    weight = assignment['weight']
    category = assignment['category']
    
    print(f"{name}: grade={grade}, weight={weight}, category={category}")

# Calculating the weighted grade
print("\n********Calculating Grades********")
total_fa = 0
total_sa = 0

for assignment in assignments:
    name = assignment['name']
    grade = assignment['grade']
    weight = assignment['weight']
    category = assignment['category']

    weighted_grade = (grade / 100) * weight

    print(f"{name} ({category}): Weighted Grade = {weighted_grade}")
    if category == 'FA':
        total_fa = total_fa + weighted_grade  
    elif category == 'SA':
        total_sa = total_sa + weighted_grade  

print("\n********SUMMARY********")
print(f"Total Weighted Grade (Formative): {total_fa}")
print(f"Total Weighted Grade (Summative): {total_sa}")

# Calculating the Final grade
final_grade = total_fa + total_sa
print(f"Your final Grade is : {final_grade}")

# Calculating the GPA
GPA = final_grade /100 * 5
print(f"Your GPA is: {GPA:2f}")

# We are now going to input the pass/fail logic into the code
total_fa_weight = 0 
total_sa_weight = 0 

for assignment in assignments:
    weight = assignment['weight']
    category = assignment['category']
    
    if category == 'FA':
        total_fa_weight += weight  
    elif category == 'SA':
        total_sa_weight += weight  
print(f"\nTotal FA Weight: {total_fa_weight}")
print(f"Total SA Weight: {total_sa_weight}")

# Calculate the pass mark (50% of each)
fa_grade_required = total_fa_weight * 0.5
sa_grade_required = total_sa_weight * 0.5

# Check if student passes
if total_fa >= fa_grade_required and total_sa >= sa_grade_required:
    status = "PASS"
else:
    status = "FAIL"

print(f"\n********STATUS********")
print(f"FA: {total_fa}/{total_fa_weight} (Need {fa_grade_required} to pass)")
print(f"SA: {total_sa}/{total_sa_weight} (Need {sa_grade_required} to pass)")
print(f"Status: {status}")

#If the student fails, suggest which assignment to 
if status == 'FAIL':
    
    print("\n********RESUBMISSION RECOMMENDATION********")
    
    # Find the assignment with the lowest grade in failed categories
    lowest_assignment = None
    
    for assignment in assignments:
        # Check if this assignment's category failed
        if assignment['category'] == 'FA' and total_fa < fa_grade_required:
            # This is a failed FA assignment
            if lowest_assignment is None or assignment['grade'] < lowest_assignment['grade']:
                lowest_assignment = assignment
        
        elif assignment['category'] == 'SA' and total_sa < sa_grade_required:
            # This is a failed SA assignment
            if lowest_assignment is None or assignment['grade'] < lowest_assignment['grade']:
                lowest_assignment = assignment
    
    # Show recommendation
    if lowest_assignment:
        print(f"Recommendation: Resubmit '{lowest_assignment['name']}'")
        print(f"Current grade: {lowest_assignment['grade']}%")
# Creating the csv file

import csv
with open('grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Assignment', 'Category', 'Grade', 'Weight'])
    
    for assignment in assignments:
        name = assignment['name']
        grade = assignment['grade']
        weight = assignment['weight']
        category = assignment['category']
        
        writer.writerow([name, category, grade, weight])  

print("\n********Data exported to grades.csv********")








