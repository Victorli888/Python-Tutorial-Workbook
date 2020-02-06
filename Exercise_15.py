from sys import argv

script, filename = argv  # 1-3 will grab the file name

txt = open(filename)  # 5 Will open and read the directions

print(f"Here's your file {filename}:")  # 7 print the file name to confirm
print(txt.read())  # calling on "txt" function and re calls from when it was opened

print("Type the filename again:")
file_again = input("> ")  # using an input to prompt the user to call a file

txt_again = open(file_again)  # will open and read it

print(txt_again.read())  # will print the actual text in the file
