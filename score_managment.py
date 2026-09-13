import json
import datetime

# Load high scores from a JSON file or initialize empty scores
def load_scores_from_file(filename="high_scores.json"):
    """
    Loads high scores from the specified file.
    Returns an empty dictionary if no file or an error occurs.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No previous high scores found. Be the first to set a record!")
        return {}
    except PermissionError:
        print("Access denied: Cannot load high scores.")
        return {}

# Save high scores to a JSON file
def save_scores_to_file(scores, filename="high_scores.json"):
    """
    Saves the high scores dictionary to a file.
    Handles permission issues with error messages.
    """
    try:
        with open(filename, "w") as file:
            json.dump(scores, file)
    except PermissionError:
        print("Access denied: Cannot save high scores.")

# Update the high score if the current score is better
def update_high_scores(player, attempts):
    """
    Updates the player's high score if the new score is better.
    Requests player name to personalize the leaderboard.
    """
    high_scores = load_scores_from_file()
    if player in high_scores:
        if attempts < high_scores[player]:
            high_scores[player] = attempts
            print("New personal best! You've set a new record for yourself.")
    else:
        high_scores[player] = attempts
    save_scores_to_file(high_scores)
    print("High scores updated!")

# Display the high scores sorted by the fewest attempts
def show_high_scores():
    """
    Displays the sorted leaderboard from saved high scores, sorted by attempts.
    """
    high_scores = load_scores_from_file()
    if high_scores:
        print("\nLeaderboard:")
        for player, score in sorted(high_scores.items(), key=lambda item: item[1]):
            print(f"{player}: {score} attempts")
    else:
        print("No high scores recorded yet.")
