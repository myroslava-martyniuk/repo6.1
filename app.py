def add(a, b):
    return a + b
def substract(a, b):
    return a - b

def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == '__main__':
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    operator = input('Enter the operator +, -, * or /: ')

    if operator == '+':
        print(f"The result of addition is: {add(num1, num2)}")
    elif operator == '-':
        print(f"The result of substraction is: {substract(num1, num2)}")
    elif operator == '*':
        print(f"The result of multiplication is: {multiplication(num1, num2)}")
    elif operator == '/':
        print(f"The result of division is: {division(num1, num2)}")    
    else:
        print('Invalid operator')
