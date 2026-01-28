import math_operations

def menu()
    print("=== SIMPLE CALCULATOR ===")
    print("Choose an option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    choice = input("")
    if choice == "1":
        math_operations.add()
    elif choice == "2":
        math_operations.sub()
    elif choice == "3":
        math_operations.mult()
    elif choice == "4":
        math_operations.div()
    elif choice == "5":
        print("Quitting...")