choices = ['stone', 'paper', 'scissors']

player1_choice = random.choice(choices)

player2_choice = input("Enter your choice (stone, paper, scissors): ")

if player2_choice == player1_choice:
    print(f"Both chose {player1_choice}. It's a tie!")
elif (player2_choice == 'stone' and player1_choice == 'scissors') or \
     (player2_choice == 'paper' and player1_choice == 'stone') or \
     (player2_choice == 'scissors' and player1_choice == 'paper'):
    print(f"You chose {player2_choice}, player1 chose {player1_choice}. You win!")
else:
    print(f"You chose {player2_choice}, player1 chose {player1_choice}. player1 wins!")
    