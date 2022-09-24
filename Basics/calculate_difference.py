
# Write a Python program to get the difference between a given number and 20, if the number is greater than 20 return double the absolute difference.

def main(num):
    if num < 20:
        return 20 - num
    else:
        return (num-20)*2

if __name__ == "__main__":
    out_put = main(22)
    print(out_put)

