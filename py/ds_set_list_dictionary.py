# Demonstrating Lists
print("List Example:")
shopping_list = ["Milk", "Bread", "Eggs", "Butter"]  # List of grocery items
shopping_list.append("Cheese")  # Adding an item
shopping_list.remove("Eggs")  # Removing an item
print("Shopping List:", shopping_list)
print("First Item:", shopping_list[0])  # Accessing elements by index
print()

# Demonstrating Sets
print("Set Example:")
unique_numbers = {10, 20, 30, 40, 50}  # A set of numbers (unordered, unique values)
unique_numbers.add(60)  # Adding an element
unique_numbers.remove(20)  # Removing an element
print("Set Elements:", unique_numbers)
print("Is 30 in the set?", 30 in unique_numbers)  # Checking existence
print()

# Demonstrating Dictionary
print("Dictionary Example:")
student_info = {
    "name": "Alice",
    "age": 20,
    "course": "Data Science"
}  # Key-Value pair representation

student_info["age"] = 21  # Updating a value
student_info["grade"] = "A"  # Adding a new key-value pair
print("Student Information:", student_info)
print("Student Name:", student_info["name"])  # Accessing value by key
print()
