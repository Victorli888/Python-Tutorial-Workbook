# Ternary Operators, Conditional expressions in Python that evaluate something based on a boolean value

#Blueprint: condition_if_true if condition else condition_if_false

print("Example 1: Nice? or Not Nice.")
is_nice = False
state = "nice" if is_nice else "not nice"
print(state)


print("\nExample 2: Involving Tuples")
# Blue print: (if_test_is_false, if_test_is_true)[test]
nice = True
personality = ("not nice", "nice")[nice]
print(f"The cat is {personality}")

# Avoid this because both elements of true and false is being evaluated (takes up extra memory)
