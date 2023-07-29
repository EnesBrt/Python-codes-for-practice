from art import logo


# Addition
def add(x, y):
    return x + y


# subtraction
def subtract(x, y):
    return x - y


# Multiplication
def multiply(x, y):
    return x * y


# division
def divide(x, y):
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)


def calculator():
    restart = True
    while restart:

        num1 = eval(input("What's the first number ? \n"))
        num2 = eval(input("What's the next number ? \n"))

        for symbol in operations:
            print(symbol)

        operations_symbol = input("Pick an operation from the line above: \n")
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        ask_again = True

        while ask_again:
            question = input("would you want ot start again ? write y for yes, n for no.\n")

            if question == "y":
                ask_again = False
            elif question == "n":
                restart = False
                ask_again = False
                print("Bye bye, See you later !")
            else:
                print("you've typed the wrong answer, type y or n !")
                ask_again = True


calculator()
