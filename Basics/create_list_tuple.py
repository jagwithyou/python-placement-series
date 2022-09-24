# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
def create_list_tuple(input_string):
    list_out = input_string.split(",")
    tuple_out = tuple(list_out)
    print(list_out)
    print(tuple_out)

if __name__=="__main__":
    input_string = '12,13,14,15,16'
    create_list_tuple(input_string)