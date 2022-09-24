
# Write a Python program to count the number 4 in a given list

def main(input_list,num):
    count = 0
    for list_num in input_list:
        if list_num==num:
            count+=1
    print(count)

if __name__ == "__main__":
    input_list = [1,2,5,4,5,6]
    number = 5
    main(input_list, number)

