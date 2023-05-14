start_game = input("Welcome to Scissors, Paper, Rock! Type play to play. ") # Welcomes the user, and to enter "play" to play.	
if start_game == "play": # Application will run if entry is "play".
    print("Let's play.") # Prints a message to confirm that game is running.
if not start_game == "play": # Application will exit if input is different from "play".
    exit()
player_one = input("Player 1: Please enter your name. ") # Asks the first player for their name.
player_two = input("Player 2: Please enter your name. ") # Asks the second player for their name.
print(f"Hello {player_one} and {player_two}. Welcome to Scissors, Paper, Rock.")
while(True):
    player_one_choice = input(f"{player_one}, type Rock, Paper or Scissors. ").lower() # Asks Player 1 to select choice.
    player_two_choice = input(f"{player_two}, type Rock, Paper or Scissors. ").lower() # Asks Player 2 to select choice.
    if player_one_choice == "rock" and player_two_choice == "paper": 
        print(f"{player_two} chose paper - {player_two} has won.")
    elif player_one_choice == "paper" and player_two_choice == "scissors":
        print(f"{player_two} chose scissors - {player_two} has won.")       ## Outcomes for each choice ##
    elif player_one_choice == "scissors" and player_two_choice == "rock":
        print(f"{player_two} chose rock - {player_two} wins.")
    elif player_one_choice == "paper" and player_two_choice == "rock":
        print(f"{player_one} chose paper - {player_one} wins.")
    elif player_one_choice == "rock" and player_two_choice == "scissors":
        print(f"{player_one} chose rock - {player_one} wins.")
    elif player_one_choice == "scissors" and player_two_choice == "paper":
        print(f"{player_one} chose scissors - {player_one} wins.")
    elif player_one_choice == player_two_choice:
        print("You have both tied! Play again.")
    break
print("Thank you for playing, come back soon!") # Prints a goodbye message once game is finished.










