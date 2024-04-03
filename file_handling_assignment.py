# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Line 1: Hello, World!\n")
        file.write("Line 2: This is a test file.\n")
        file.write("Line 3: 42 is the answer to everything.\n")
        print("File 'my_file.txt' created and written successfully.")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File content:\n" + content)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File reading process completed.\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Appending additional content.\n")
        file.write("Line 5: Python is fun!\n")
        file.write("Line 6: 3.14 is a mathematical constant.\n")
        print("Additional content appended to 'my_file.txt'.")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File appending process completed.")
