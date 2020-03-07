print("Example 1: Using Exceptions\n")

# What is Exception?
# An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the programs
# instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an
# exception. An exception is a Python object that represents an error.

# When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and
# quits.

# Handling an exception
# If you have some suspicious code that may raise an exception, you can defend your program by placing the suspicious
# code in a try: block. After the try: block, include an except: statement, followed by a block of code which handles
# the problem as elegantly as possible.
print("Starting Step 1.....")

print("Moving to step 2.....")
try:
    file = open('test.txt', 'rb')  # rb - read binary
except(IOError, EOFError) as e:
    print('oooohhh noooo! An IOError occurred.  {}'.format(e.args[-1]))
# As you can see an error occurred in after step 2, the error is due to the fact that there is no such test.txt in our
# directory, but instead of ending the script we can continue the process. This is  "defending" our program.
print("Step 3")
print("Step 4")

print("\n\n\n Example 2: Handling Multiple exceptions")
# We can have as many except blocks as we want. This example also includes raise e, this line raises the actual error
# and ends the script. " Try commenting it out and you'll see that the script will continue.
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("GOOD GOD, an EOF error occurred.")
    raise e
except IOError as e:
    print("Holy Moly, an error occurred.")
    # raise e  # uncomment to observe behavior

print("\n\n\nExample 3: Encompassing ALL exceptions ")
try:
    file = open('Fake_file.txt', 'rb')
except Exception as e:
    print("This is non-sense")
    # raise e    # uncomment to observe behavior

print("\nExample 4: try/else clause")
# Often times we might want some code to run if no exception occurs. This can easily be achieved by using an else clause
# One might ask: why, if you only want some code to run if no exception occurs, wouldn’t you simply put that code inside
# the try? The answer is that then any exceptions in that code will be caught by the try, and you might not want that.
# Most people don’t use it
print("\n\n\nExample 5: finally clause")
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))

finally:
    print("This would be printed whether or not an exception occurred!")

print("\nAnother Example")

try:
    print("I'm sure no exception will occur")
except Exception:
    print("This is an exception")
else:
    # Any code that should only run if no exception occurs on the try
    # but for which exceptions should NOT be caught
    print("This would only run if no exceptions occurs")
finally:
    print("This would be printed in every case.")
