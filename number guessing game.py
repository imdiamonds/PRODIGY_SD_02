import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.generated_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess the number (between 1 and 100):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1

            if user_guess == self.generated_number:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.generated_number} in {self.attempts} attempts.")
                self.master.destroy()
            elif user_guess < self.generated_number:
                messagebox.showinfo("Incorrect Guess", "Too low! Try again.")
            else:
                messagebox.showinfo("Incorrect Guess", "Too high! Try again.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()