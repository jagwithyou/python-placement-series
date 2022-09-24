
# Write a Python program to create a histogram from a given list of integers

def main(input_list):
    res =""
    for list_item in input_list:
        res = res + str(list_item) + " | "+("*"*list_item)+"\n"
    return res

def reverse_histogram(input_list):
    max_val = max(input_list)
    res = ""
    while max_val >0:
        for value in input_list:
            if max_val <= value:
                res = res + " * "
            else:
                res += "   "
        res += "\n"
        max_val -= 1

    res = res + ("-"*len(input_list)*3) +"\n"
    for data in input_list:
        res=res+" "+str(data)+" "
    return res


if __name__ == "__main__":
    # output = main([2,4,3,5])
    # print(output)
    print(reverse_histogram([2,4,3,5,8,4,6]))
