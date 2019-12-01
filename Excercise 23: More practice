print("Let's practice everything.")
print("you\'d need to know \'bout excapes with \\ that do:")
print('\n new lines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intution 
and requires an explanation
\n\t\twhere there is none.
"""

print("------------")
print(poem)
print("------------")


five = 10-2+3-6
print(f"This should be five. {five}")

def secret_formula(started):  # this code will run with a variable subbed into "started"
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)  # start_point = started in "secret_formula" function
#  line 30 renames the variables to beans instead of jelly_beans
# remember that this is another way to formulate a string
print("with a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
# this is a better way of doing it because it gives a clear indication of what is being called
start_point = start_point / 10
#  This creates a new start point to run to run the "Secret_formula" function
print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
# this references the return order, not what is actually written in the string
