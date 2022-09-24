
# Write a Python program to accept a filename from the user and print the extension of that.

def main(file_name):
    file_name_split = file_name.split(".")
    print(file_name_split[-1])

if __name__ == "__main__":
    file_name = "input_file.txt"
    main(file_name)

