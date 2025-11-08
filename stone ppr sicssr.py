import random

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def get_user_choice():
    choice = input("Enter your choice (stone, paper, scissors): ").lower()
    while choice not in ['stone', 'paper', 'scissors']:
        choice = input("Invalid choice. Please enter 'stone', 'paper', or 'scissors': ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'stone' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'stone') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    
    return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()