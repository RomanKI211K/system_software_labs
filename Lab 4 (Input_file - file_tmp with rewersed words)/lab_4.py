import os

file_name = input("Enter the name of the file: ")
found_file = False

for root, dirs, files in os.walk("."):
    if file_name in files:
        file_path = os.path.join(root, file_name)
        found_file = True
        break

if not found_file:
    print("File not found. Please try again.")
else:
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            tmp_file_path = os.path.splitext(file_path)[0] + ".tmp"
            with open(tmp_file_path, 'w') as tmp_file:
                for line in lines:
                    new_line = []
                    for word in line.split():
                        new_line.append(word[::-1])
                    new_line = " ".join(new_line)

                    tmp_file.write(new_line + "\n")

        print("File successfully edited!")

    except PermissionError:
        print("Permission denied to write to file. Please, try again with appropriate permissions.")
    except Exception as e:
            print("An error occurred:", e)
