# ----------------ERROR HANDLING------------------

# Some usual errors:

# FilenotFoundError
# with open("not_existing_file.txt") as file:
#     file.read()

# KeyError
# dictionary = {"key": "value"}
# dictionary["not_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Orange"]
# fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")




