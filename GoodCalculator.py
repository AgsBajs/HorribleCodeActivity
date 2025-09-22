"""Features:
- Input validation for numeric values.
- Division by zero is handled with a ZeroDivisionError.
- Continuous loop until the user chooses to exit.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """
    Return the quotient of two numbers.
        Raises:
            ZeroDivisionError: If the divisor is zero.
    """
    if b == 0:
        raise ZeroDivisionError
    return a / b

def show_menu():
    print("\nSelect Operation:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\nq. Quit")

def main():
    show_menu()
    while True:
        choice = input()
        if choice in ('1','2','3','4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "yes":
                show_menu()
            elif next_calculation == "no":
                print("Thank you. Goodbye.")
                break

        else:
            print("Invalid Input")

if __name__ == '__main__':
    main()