
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn 

def main(input_number):
    n=int(input_number)
    nn=int(input_number+input_number)
    nnn=int(input_number+input_number+input_number)
    print(n+nn+nnn)
    
if __name__ == "__main__":
    input_num = "5"
    main(input_num)
