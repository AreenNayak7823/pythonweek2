# Create
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Original list:", numbers)

# Read
index = int(input("Enter index to read: "))
print("Element at index", index, "is", numbers[index])

# Update
index = int(input("Enter index to update: "))
value = int(input("Enter new value: "))
numbers[index] = value
print("After update:", numbers)

# Delete
index = int(input("Enter index to delete: "))
del numbers[index]
print("After deletion:", numbers)
