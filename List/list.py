# Modifying List Items

print("=" * 55)
print(f"{'Modify items':^55}")
print("=" * 55)

students = ["Prakash", "Rahul", "Priya"]
students[1] = "Ravi"
print(students)    # ['Prakash', 'Ravi', 'Priya']

# Add items

print("=" * 55)
print(f"{'Add items':^55}")
print("=" * 55)


students = ["Prakash", "Rahul"]

# append() — adds to the end
students.append("Priya")
print(students)    # ['Prakash', 'Rahul', 'Priya']

# insert() — adds at a specific position
students.insert(1, "Anil")
print(students)    # ['Prakash', 'Anil', 'Rahul', 'Priya']

# Remove items

print("=" * 55)
print(f"{'Remove items':^55}")
print("=" * 55)


students = ["Prakash", "Rahul", "Priya", "Anil"]

# remove() — removes by value
students.remove("Rahul")
print(students)    # ['Prakash', 'Priya', 'Anil']

# pop() — removes by index (default: last item)
students.pop()
print(students)    # ['Prakash', 'Priya']

students.pop(0)
print(students)    # ['Priya']

# clear() — removes everything
students.clear()
print(students)    # []