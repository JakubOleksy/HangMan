import tkinter as tk
from tkinter import messagebox
import random

# Load words from file
with open("words.txt", "r") as file:
    words = file.read().splitlines()

# Select a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

def update_display():
    display_word.set(" ".join(guessed))
    display_attempts.set(f"Attempts left: {attempts}")

def guess(letter):
    global attempts
    if letter in word:
        for index, char in enumerate(word):
            if char == letter:
                guessed[index] = letter
    else:
        attempts -= 1
        draw_hangman(attempts)
    update_display()
    check_win_loss()

def draw_hangman(attempts):
    # This function will draw the hangman step by step
    # For simplicity, it's not implemented in this example
    pass

def check_win_loss():
    if "_" not in guessed:
        messagebox.showinfo("Hangman", "You won!")
        root.destroy()
    elif attempts <= 0:
        messagebox.showinfo("Hangman", f"You lost! The word was: {word}")
        root.destroy()

root = tk.Tk()
root.title("Hangman Game")

display_word = tk.StringVar()
display_attempts = tk.StringVar()

tk.Label(root, textvariable=display_word, font=('Helvetica', 24)).pack()
tk.Label(root, textvariable=display_attempts, font=('Helvetica', 14)).pack()

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    tk.Button(root, text=letter, command=lambda l=letter: guess(l)).pack(side="left")

update_display()

root.mainloop()
