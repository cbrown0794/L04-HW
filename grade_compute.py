# grade_compute.py

def gradeToNumber(grade):
    """
    Converts a letter grade to a number using standard 4.0 scale logic.
    Constraints: No dictionaries allowed.
    """
    grade = grade.upper().strip()
    
    if grade == 'F':
        return 0.0
    
    # Base value determination
    score = 0.0
    if grade.startswith('A'):
        score = 4.0
    elif grade.startswith('B'):
        score = 3.0
    elif grade.startswith('C'):
        score = 2.0
    elif grade.startswith('D'):
        score = 1.0
    else:
        return 0.0 # Default for F or invalid
        
    # Modifier determination
    if '+' in grade:
        score += 0.3
    elif '-' in grade:
        score -= 0.3
        
    return score

def numberToGrade(score):
    """
    Converts a numeric score back to a letter grade.
    """
    if score >= 4.0: return 'A' # Cap at A for output aesthetic, or A+ if preferred
    elif score >= 3.7: return 'A-'
    elif score >= 3.3: return 'B+'
    elif score >= 3.0: return 'B'
    elif score >= 2.7: return 'B-'
    elif score >= 2.3: return 'C+'
    elif score >= 2.0: return 'C'
    elif score >= 1.7: return 'C-'
    elif score >= 1.3: return 'D+'
    elif score >= 1.0: return 'D'
    else: return 'F'

def validateInput(input_list):
    """
    Validates that we have exactly 4 items and they are valid grades.
    """
    if len(input_list) != 4:
        print("Error: You must enter exactly 4 grades separated by '$'.")
        return False
        
    valid_chars = ['A', 'B', 'C', 'D', 'F']
    for item in input_list:
        clean_item = item.strip().upper()
        if len(clean_item) == 0:
            return False
        # Check first character is a valid letter
        if clean_item[0] not in valid_chars:
            print(f"Error: '{item}' is not a valid grade.")
            return False
            
    return True

def processGrades(grade_list):
    """
    Main logic to convert, drop lowest, apply curve, and average.
    Returns: (lowest_grade_letter, average_score, final_letter_grade)
    """
    # Convert all to numbers
    num_grades = []
    for g in grade_list:
        num_grades.append(gradeToNumber(g))
        
    # Find and drop lowest
    # (Without using min() if we want to be strictly manual, but min() is standard function)
    lowest_val = min(num_grades)
    num_grades.remove(lowest_val) # Removes only the first occurrence
    
    # Calculate Average of remaining 3
    avg = sum(num_grades) / 3.0
    
    # CONSTRAINT 4: Weighted Logic / Curve Bonus
    # "if the remaining three grades are below 'B-' or lower"
    # B- is 2.7. So if ALL remaining grades are <= 2.7
    apply_curve = True
    for grade in num_grades:
        if grade > 2.7: # If any grade is higher than B-
            apply_curve = False
            break
            
    if apply_curve:
        avg += 0.25
        print("\n(Notice: Curve Bonus of +0.25 applied!)")

    return numberToGrade(lowest_val), avg, numberToGrade(avg)