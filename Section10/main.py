from art import logo

#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    
    final_answer = 0

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an opertation from the line above: ")
    num2 = float(input("What's the second number?: "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    final_answer = first_answer

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    more = True
    while more == True:
        answer = input(f"Type 'y' to continue calculating with {final_answer}, or type 'n' to start a new calculation: ").lower()

        if answer == "y":
            operation_symbol = input("Pick an operation: ")
            num3 = float(input("Pick the next number: "))
            calculation_function = operations[operation_symbol]
            second_answer = calculation_function(final_answer, num3)
            print(f"{final_answer} {operation_symbol} {num3} = {second_answer}")
            final_answer = second_answer
        else: 
            more = False
            calculator()

calculator()
