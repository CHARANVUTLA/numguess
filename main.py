from game_logic import number_guessing_game, log_event
from score_management import show_high_scores, save_scores_to_file, load_scores_from_file

def reset_high_scores():
    """
    Resets the high scores by saving an empty dictionary to the high scores file.
    Asks for user confirmation before proceeding.
    """
    confirmation = input("Are you sure you want to reset all high scores? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        save_scores_to_file({})
        print("All high scores have been reset.")
        log_event("High scores reset by user.")
    else:
        print("High scores were not reset.")
        log_event("High score reset canceled by user.")

def display_main_menu():
    """
    Displays the main menu options for the player.
    Provides options to play the game, view high scores, reset scores, or exit.
    """
    print("\n========== Number Guessing Game Main Menu ==========")
    print("1. Play Game")
    print("2. View High Scores")
    print("3. Reset High Scores")
    print("4. Exit")
    print("====================================================")

def choose_difficulty():
    """
    Prompts the player to select a difficulty level.
    Returns the chosen difficulty level as a string.
    """
    print("\nSelect your difficulty level:")
    print("1. Easy (1-50, 15 attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 7 attempts)")
    
    level_choice = input("Choose difficulty level (1, 2, or 3): ").strip()
    difficulty_map = {'1': 'easy', '2': 'medium', '3': 'hard'}
    difficulty_level = difficulty_map.get(level_choice, 'medium')  # Default to 'medium'
    
    print(f"Difficulty set to {difficulty_level.capitalize()}.")
    log_event(f"Difficulty chosen: {difficulty_level}")
    return difficulty_level

def main():
    """
    Main loop for the game, handling user interactions in the menu.
    Controls navigation for playing the game, viewing, and resetting high scores.
    """
    log_event("Game session started")
    while True:
        display_main_menu()
        
        choice = input("Please select an option (1-4): ").strip()
        
        if choice == '1':
            difficulty_level = choose_difficulty()
            number_guessing_game(difficulty_level)
        elif choice == '2':
            show_high_scores()
        elif choice == '3':
            reset_high_scores()
        elif choice == '4':
            print("Thank you for playing the Number Guessing Game! Goodbye!")
            log_event("Game session ended by user.")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 4.")
            log_event(f"Invalid menu selection: {choice}")

if __name__ == "__main__":
    main()
