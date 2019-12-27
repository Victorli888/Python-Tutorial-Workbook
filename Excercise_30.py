people = 31
cars = 15
trucks = 30
# We use elif instead of if again so that the statements follow the same branch
# for example, if we did if cars > people on line 9 then it would print that statement and the else statement

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide")

if trucks > cars:
    print("That's too many trucks")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
