# letter_grade_avg.py
import grade_compute as gc

def main():
    print("------------------------------------------------")
    print("      Welcome to the Grade Calculator")
    print("Enter 4 grades separated by '$' (e.g. A$ B+$ C$ A-)")
    print("------------------------------------------------")

    while True:
        user_input = input("\nEnter grades (or 'q' to quit): ")
        
        # Check for quit
        if user_input.strip().lower() == 'q':
            print("Exiting program...")
            break
            
        # CONSTRAINT 3: Split by Dollar Sign
        raw_grades = user_input.split('$')
        
        # Clean whitespace from split parts
        cleaned_grades = []
        for g in raw_grades:
            cleaned_grades.append(g.strip())
            
        # CONSTRAINT 2: Input Validation
        if gc.validateInput(cleaned_grades):
            
            # Process the grades
            lowest_letter, avg_num, final_letter = gc.processGrades(cleaned_grades)
            
            # Format raw input for display (e.g., "A, B+, C, A")
            formatted_input = ", ".join(cleaned_grades).upper()
            
            # CONSTRAINT 5: ASCII Box Output (40 chars wide)
            print("-" * 40)
            print(f"|{'GRADE REPORT SUMMARY':^38}|")
            print("-" * 40)
            print(f"| Grades Entered: {formatted_input:<20} |") # Adjust spacing as needed
            print(f"| Lowest Grade Dropped: {lowest_letter:<14} |")
            print(f"| Calculated Average:   {avg_num:<14.2f} |")
            print(f"| Final Letter Grade:   {final_letter:<14} |")
            print("-" * 40)

if __name__ == "__main__":
    main()