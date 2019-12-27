# From a "pacakge" import "features" from it
from sys import argv
# For the Terminal : 1) The script you want to run , 2) The file name you want to run with it
script, filename = argv
# filename is saved a usable variable to use in your script
print(f"We're going to erase {filename},")
print(f" If you don't want that, hit Ctrl+C (^C).")
print("If you do want that, hit RETURN.")
# creating the user instructions that will lead to to user input
input(">")
# you already told the computer to read "filename" now you have to tell it to open it
print("Opening the file...")
target = open(filename, "w")  # After opening it you set the "opened file to a new variable like "target"
# Notice the "w" this is tells the computer to open the script in "write mode"
# the default setting to "open" is "read mode"
print("Truncating the file. Goodbye!")  # truncating is to shorten code by removing it
target.truncate()
# Now ask the user to input new text into the file
print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")  # setting inputs to working variables
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# target is the new file text and now we'd like to write new lines into it.
target.write(line1)     # Write input1 into the new file
target.write("\n")      # create a new line ( Move to the next line in the text file)
target.write(line2)     # Rinse lather and repeat
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()  # Need to finish this up by telling the new file text "target to close"
