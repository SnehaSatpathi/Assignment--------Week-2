#Create a list and perform CRUD operations
# Create
my_list = [10, 20, 30]
print("Initial list:", my_list)

# Read
print("First element:", my_list[0])

# Update
my_list[1] = 25
print("Updated list:", my_list)

# Delete
del my_list[2]
print("After deletion:", my_list)



# Dictionary program to count word frequency
text = "python is easy and python is powerful"
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word frequency:", freq)


# Use nested loops to print a pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()




# Find largest and smallest number in a list
numbers = [12, 45, 2, 67, 34, 89, 1]

largest = max(numbers)
smallest = min(numbers)

print("Largest:", largest)
print("Smallest:", smallest)




# Sort a list using sort() and lambda key
students = [("Sneha", 72), ("Ravi", 85), ("Anita", 65)]

# Sort by marks
students.sort(key=lambda x: x[1])
print("Sorted by marks:", students)

# Sort by name
students.sort(key=lambda x: x[0])
print("Sorted by name:", students)


