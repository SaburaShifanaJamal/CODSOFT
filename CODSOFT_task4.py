import tkinter as tk
from tkinter import messagebox
import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"
def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    if result == "tie":
        message = f"It's a tie! Computer also chose {computer_choice}."
    elif result == "win":
        global user_score
        user_score += 1
        message = f"You win! Computer chose {computer_choice}."
    else:
        global computer_score
        computer_score += 1
        message = f"You lose! Computer chose {computer_choice}."

    result_label.config(text=message)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
def play_again():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
    result_label.config(text="Choose rock, paper, or scissors!")
user_score = 0
computer_score = 0
root = tk.Tk()
root.title("Rock, Paper, Scissors")
instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:")
instruction_label.pack()
rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
rock_button.pack(side=tk.LEFT)
paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
paper_button.pack(side=tk.LEFT)
scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))
scissors_button.pack(side=tk.LEFT)
result_label = tk.Label(root, text="Choose rock, paper, or scissors!")
result_label.pack()
score_label = tk.Label(root, text=f"Score - You: {user_score} | Computer: {computer_score}")
score_label.pack()
play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack()
root.mainloop()
