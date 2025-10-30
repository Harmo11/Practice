
import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number Game")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="I'm thinking of a number between 1 and 100.")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.number_to_guess:
                self.result_label.config(text="Too low!")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high!")
            else:
                self.result_label.config(text=f"Correct! You guessed it in {self.attempts} attempts.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

root = tk.Tk()
game = GuessNumberGame(root)
root.mainloop()
