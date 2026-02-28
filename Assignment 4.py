"""
Assignment 4: Module 5 - Files, Exceptions, and Errors in Python
Task 1: Read a File and Handle Errors
Task 2: Write and Append Data to a File
"""

# Task 1: Read a File and Handle Errors
print("=" * 50)
print("TASK 1: Read a File and Handle Errors")
print("=" * 50)

try:
    with open('sample.txt', 'r') as file:
        print("File content:")
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n")

# Task 2: Write and Append Data to a File
print("=" * 50)
print("TASK 2: Write and Append Data to a File")
print("=" * 50)

try:
    # Get user input
    user_input = input("Enter data to write to the file: ")
    
    # Write data to file
    with open('output.txt', 'w') as file:
        file.write(f"Initial data: {user_input}\n")
    
    print("Data written to 'output.txt'")
    
    # Append additional data to the file
    additional_data = input("Enter additional data to append: ")
    with open('output.txt', 'a') as file:
        file.write(f"Appended data: {additional_data}\n")
    
    print("Data appended to 'output.txt'")
    
    # Read and display the final content
    print("\nFinal content of 'output.txt':")
    with open('output.txt', 'r') as file:
        content = file.read()
        print(content)
    
except FileNotFoundError:
    print("Error: The file could not be created or found.")
except IOError as e:
    print(f"IO Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("=" * 50)
print("Assignment 4 completed!")
print("=" * 50)
