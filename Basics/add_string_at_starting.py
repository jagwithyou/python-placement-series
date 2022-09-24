
# Write a Python program to get a new string from a given string where Is has been added to the front. If the given string already begins with Is then return the string unchanged

def main(input_string):
    if input_string.startswith("is"):
        return input_string
    else:
        return "is "+input_string

if __name__ == "__main__":
    res = main("is he playing")
    print(res)
