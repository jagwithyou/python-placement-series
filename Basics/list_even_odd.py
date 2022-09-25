
# Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 10 in the sequence.
def check_even_odd(num):
    if num%2==0:
        return True
    return False

def main(input_list):
    for value in input_list:
        if check_even_odd(value) and value<10:
            print(value)

if __name__ == "__main__":
    main([2,3,4,5,6,7,8,9,12,15,16])

