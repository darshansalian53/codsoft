import tkinter as tk
import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = user_choice_var.get().lower()

    result_label.config(text=f"Computer chose: {computer_choice}\nYou chose: {user_choice}")

    if computer_choice == user_choice:
        result_label.config(text=result_label.cget("text") + "\nIt's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        result_label.config(text=result_label.cget("text") + "\nYou win!")
    else:
        result_label.config(text=result_label.cget("text") + "\nComputer wins!")

    play_button.config(state=tk.DISABLED)
    play_again_button.config(state=tk.NORMAL)

def play_again():
    user_choice_var.set("")
    result_label.config(text="")
    play_button.config(state=tk.NORMAL)
    play_again_button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x300")

user_choice_label = tk.Label(root, text="Enter your choice (Rock , Paper, or Scissors):", font ="normal 20 bold", fg="red")
user_choice_label.pack()
user_choice_var = tk.StringVar()
user_choice_entry = tk.Entry(root, textvariable=user_choice_var, font=('consolas', 20), width=20 )
user_choice_entry.pack()

play_button = tk.Button(root, text="Play", command=play_game ,font="normal 20 ",bg="white", borderwidth=3 )
play_button.pack()
play_button.pack( pady=20)

play_again_button = tk.Button(root, text="Play Again", command=play_again, state=tk.DISABLED, font="normal 20", bg="white", borderwidth=3)
play_again_button.pack()

result_label = tk.Label(root, text="" , font="normal 15", fg="red")
result_label.pack()

root.mainloop()