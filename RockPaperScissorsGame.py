import random

def welcome_message():
    print("\033[95m\033[1m")  # Set color to bright magenta and bold text
    print("##############################################")
    print("#                                            #")
    print("#          Welcome to Rock, Paper,           #")
    print("#                  Scissors!                 #")
    print("#                                            #")
    print("##############################################")
    print("#                                            #")
    print("#           Developed by Wahab Khan          #")
    print("#                                            #")
    print("##############################################")
    print("\033[0m")  # Reset color

def play_game():
    choices = ["rock", "paper", "scissors"]
    welcome_message()

    print("\033[93mLet's start the game! Type 'rock', 'paper', or 'scissors' to play.\033[0m")
    
    while True:
        user_choice = input("\033[94mEnter your choice: \033[0m").lower()
        if user_choice not in choices:
            print("\033[91mInvalid choice! Please try again.\033[0m")
            continue

        computer_choice = random.choice(choices)
        print(f"\033[93mComputer chose: {computer_choice}\033[0m")

        if user_choice == computer_choice:
            print("\033[96mIt's a tie!\033[0m")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("\033[92mYou win!\033[0m")
        else:
            print("\033[91mYou lose!\033[0m")

        play_again = input("\033[94mDo you want to play again? (yes/no): \033[0m").lower()
        if play_again != 'yes':
            print("\033[93mThanks for playing! Goodbye!\033[0m")
            break

if __name__ == "__main__":
    play_game()
