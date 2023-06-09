import random

def get_choice():
    options = ["rock", "paper", "cut"]
    player_choice = input("Enter a choice (rock, paper, or cut): ")
    while player_choice not in options:
        player_choice = input("Invalid choice. Enter again (rock, paper, or cut): ")

    computer_choice = random.choice(options)
    result = {"player": player_choice, "computer": computer_choice}
    print(f"You chose {player_choice} and computer chose {computer_choice}")

    if player_choice == "rock" and computer_choice == "paper":
        return "You lose!"
    elif player_choice == "rock" and computer_choice == "cut":
        return "You win!"
    elif player_choice == "paper" and computer_choice == "rock":
        return "You win!"
    elif player_choice == "paper" and computer_choice == "cut":
        return "You lose!"
    elif player_choice == "cut" and computer_choice == "rock":
        return "You lose!"
    elif player_choice == "cut" and computer_choice == "paper":
        return "You win!"
    else:
        return "It's a tie!"

while True:
    result = get_choice()
    print(result)
    choice_again = ["yes", "no"]
    play_again = input("Do you want to play again? Enter 'yes' or 'no': ").lower()
    while play_again not in choice_again:
        play_again = input("Invalid choice. Enter again (yes or no):  ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
