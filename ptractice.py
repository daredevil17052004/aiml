# List: Iterating over a list and performing operations
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)

# Dictionary: Accessing keys and values
person = {
    "name": "Alice",
    "age": 30,
    "profession": "Engineer"
}

# Accessing dictionary keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Set: Using sets for unique data handling
data = [1, 2, 2, 3, 4, 4, 5]
unique_data = set(data)

print("Original data:", data)
print("Unique data:", unique_data)

# Set operations example
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# Intersection
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

# Difference
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b:", difference_set)
