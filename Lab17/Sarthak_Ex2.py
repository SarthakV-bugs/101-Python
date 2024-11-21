def calculateGradePoint(grade):
    grade = grade.upper()
    if grade == 'A':
        return 4
    elif grade == 'B':
        return 3
    elif grade == 'C':
        return 2
    elif grade == 'D':
        return 1
    elif grade == 'F':
        return 0
    else:
        return 0

def calculateGPA():
    total_grade_points = 0
    for i in range(5):
        grade = input(f"Enter grade for subject {i+1} (A, B, C, D, F): ")
        grade_point = calculateGradePoint(grade)
        total_grade_points += grade_point
    gpa = total_grade_points / 5
    print(f"Grade Point Average: {gpa}")

def main():

    calculateGPA()

if __name__ == "__main__":
    main()