import random
import time

def game_rules():
    print("                 --------- WELCOME TO THE MATH GAME ---------                         \n")
    print("                       ----- GAME DESCRIPTION -----                           ")
    print("""You will be given random math equations and you'll have to solve them within 30 seconds.
For each correct answer you'll be given points. If you get an answer wrong, the game is over. 
When the clock runs out of time, you'll be given the your total points. Have fun!!\n\n""")
    
    while True:
        start = input("Are you ready to start the game? Yes or No: ")
        if start == "Yes".lower():
            print()
        else:
            exit()
        break

game_time = 30

def user_input():
    operation = input("\nChoose an operation: \n1. Addition \n2. Subtraction \n3. Multiplication \n")
    difficulty = input("\nChoose a difficulty level: \n1. Easy \n2. Medium \n3. Hard \n")
    while operation not in ["1", "Addition", "2", "Subtraction", "3", "Multiplication"]:
        operation = input("\nInvalid choice!!! Choose an operation: \n1. Addition \n2. Subtraction \n3. Multiplication \n")
    while difficulty not in ["1", "Easy ", "2", "Medium", "3",  "Hard"]:
        difficulty = input("\nInvalid choice!!! Choose a difficulty level: \n1. Easy \n2. Medium \n3. Hard \n")
    return operation, difficulty

def create_equation(operation, difficulty):    
    if operation == "1" or operation == "Addition".lower():
        if difficulty == "1" or difficulty == "Easy".lower():
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif difficulty == "2" or difficulty == "Medium".lower():
            num1 = random.randint(10, 100)
            num2 = random.randint(10, 100)
        else:
            num1 = random.randint(100, 200)
            num2 = random.randint(100, 200)
        equation = "{} + {} = ?".format(num1, num2)
        answer = num1 + num2
    elif operation == "2" or operation == "Subtraction".lower():
        if difficulty == "1" or difficulty == "Easy".lower():
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif difficulty == "2" or difficulty == "Medium".lower():
            num1 = random.randint(10, 100)
            num2 = random.randint(10, 100)
        else:
            num1 = random.randint(100, 200)
            num2 = random.randint(100, 200)
        equation = "{} - {} = ?".format(num1, num2)
        answer = num1 - num2
    else:
        if difficulty == "1" or difficulty == "Easy".lower():
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 5)
        elif difficulty == "2" or difficulty == "Medium".lower():
            num1 = random.randint(6, 15)
            num2 = random.randint(6, 15)
        else:
            num1 = random.randint(15, 30)
            num2 = random.randint(15, 30)
        equation = "{} * {} = ?".format(num1, num2)
        answer = num1 * num2
    return equation, answer

def play_game(operation, difficulty):    
    score = 0
    start_time = time.time()
    while True:
        equation, answer = create_equation(operation, difficulty) 
        print(equation)
        user_answer = float(input("Answer: "))
        if user_answer == answer:
            score += 1
            print("Right answer!!!\n")
        else:
            print("Wrong answer! The answer is:", answer)
            break
        if time.time() - start_time >= game_time:
            print("Time's up")
            break       
    print(f"Game over! Your score was {score}")
    return score

def main():
    game_rules()
    top_score = 0
    while True:
            operation, difficulty = user_input()            
            score = play_game(operation, difficulty)
            if score > top_score:
                top_score = score
                print("Congratulations! That's your highest score.")
            else:
                print(f"Your best score is {top_score}.")
            play_again = input("Do you want to play again? (Yes / No): ").lower()
            if play_again.lower() == "no":
                break

if __name__ == "__main__":
    main()