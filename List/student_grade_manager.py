# Student Grade Manager
# Written by Prakash Gangurde

def add_student(students, name, scores):
    """Add a new student with their scores to the list."""
    students.append({
        "name": name,
        "scores": scores
    })


def calculate_average(scores):
    """Calculate the average of a list of scores."""
    return round(sum(scores) / len(scores), 2)


def get_grade(average):
    """Return a letter grade based on the average score."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def get_top_performers(students, n=3):
    """Return the top N students based on average score."""
    ranked = sorted(
        students,
        key=lambda student: calculate_average(student["scores"]),
        reverse=True
    )
    return ranked[:n]


def display_report(students):
    """Display a formatted report for all students."""

    print()
    print("=" * 55)
    print(f"{'STUDENT GRADE REPORT':^55}")
    print("=" * 55)
    print(f"{'Name':<20} {'Average':>10} {'Grade':>8} {'Status':>12}")
    print("-" * 55)

    passing = []
    failing = []

    for student in students:
        name = student["name"]
        scores = student["scores"]

        average = calculate_average(scores)
        grade = get_grade(average)
        status = "Pass" if average >= 40 else "Fail"

        print(f"{name:<20} {average:>10} {grade:>8} {status:>12}")

        if average >= 40:
            passing.append(name)
        else:
            failing.append(name)

    print("=" * 55)
    print(f"\nTotal students : {len(students)}")
    print(f"Passing        : {len(passing)}")
    print(f"Failing        : {len(failing)}")

    # Display the actual top performer
    if students:
        top_student = max(
            students,
            key=lambda student: calculate_average(student["scores"])
        )
        top_average = calculate_average(top_student["scores"])

        print(f"\nTop performer  : {top_student['name']} ({top_average})")

    if failing:
        print(f"\nNeeds support  : {', '.join(failing)}")


# ---------------- Main Program ----------------

students = []

subjects = (
    "Python",
    "Linux",
    "Web Dev",
    "Security",
    "Database"
)

print("=" * 55)
print(f"{'STUDENT GRADE MANAGER':^55}")
print("=" * 55)

num_students = int(input("\nHow many students? "))

for i in range(num_students):
    print(f"\nStudent {i + 1}")

    name = input("  Name: ")

    scores = []

    for subject in subjects:
        score = int(input(f"  {subject} score (0-100): "))
        scores.append(score)

    add_student(students, name, scores)

display_report(students)

print("\n--- Top 3 Performers ---")

top_students = get_top_performers(students)

for rank, student in enumerate(top_students, start=1):
    average = calculate_average(student["scores"])
    print(f"{rank}. {student['name']} — Average: {average}")