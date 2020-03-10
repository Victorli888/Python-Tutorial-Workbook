# Blueprint: lambda argument: manipulate(argument)

print("Example: Using Lambda")

add = lambda x, y : x + y
quadratic = lambda x1, x2, c: x1**2 + x2*2 + c  # (x1)^2 + (x2)*2 + (c)


print(add(3, 5))
print(quadratic(5, 3, 3))  # (5)^2 + (3)*2 + 3 = 34

# For more examples please view Exercise_Lambda.py
