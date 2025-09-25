import time


def main():
    # Login / Registration Part
    name = input("Enter your username: ").strip().lower()
    print(f"Hello {name}, you are most welcomed!")

    while True:
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

        if password == confirm_password:
            print(f"✅ Password verified. Length: {len(password)}")
            break
        else:
            print("❌ Passwords do not match. Try again.\n")

    print("\nWelcome to the Calculator App (Created by MRCET Student with guidance of Mr. Siddharth)\n")

    # Calculator Loop
    while True:
        try:
            x = float(input("Enter the value of X: "))
            y = float(input("Enter the value of Y: "))
        except ValueError:
            print("⚠️ Invalid number input. Please try again.")
            continue

        operator = input(
            "Enter operator (+, -, x, /) or 'q' to quit: ").strip()

        if operator == "q":
            print("👋 Exiting Calculator. Goodbye!")
            break
        elif operator == "+":
            print("Result:", add(x, y))
        elif operator == "-":
            print("Result:", subtract(x, y))
        elif operator == "x":
            print("Result:", multiply(x, y))
        elif operator == "/":
            print("Result:", divide(x, y))
        else:
            print("⚠️ Invalid operator. Please use +, -, x, or /.\n")

        time.sleep(1)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return "Undefined (division by zero)" if b == 0 else a / b


if __name__ == "__main__":
    main()
