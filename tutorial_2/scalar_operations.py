def add(num1, num2):
    return (num1 + num2)

def subtract(num1, num2):
    return (num1 - num2)

def multiply(num1, num2):
    return (num1 * num2)

def divide(num1, num2):
    return (num1 / num2)

def main():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print(add(first_number, second_number))
    print(subtract(first_number, second_number))
    print(multiply(first_number, second_number))
    print(divide(first_number, second_number))

main()
