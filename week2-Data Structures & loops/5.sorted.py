n = int(input("Enter number of students: "))
students = []

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    score = int(input(f"Enter score of {name}: "))
    students.append({"name": name, "score": score})

students.sort(key=lambda x: x["score"], reverse=True)
print("Sorted by score (descending):")
for s in students:
    print(s["name"], "-", s["score"])
