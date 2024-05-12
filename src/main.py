import tkinter as tk
from tkinter import messagebox
import random

# Load words from file
with open("words.txt", "r") as file:
    words = file.read().splitlines()

# Select a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 10

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
    canvas.delete("hangman")
    parts = [lambda: canvas.create_line(50, 130, 100, 130, tag="hangman"),
             lambda: canvas.create_line(75, 130, 75, 30, tag="hangman"),
             lambda: canvas.create_line(75, 30, 125, 30, tag="hangman"),
             lambda: canvas.create_line(125, 30, 125, 50, tag="hangman"),
             lambda: canvas.create_oval(115, 50, 135, 70, tag="hangman"),
             lambda: canvas.create_line(125, 70, 125, 100, tag="hangman"),
             lambda: canvas.create_line(125, 80, 105, 90, tag="hangman"),
             lambda: canvas.create_line(125, 80, 145, 90, tag="hangman"),
             lambda: canvas.create_line(125, 100, 105, 110, tag="hangman"),
             lambda: canvas.create_line(125, 100, 145, 110, tag="hangman")]
    for i in range(len(parts) - attempts):
        parts[i]()

def display_death_screen():
    canvas.delete("all")
    canvas.create_text(100, 60, text="YOU DIED", font=('Helvetica', 30, 'bold'), fill="red", tag="death")

def check_win_loss():
    if "_" not in guessed:
        messagebox.showinfo("Hangman", "You won!")
        root.destroy()
    elif attempts <= 0:
        display_death_screen()
        root.after(2000, root.destroy)

root = tk.Tk()
root.title("Hangman Game")

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

display_word = tk.StringVar()
display_attempts = tk.StringVar()

tk.Label(root, textvariable=display_word, font=('Helvetica', 24)).pack()
tk.Label(root, textvariable=display_attempts, font=('Helvetica', 14)).pack()

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    tk.Button(root, text=letter, command=lambda l=letter: guess(l)).pack(side="left")

update_display()

root.mainloop()
