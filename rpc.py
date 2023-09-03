import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose from rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    rounds = int(input("Enter the number of rounds: "))

    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

    print("Game over!")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
