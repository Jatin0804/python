##  HIGHER-LOWER GAME

# Add art.
import d14_art
from d14_game_data import data
import random
import os

# Generate a random account from the game data
def get_random_Account():
    return random.choice(data)

# Format account data into printable format.
def format_data(Account):
    name = Account["name"]
    description = Account['description']
    country = Account["country"]

    return f"{name}, a {description}, from {country}"

# Ask user for a guess.

# Check if user is correct.
def check_Answer(guess, a_follower, b_follower):
    """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
    if a_follower > b_follower :
        return guess == "a"
    else:
        return guess == "b"
    
def game():
    print(d14_art.logo)
    score = 0
    game_continue = True
    account_A = get_random_Account()
    account_B = get_random_Account()

    # Make game repeatable.
    while game_continue:
        # Make B become the next A.
        account_A = account_B
        account_B = get_random_Account()

        while account_A == account_B :
            account_B = get_random_Account()

        print(f"Compare A : {format_data(account_A)}.")
        print(d14_art.vs)
        print(f"Compare B : {format_data(account_B)}.")

        guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
        # Get follower count.
        a_follower_count = account_A["follower_count"]
        b_follower_count = account_B["follower_count"]
        # If Statement
        is_correct = check_Answer(guess, a_follower_count, b_follower_count)

        # Clear screen between rounds.
        os.system('cls')
        print(d14_art.logo)
        # Feedback.
        if is_correct:
            # Score Keeping.
            score += 1
            print(f"You are right! Current Score : {score}")
        else:
            game_continue = False
            print(f"Sorry, that's Wrong. Final Score : {score}")


game()
