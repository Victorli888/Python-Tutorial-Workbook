#from sys import argv

#script, filename = argv  # 1-3 will grab the file name

#txt = open(filename)  # 5 Will open and read the directions

#print(f"Here's your file {filename}:")  # 7 print the file name to confirm
#print(txt.read())  # calling on "txt" function and re calls from when it was opened

# print("Type the filename again:")
# file_again = input("> ")  # using an input to prompt the user to call a file

#  txt_again = open(file_again)  # will open and read it

#  print(txt_again.read())  # will print the actual text in the file

#  Exercise 15 Practice
#print("Tell me what file would you like to open:")
#file = input("> ")

#txt = open(file)
#print(txt.read())

#  attempt 2

#print("Hello there what file would you like to open?:")  # input prompt
#file = input("> ")  # input variable
#txt = open(file)  # You've prompted the file from the user now you need to open it
#print(txt.read())  # Okay You've opened it Now tell the code to recall it and print it

# attempt 3
#print("Hi there, What file what you like to open?:")
#file = input("> ")
#txt = open(file)
#print(txt.read())

# attempt 4 This time grab the feature from the package sys from argv
#from sys import agrv
#agrv = script, file # Wrong order try again

#txt = open(file)
#print("f From {script} this is what I've found") # its f" not "f
#print(txt.read)

# attempt 5
#from sys import argv
#script, file = argv

#txt = open(file)
#print(f"alright this is the file I found: {script}")
#print(txt.read) # so close... command is print(txt.read())  dont for  get the ()

#attempt 6 This time I'll do both the package-feature and input method
# input method:
from sys import argv
script, file = argv
txt = open(file)
print(f"This is your file is: {script} and it says:")
print(txt.read())

print("What is the file You want to open?:")
file1 = input("> ")
text1 = open(file1)
print("I'll read this file for you then.")
print(text1.read())

# Perfect!
