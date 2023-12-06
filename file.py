import os
import shutil

from_dir = "C:/Users/Smart/Desktop/sample 111"
to_dir = "C:/Users/Smart/Downloads" 

list_of_files = os.listdir(from_dir)

print("List of Files in Downloads:")
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    print(f"File: {name}, Extension: {extension}")

    shutil.move(os.path.join(from_dir, file_name), os.path.join(to_dir, file_name))

print("Files moved successfully!")