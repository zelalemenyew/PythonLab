
import random

# Initialising the variables
player_score = 0
computer_score = 0
draw_game = 0

# Creation of a while loop to continually prompt the user to play the game
while True:

    # Prompt the user to enter either Rock, Paper, or Scissors
    player_choice = input( 'enter a choice (Rock, Paper, Scissors): ' )

    # Create a list of possible choices
    options = ["Rock", "Paper", "Scissors"]

    # Computer randomly selecting one of the choices
    computer_choice = random.choice( options )

    # Creation of an if statement to determine the winner of the round
    if player_choice == computer_choice:
        print( f"It's a tie! You both chose {player_choice}" )
        draw_game += 1
    elif player_choice == "Rock":
        if computer_choice == "Paper":
            print( "You lose! Paper beats Rock" )
            computer_score += 1
        else:
            print( "You win! Rock beats Scissors" )
            player_score += 1
    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            print( "You lose! Scissors beat Paper" )
            computer_score += 1
        else:
            print( "You win! Paper beats Rock" )
            player_score += 1
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            print( "You lose! Rock beats Scissors" )

            computer_score += 1
        else:
            print( "You win! Scissors beats Paper" )

            player_score += 1
    else:
        print( "Please enter a valid option" )

    # Prompt the user to either keep playing or not
    new_game = input( "Do you want playing again? (yes or no) " )

    # Create an if statement that split the programing depending on the input
    if new_game == "no":
        break
    else:
        continue

# Print the score of the game
print( f"Games Played: {player_score + computer_score + draw_game}" )

print( f"Your Score: {player_score}" )

print( f"Computer Score: {computer_score}" )

print( f"Draws: {draw_game}" )






