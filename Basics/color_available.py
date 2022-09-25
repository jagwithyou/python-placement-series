
# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2

def main(input_list1, input_list2):
    res = []
    for color in input_list1:
        if color not in input_list2:
            res.append(color)
    return res

if __name__ == "__main__":
    input_list1 = set(["White", "Black", "Red"]) 
    input_list2 = set(["Red", "Green"])
    print(input_list1.difference(input_list2))
    print(main(input_list1, input_list2))

