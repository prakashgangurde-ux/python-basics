# Student Report Card Generator
# Written by Prakash Gangurde

def get_grade(score):
    """Returns the letter grade for a given score."""
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def calculate_percentage(total, max_marks):
    """Calculates percentage from total marks obtained."""
    return round((total / max_marks) * 100, 2)


def get_remarks(percentage):
    """Returns remarks based on percentage."""
    if percentage >= 90:
        return "Outstanding"
    elif percentage >= 75:
        return "Excellent"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 40:
        return "Needs Improvement"
    else:
        return "Please seek academic support"


def print_report(name, scores):
    """Prints a formatted report card for the student."""
    subjects = ["Python", "Linux", "Web Dev", "Cybersecurity", "Database"]
    total = sum(scores)
    max_marks = len(subjects) * 100
    percentage = calculate_percentage(total, max_marks)
    remarks = get_remarks(percentage)

    print()
    print("=" * 40)
    print("       STUDENT REPORT CARD")
    print("=" * 40)
    print(f"Name       : {name}")
    print("-" * 40)

    for subject, score in zip(subjects, scores):
        grade = get_grade(score)
        print(f"{subject:<15} {score}/100     Grade: {grade}")

    print("-" * 40)
    print(f"Total      : {total}/{max_marks}")
    print(f"Percentage : {percentage}%")
    print(f"Remarks    : {remarks}")
    print("=" * 40)


# --- Main Program ---
print("=== Student Report Card Generator ===")
print()

name = input("Enter student name: ")

print(f"\nEnter marks out of 100 for {name}:")
scores = []

subjects = ["Python", "Linux", "Web Dev", "Cybersecurity", "Database"]
for subject in subjects:
    score = int(input(f"  {subject}: "))
    scores.append(score)

print_report(name, scores)