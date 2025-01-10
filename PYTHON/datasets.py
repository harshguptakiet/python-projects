my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.pop()
my_list.reverse()
print("List after operations:", my_list)

# 2. Tuple Operations
print("\nTuple Operations")
my_tuple = (10, 20, 30, 40, 50)
print("Count of 20:", my_tuple.count(20), "| Index of 30:", my_tuple.index(30))

# 3. String Operations
print("\nString Operations")
my_string = "Hello, World!"
print("Uppercase:", my_string.upper(), "| Replaced:", my_string.replace("World", "Python"))

# 4. Set Operations
print("\nSet Operations")
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)
print("Union:", my_set.union({4, 5, 6, 7, 8}))

# 5. Dictionary Operations
print("\nDictionary Operations")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
my_dict["age"] = 26
my_dict.pop("city")
print("Keys:", list(my_dict.keys()), "| Values:", list(my_dict.values()))