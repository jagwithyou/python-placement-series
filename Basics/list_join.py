
# Write a Python program to concatenate all elements in a list into a string and return it

def main(input_list, join_string):
    res = ""
    for data in input_list:
        res += str(data) + join_string
    return res

if __name__ == "__main__":
    output = main(["abc", "pqr", "xyz"], " ")
    print(output)
