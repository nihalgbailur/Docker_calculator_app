import logging

# Configure logging
logging.basicConfig(
    filename='/var/log/calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_valid_number(prompt):
    """Repeatedly ask for input until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            logging.warning("Invalid number input")

def perform_operation(num1, num2, op):
    """Perform arithmetic operations and handle errors."""
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2
    }
    if op == '/':
        if num2 == 0:
            logging.error("Attempted division by zero")
            return "Undefined (division by zero)"
        return num1 / num2
    return operations.get(op, "Invalid operation")

def calculator():
    """Main calculator function with a loop for continuous use."""
    while True:
        print("\n===== Simple Calculator =====")
        num1 = get_valid_number("Enter first number: ")
        num2 = get_valid_number("Enter second number: ")
        
        print("\nAvailable operations: +, -, *, /")
        op = input("Choose an operation: ").strip()
        
        result = perform_operation(num1, num2, op)
        print(f"\nResult: {num1} {op} {num2} = {result}")
        logging.info(f"Calculated: {num1} {op} {num2} = {result}")
        
        # Ask if user wants to continue
        if input("\nAnother calculation? (y/n): ").lower() != 'y':
            logging.info("Exiting calculator.")
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
