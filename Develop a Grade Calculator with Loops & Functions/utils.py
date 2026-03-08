def calculate_average(grades):
    """Returns the average of a list of numbers (float)."""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def assign_letter_grade(avg):
    """Returns 'A', 'B', 'C', 'D', or 'F' based on standard grading scale."""
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def validate_grade(score):
    """Checks if input is numeric and between 0-100; returns valid float or raises ValueError."""
    try:
        val = float(score)
        if 0 <= val <= 100:
            return val
        else:
            raise ValueError("Grade must be between 0 and 100")
    except ValueError:
        raise ValueError("Invalid grade: must be a numeric value between 0 and 100")

def find_class_extremes(students):
    """Identify student(s) with highest and lowest averages."""
    if not students:
        return None, None
        
    highest_students = []
    lowest_students = []
    highest_avg = -float('inf')
    lowest_avg = float('inf')

    for name, grades in students.items():
        avg = calculate_average(grades)
        
        # Check for highest
        if avg > highest_avg:
            highest_avg = avg
            highest_students = [name]
        elif avg == highest_avg:
            highest_students.append(name)
            
        # Check for lowest
        if avg < lowest_avg:
            lowest_avg = avg
            lowest_students = [name]
        elif avg == lowest_avg:
            lowest_students.append(name)
            
    return highest_students, lowest_students
