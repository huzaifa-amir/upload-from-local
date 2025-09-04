def simple_calculator():
    print("Simple Calculator - Addition and Subtraction Only")
    print("Enter numbers and operations continuously.")
    print("Type 'q' or 'quit' to exit.\n")

    total = 0.0
    first_input = True

    while True:
        if first_input:
            user_input = input("Enter the first number: ")
            if user_input.lower() in ['q', 'quit']:
                break
            try:
                total = float(user_input)
                first_input = False
            except ValueError:
                print("Invalid number. Try again.")
                continue
        else:
            operator = input("Enter operator (+ or -), or 'q' to quit: ")
            if operator.lower() in ['q', 'quit']:
                break
            if operator not in ['+', '-']:
                print("Invalid operator. Use '+' or '-'.")
                continue

            num_input = input("Enter next number: ")
            if num_input.lower() in ['q', 'quit']:
                break
            try:
                number = float(num_input)
            except ValueError:
                print("Invalid number. Try again.")
                continue

            if operator == '+':
                total += number
            elif operator == '-':
                total -= number

            print(f"Current Total: {total}\n")

    print(f"\nFinal Result: {total}")
    print("Calculator exited.")

# Run the calculator
simple_calculator()