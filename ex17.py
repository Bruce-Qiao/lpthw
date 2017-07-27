from sys import argv
from os.path import exists

script, file1, file2 = argv

source_file = open(file1)
source_file_content = source_file.read()
print(f"{file1} has {len(source_file_content)} bytes long.")

print(f"Is {file2} exist? {exists(file2)}")

destination_file = open(file2, "w")
destination_file.write(source_file_content)

source_file.close()
destination_file.close()
