def checkList(l, index):
    try:
        print(f"Element at index {index}: {l[index]}")
    except IndexError:
        print(f"Error: Index {index} is out of range.")
    except TypeError:
        print("Error: The first argument must be a list.")


# Test

print("Test1: Number and index")
numbers = [10, 20, 30, 40, 50]
checkList(numbers, 2)

print("Test2: String input and index")
checkList("Sarthak", 5)

print("Test3: Boolean and index")
checkList(True, 0)

print("Test4: String and invalid index")
checkList("LABWORK", 5)
checkList('something', 20)
