import argparse
 
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-o", "--Output", help = "Enter Output file name")
parser.add_argument("-m", "--Message", help = "Enter the message for the file")
 
# Read arguments from command line
args = parser.parse_args()
 
if args.Output:
    print("Creating file as: % s.py" % args.Output)

formatted_string = f'''
# {args.Message}

def main():
    pass

if __name__ == "__main__":
    main()

'''
with open(args.Output+".py", 'a') as the_file:
    the_file.write(formatted_string)