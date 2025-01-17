import json

# Define the data
data = {
    "Questions": [
        "1. What is used for exponentiation in Python?",
        "2. How is a list and a tuple different?",
        "3. What are the basic data types in Python?",
        "4. How do you declare a variable in Python?",
        "5. What will be the output, print(3 * 'a') ?"
    ],
    "A)": ["*", "Lists are immutable, tuples are mutable", "Integer, String, List, Tuple", "var x = 10", "aaa"],
    "B)": ["^", "Lists are ordered, tuples are unordered", "Integer, String, List, Boolean", "x := 10", "Error"],
    "C)": ["**", "Tuples are immutable, lists are mutable", "Integer, String, Set, Dictionary", "x = 10", "a3"],
    "D)": ["%", "None of the above", "Integer, String, Float, Boolean", "int x = 10", "a \"*\" 3]"]
}


with open('questions.json', 'w') as json_file:

    json.dump(data, json_file, indent=2)

