import datetime

History_file = "history.txt"

def show_history():
    try:
        with open(History_file, 'r') as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No History Found")
        else:
            print("\n--- Calculation History ---")
            for line in reversed(lines):
                print(line.strip())

    except FileNotFoundError:
        print("No History File Found")


def clear_history():
    with open(History_file, 'w') as file:
        pass
    print("History Cleared")


def save_to_history(equation, result):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(History_file, 'a') as file:
        file.write(f"[{time}] {equation} = {result}\n")


def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input! Use format: 8 + 8")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Please enter valid numbers!")
        return

    try:
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Cannot divide by zero")
                return
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        elif op == "**":
            result = num1 ** num2
        elif op == "//":
            result = num1 // num2
        else:
            print("Invalid Operator")
            return

    except Exception as e:
        print("Error occurred:", e)
        return

    if result.is_integer():
        result = int(result)

    print("Result:", result)
    save_to_history(user_input, result)


def main():
    print("---- Advanced Calculator ----")
    print("Commands: history | clear | exit")
    print("Operations: +  -  *  /  %  **  //")

    while True:
        user_input = input("\nEnter calculation or command: ").lower()

        if user_input == "exit":
            print("Good Bye 👋")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)


main()