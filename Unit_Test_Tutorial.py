def calculator(num1, symbol, num2):

    if symbol == "*":
        return num1 * num2

    if symbol == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Can't Divide by Zero."
