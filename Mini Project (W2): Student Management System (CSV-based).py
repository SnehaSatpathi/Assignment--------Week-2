
import csv

filename = "students.csv"

def add_student(name, marks, roll):
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, marks, roll])
    print("Student added!")

def delete_student(roll):
    rows = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[2] != roll:
                rows.append(row)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Student deleted!")

def search_student(roll):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[2] == roll:
                print("Student found:", row)
                return
    print("Student not found!")

# Example usage
add_student("Sneha", 85, "101")
add_student("Ravi", 90, "102")
search_student("101")
delete_student("102")
