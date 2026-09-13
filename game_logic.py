from game_settings import get_game_settings, generate_number
from score_management import update_high_scores
import datetime

# Main gameplay function with enhanced feedback and guess tracking
def number_guessing_game(difficulty_level):
    """
    Runs the number guessing game and handles player guesses.
    Provides feedback after each guess and records history.
    """
    settings = get_game_settings(difficulty_level)
    number = generate_number(settings)
    max_attempts = settings['max_attempts']
    attempts = 0
    guess_history = []  # Tracks each guess for analysis

    print(f"\nI'm thinking of a number between {settings['range'][0]} and {settings['range'][1]}.")
    log_event(f"Game started - Difficulty level: {difficulty_level}")
    
    # Gameplay loop
    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
            guess_history.append(guess)
            attempts += 1
            if guess < number:
                print("Too low! Try a higher number.")
            elif guess > number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                show_game_summary(guess_history, number, attempts)
                player = input("Enter your name for the high score board: ")
                update_high_scores(player, attempts)
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    if attempts == max_attempts and guess != number:
        print(f"Out of attempts! The correct number was {number}.")
        show_game_summary(guess_history, number, attempts, won=False)

# Display a game summary
def show_game_summary(guesses, number, attempts, won=True):
    """
    Summarizes the game result at the end of each session.
    """
    result = "won" if won else "lost"
    print(f"\nGame Summary - You {result}!")
    print(f"Number to guess: {number}")
    print(f"Your guesses: {guesses}")
    print(f"Total attempts: {attempts}")
    log_event(f"Game result: {result} - Number: {number} - Attempts: {attempts}")

# Logs game events
def log_event(event, filename="game_log.txt"):
    """
    Logs important game events to a specified file with timestamps.
    """
    with open(filename, "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - {event}\n")
