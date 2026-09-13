import random

# Game settings for different difficulty levels with descriptions
def get_game_settings(difficulty_level):
    """
    Returns game parameters based on the chosen difficulty level.
    Parameters include range for the random number and maximum allowed attempts.
    """
    settings = {
        'easy': {'range': (1, 50), 'max_attempts': 15, 'description': "Easy level with a small range and more attempts."},
        'medium': {'range': (1, 100), 'max_attempts': 10, 'description': "Medium level with a moderate range and attempts."},
        'hard': {'range': (1, 200), 'max_attempts': 7, 'description': "Hard level with a large range and fewer attempts."}
    }
    chosen_settings = settings.get(difficulty_level, settings['medium'])
    print(f"\nSelected Difficulty: {difficulty_level.capitalize()} - {chosen_settings['description']}")
    return chosen_settings  # Defaults to medium if invalid choice

# Function to generate a random target number within the chosen range
def generate_number(settings):
    """
    Generates a random target number within the range specified by the settings.
    Helps in customizing the number generation based on difficulty.
    """
    return random.randint(*settings['range'])
