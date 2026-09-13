# numguess
# 🎯 Number Guessing Game

A simple and interactive **Number Guessing Game built with Python**.
The project allows players to choose different difficulty levels, guess a randomly generated number, track their attempts, maintain a high-score leaderboard, and record important game events in a log file.

---

## 📌 Project Overview

The Number Guessing Game challenges the player to guess a randomly generated number within a limited number of attempts.

The game provides **three difficulty levels**:

| Difficulty | Number Range | Maximum Attempts |
| ---------- | ------------ | ---------------- |
| 🟢 Easy    | 1 – 50       | 15               |
| 🟡 Medium  | 1 – 100      | 10               |
| 🔴 Hard    | 1 – 200      | 7                |

After every guess, the game provides feedback such as:

* **Too low** – the guessed number is smaller than the target.
* **Too high** – the guessed number is larger than the target.
* **Correct** – the player successfully guesses the number.

The project also includes a persistent **high-score system** and **event logging**.

---

## ✨ Features

* 🎮 Interactive command-line gameplay
* 🎚️ Three difficulty levels
* 🎲 Random number generation
* 💡 Helpful feedback after every guess
* 📝 Guess history tracking
* 🏆 High-score leaderboard
* 💾 High scores stored in a JSON file
* 🔄 Reset high scores with confirmation
* 📋 Game summary after each round
* 📊 Personal best score tracking
* 📝 Game event logging with timestamps
* ⚠️ Input validation for invalid guesses
* 🧩 Modular Python code structure

---

## 📂 Project Structure

```text
Number-Guessing-Game/
│
├── main.py
├── game_logic.py
├── game_settings.py
├── score_management.py
│
├── high_scores.json
├── game_log.txt
│
└── README.md
```

### File Description

#### `main.py`

Handles the main menu and overall user interaction.

Responsibilities:

* Display the main menu
* Start a new game
* Select difficulty
* Display high scores
* Reset high scores
* Exit the application

#### `game_settings.py`

Contains the settings for each difficulty level.

Responsibilities:

* Define number ranges
* Define maximum attempts
* Generate random target numbers
* Provide difficulty descriptions

#### `game_logic.py`

Contains the core gameplay functionality.

Responsibilities:

* Run the guessing game
* Process player guesses
* Provide high/low feedback
* Track guesses
* Display game summaries
* Record game events

#### `score_management.py`

Manages the leaderboard and persistent scores.

Responsibilities:

* Load scores from JSON
* Save scores to JSON
* Update personal best scores
* Display the leaderboard

---

## 🛠️ Technologies Used

* **Python 3**
* `random` – random number generation
* `json` – storing high scores
* `datetime` – timestamped event logging

No external Python packages are required.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/number-guessing-game.git
```

### 2. Navigate to the Project Directory

```bash
cd number-guessing-game
```

### 3. Run the Game

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

---

## 🎮 How to Play

When the program starts, the main menu appears:

```text
========== Number Guessing Game Main Menu ==========
1. Play Game
2. View High Scores
3. Reset High Scores
4. Exit
====================================================
```

### Step 1 — Start the Game

Select:

```text
1. Play Game
```

### Step 2 — Choose Difficulty

You can select:

```text
1. Easy
2. Medium
3. Hard
```

### Step 3 — Guess the Number

Enter an integer when prompted:

```text
Your guess: 50
```

The game will tell you whether your guess is too high or too low.

### Step 4 — Win the Game

If you guess correctly, you will see:

```text
Congratulations! You guessed the number in 5 attempts.
```

You can then enter your name to save your score.

### Step 5 — View the Leaderboard

Select:

```text
2. View High Scores
```

The leaderboard displays players based on the **fewest attempts**.

---

## 🏆 Scoring System

The objective is to guess the number using the **minimum number of attempts**.

For example:

```text
Leaderboard:

Charan: 3 attempts
Rahul: 5 attempts
Arun: 7 attempts
```

If an existing player achieves a better score, their previous score is replaced with the new personal best.

---

## 💾 Data Storage

The project uses two files for storing information.

### `high_scores.json`

Stores player names and their best scores.

Example:

```json
{
    "Charan": 3,
    "Rahul": 5,
    "Arun": 7
}
```

### `game_log.txt`

Stores important game events with timestamps.

Example:

```text
2026-09-13 13:30:10 - Game session started
2026-09-13 13:30:15 - Difficulty chosen: medium
2026-09-13 13:30:20 - Game started - Difficulty level: medium
2026-09-13 13:30:45 - Game result: won - Number: 73 - Attempts: 4
```

---

## 🛡️ Input Validation

The game handles invalid input so that the program does not crash when the player enters something other than an integer.

Example:

```text
Your guess: hello
Invalid input! Please enter a valid integer.
```

---

## 🔄 Reset High Scores

Players can reset the leaderboard from the main menu.

The program asks for confirmation:

```text
Are you sure you want to reset all high scores? (yes/no):
```

The scores are deleted only when the player enters:

```text
yes
```

This prevents accidental deletion of the leaderboard.

---

## 🧩 Modular Design

The project is divided into separate Python modules instead of keeping everything in one file.

```text
main.py
   │
   ├── game_logic.py
   │       │
   │       └── game_settings.py
   │
   └── score_management.py
```

This makes the project:

* Easier to understand
* Easier to maintain
* Easier to debug
* Easier to extend
* More organized

---

## 📚 Concepts Demonstrated

This project demonstrates several important Python programming concepts:

* Functions
* Modules
* Imports
* Dictionaries
* Lists
* Loops
* Conditional statements
* Exception handling
* File handling
* JSON data storage
* Random number generation
* User input
* String formatting
* Timestamps
* Basic data persistence
* Modular programming

---

## 🔮 Possible Future Improvements

Some features that could be added in future versions include:

* 🌐 Graphical User Interface (GUI)
* 👥 Multiplayer mode
* ⏱️ Time-based scoring
* 📈 Statistics and performance tracking
* 🔢 Custom number ranges
* 🔊 Sound effects
* 🎨 Different themes
* 🏅 Achievement system
* 📅 Game history
* 📊 Advanced leaderboard statistics

---


