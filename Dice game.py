import tkinter as tk
import random

class DiceGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dice Game: Beat the Computer ????")

        # Labels for displaying player and computer dice results
        self.player_label = tk.Label(self.window, text="Your Roll: ??", font=("Arial", 24))
        self.player_label.pack(pady=10)

        self.computer_label = tk.Label(self.window, text="Computer Roll: ??", font=("Arial", 24))
        self.computer_label.pack(pady=10)

        self.result_label = tk.Label(self.window, text="Press Roll to Start!", font=("Arial", 28, "bold"), fg="blue")
        self.result_label.pack(pady=20)

        # Roll button
        self.roll_button = tk.Button(self.window, text="Roll Dice ??", font=("Arial", 20), command=self.play_game)
        self.roll_button.pack(pady=30)

    def play_game(self):
        # Player's dice roll
        player_roll = random.randint(1, 6)
        self.player_label.config(text=f"Your Roll: ?? {player_roll}")

        # Computer's dice roll
        computer_roll = random.randint(1, 6)
        self.computer_label.config(text=f"Computer Roll: ?? {computer_roll}")

        # Determine the winner
        if player_roll > computer_roll:
            self.result_label.config(text="You Win! ??", fg="green")
        elif player_roll < computer_roll:
            self.result_label.config(text="Computer Wins! ??", fg="red")
        else:
            self.result_label.config(text="It's a Tie! ?????", fg="orange")

    def run(self):
        self.window.mainloop()

# Run the Dice Game
app = DiceGame()
app.run()
