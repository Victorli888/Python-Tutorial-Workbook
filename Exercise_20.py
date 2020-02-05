from sys import argv  #  create an import file
#  then use this to tell the terminal what files you want to be using import file
script, input_file = argv
# create a mini-script called print_all() with input (f) to perform line 6 when called on
def print_all(f):
    print(f.read())  # Tell python to read file and then print it on the terminal

def rewind(f):  # create a miniscript called rewind with variable f
    f.seek(0)  # simple means of setting a reference point in the file.

def print_a_line(line_count, f):  # another mini-script with two variables
    print(line_count, f.readline())
# this will print variable "line_count and f.readline() - readline() reads a single line from a file
current_file = open(input_file)
# Telling Python to open the input file declared in args and calling it current_file
print("first let's print the whole file: \n")
print ("Name of the file: ", current_file.name)  # .name at the end tells python to name the file
print_all(current_file)  # Call print_all function using "current_file" as variable f
# print the entire current_file       # since we printed the current file our reference point was at the end of the txt file. Now we're at the beginning.
print("lets print 3 lines;")

current_line = 1  # creating a variable named current_line and setting it to "1"
print_a_line(current_line, current_file) # call print_a_line function using current_line and current_file as variables

current_line = current_line + 1  # this would make line 2
print_a_line(current_line, current_file) #  technically since we never used "rewind" we're still on line 2 of the file

current_line = current_line + 1  # creates line 3
print_a_line(current_line, current_file)  # reads the final line of the txt.txt file
