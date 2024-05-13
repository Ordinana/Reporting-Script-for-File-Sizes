import os

# defining directories and files

path = input("Define a path: ")

actual_path = os.path.abspath(path)

# father_path = os.path.dirname(actual_path)

file_metadata = {}

num_files = int(input("How many files do you want to find?:"))

for root, directories, files in os.walk(actual_path):
    count = 0
    for _file in files:
        full_path = os.path.join(root, _file)
        size = os.path.getsize(full_path)
        file_metadata[full_path] = size
        if count == num_files:
            break   
        count += 1
    if count == num_files:
        break

        
# report back the results with only the largest files
num_largest = int(input("How many largest files do you want to report?:"))

items_shown = 0

count = 1

for path, size in sorted(file_metadata.items(), key=lambda x:x[1], reverse=True):
    if items_shown == num_largest:
        break
    print(f"Number {count}: Size: {size}b Path: {path}")
    items_shown += 1
    count += 1
