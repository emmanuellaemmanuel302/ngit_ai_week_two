
def calculator():
    try:
        num1 = float(input("enter first number:"))
        num2 = float(input("enter second number"))
        operator = input ("choose operation (+, -, *, /):")
        if operator == "+":
            result = num1 + num2
        elif operator =="-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print ("error: cannot divide by zero.")
                return
            result = num1 / num2
        else: 
            print ("invalid operation selected.")
            return
        print(f"result: {result}")
    except ValueError:
        print("invalid input. please enter numeric values.")


#Salary Tax Checker 
def salary_tax_checker():
    try:
        salary = float(input("enter your monthly salary"))
        if salary > 250000:
            tax_rate = 0.15
        else:
            tax_rate = 0.5
        tax = salary * tax_rate
        net_salary = salary - tax
        print(f"Tax deducted: {tax}")
        print(f"Net salary: {net_salary}")
    except ValueError:
        print("invalid input. please enter a valid number")

# Number Guessing Game Function
def number_guessing_game():
    import random
    secret_number =random.randint(1, 10)
    attempts = 3
    print("Guess the number between 1 and 10.")
    while attempts > 0:
        try:
            guess = int(input(f"you have{attempts} attempt(s) left. Enter your guess:"))
            if guess == secret_number:
                print("congratulations! you have guessed correctly!")
                return
            else:
                print("wrong guess.")
                attempts -= 1
        except ValueError:
            print("please enter a valid number.")
            print(f"sorry, you lost. the correct number was {secret_number}.")

# Main Menu 
def main():
    while True:
        print("\n=== loan company Utility Tool ===")
        print("1. Calculator")
        print("2. salary Tax Checker")
        print("3. Number Guessing Game")
        print("4. Exit")
        choice = input("select an option (1-4): ")
        if choice == "1":
            calculator()
        elif choice == "2":
            salary_tax_checker()
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selecetion. Please choose between 1 and 4.")

#Run the program
if __name__== "__main__":
    main()



