import tkinter as tk
import random

def play_game(player_choice):
    global player_score, computer_score
    
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    result = determine_winner(player_choice, computer_choice)
    
    result_label.config(text=f"Computer chose {computer_choice}\n{result}", font=("Arial", 14, "bold"), fg=get_result_color(result))
    
    update_scores(result)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def update_scores(result):
    global player_score, computer_score
    if "You win" in result:
        player_score += 1
    elif "Computer wins" in result:
        computer_score += 1
    
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score}", font=("Arial", 14))

def replay_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score}", font=("Arial", 14))
    result_label.config(text="Choose your move", font=("Arial", 14, "italic"), fg="black")

def stop_game():
    root.destroy()

def get_result_color(result):
    if "You win" in result:
        return "green"
    elif "Computer wins" in result:
        return "red"
    else:
        return "black"

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Global variables for scores
player_score = 0
computer_score = 0

# Create buttons for player choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"), font=("Arial", 12))
paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"), font=("Arial", 12))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"), font=("Arial", 12))

# Create buttons for game control
replay_button = tk.Button(root, text="Replay", command=replay_game, font=("Arial", 12))
stop_button = tk.Button(root, text="Stop", command=stop_game, font=("Arial", 12))

# Create a label to display the result
result_label = tk.Label(root, text="Choose your move", font=("Arial", 14, "italic"), fg="black")

# Create a label to display the scores
score_label = tk.Label(root, text=f"Player: {player_score} | Computer: {computer_score}", font=("Arial", 14))

# Create labels for game instructions
instruction_lines = [
    "Instructions:",
    "1. Rock beats scissors.",
    "2. Scissors beat paper.",
    "3. Paper beats rock."
]

instructions_labels = [tk.Label(root, text=line, font=("Arial", 12, "italic")) for line in instruction_lines]

# Place the widgets in the grid
for i, label in enumerate(instructions_labels):
    label.grid(row=i, column=0, columnspan=3, pady=2)

rock_button.grid(row=len(instruction_lines), column=0, padx=10, pady=10)
paper_button.grid(row=len(instruction_lines), column=1, padx=10, pady=10)
scissors_button.grid(row=len(instruction_lines), column=2, padx=10, pady=10)
replay_button.grid(row=len(instruction_lines)+1, column=0, padx=10, pady=10)
stop_button.grid(row=len(instruction_lines)+1, column=2, padx=10, pady=10)
result_label.grid(row=len(instruction_lines)+2, column=0, columnspan=3, pady=10)
score_label.grid(row=len(instruction_lines)+3, column=0, columnspan=3, pady=10)

# Run the Tkinter event loop
root.mainloop()
