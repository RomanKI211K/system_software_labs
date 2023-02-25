file_path = input("Enter path to your file: ")

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line_index, line in enumerate(lines):
            file.write(f'{line_index + 1}: {line}')

    print("File successfully edited!")
except FileNotFoundError:
    print("File not found. Please, try again.")
except PermissionError:
    print("Permission denied to write to file. Please, try again with appropriate permissions.")
except Exception as e:
    print("An error occurred:", e)