import csv

filename = "students.csv"

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, marks])
    print("Student added successfully!")

def view_students():
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_student():
    roll = input("Enter roll number to search: ")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == roll:
                print("Found:", row)
                return
    print("Student not found!")

def delete_student():
    roll = input("Enter roll number to delete: ")
    rows = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row[1] != roll]
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Student deleted successfully!")

# Menu
while True:
    print("\n1. Add  2. View  3. Search  4. Delete  5. Exit")
    choice = input("Enter choice: ")
    if choice == '1': add_student()
    elif choice == '2': view_students()
    elif choice == '3': search_student()
    elif choice == '4': delete_student()
    elif choice == '5': break
