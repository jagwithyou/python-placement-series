# Write a Python program to display the first and last colors from the following list.

def main(colors):
    print("First color is",colors[0])
    print("Last color is", colors[-1])

if __name__ == "__main__":
    input_colors = ["white", "blue", "red"]
    main(input_colors)