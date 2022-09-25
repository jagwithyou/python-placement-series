
# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def main(a,b):
    if b==0:
        return a
    return main(b,a%b)

if __name__ == "__main__":
    print(main(56,98))

