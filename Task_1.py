filename = 'sample.txt.py'

try:
    file = open(filename, 'r')
    print("Reading file content:")
    a=file.read()
    print(a)
    file.close()
except FileNotFoundError:
    print("Error: The file", filename, "was not found.")
