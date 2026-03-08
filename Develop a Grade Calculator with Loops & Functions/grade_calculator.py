import utils

def main():
    print("Welcome to the Modular Grade Calculator!")
    print("----------------------------------------")
    
    students = {}

    while True:
        name = input("\nEnter student name (or press Enter to finish): ").strip()
        if not name:
            break

        grades = []
        print(f"Enter 3 grades for {name}:")
        
        for i in range(1, 4):
            while True:
                score_str = input(f" Grade {i}: ").strip()
                try:
                    # Validate the grade input using our utility function
                    valid_score = utils.validate_grade(score_str)
                    grades.append(valid_score)
                    break  # Valid input, break out of the while loop
                except ValueError as e:
                    print(f"   Error: {e}")
        
        # Store the list of valid grades in the dictionary under the student's name
        students[name] = grades

    # Check if any students were added
    if not students:
        print("\nNo student data was entered. Exiting program.")
        return

    # Generate the Final Report
    print("\n" + "="*50)
    print(" " * 15 + "Final Grade Report")
    print("="*50)
    
    # Use string formatting for clean alignment
    print(f"{'Name':<20} | {'Average':<10} | {'Letter Grade'}")
    print("-" * 50)
    
    for name, grades in students.items():
        # Compute average and letter grade
        avg = utils.calculate_average(grades)
        letter_grade = utils.assign_letter_grade(avg)
        
        # Print row in table
        print(f"{name:<20} | {avg:<10.2f} | {letter_grade}")
    print("-" * 50)

    # Bonus: Identify class extremes
    highest_students, lowest_students = utils.find_class_extremes(students)
    
    if highest_students and lowest_students:
        print("\n--- Class Extremes ---")
        
        highest_names = ", ".join(highest_students)
        highest_avg = utils.calculate_average(students[highest_students[0]])
        print(f"Highest Average: {highest_names} ({highest_avg:.2f})")
        
        lowest_names = ", ".join(lowest_students)
        lowest_avg = utils.calculate_average(students[lowest_students[0]])
        print(f"Lowest Average:  {lowest_names} ({lowest_avg:.2f})")
        
    print("\nThank you for using the Grade Calculator!")

if __name__ == "__main__":
    main()
