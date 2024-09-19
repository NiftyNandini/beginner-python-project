import tkinter as tk
from tkinter import messagebox
import random

class MemoryPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game 🧠")
        self.root.configure(bg="#2E2E2E")
        self.buttons = []
        self.cards = []
        self.first_card = None
        self.second_card = None
        self.attempts = 0
        self.matched_pairs = 0

        self.create_cards()
        self.shuffle_cards()
        self.create_grid()

    def create_cards(self):
        emojis = ["😀", "🐶", "🍎", "🚗", "🎈", "🌟", "🎵", "🏀"]  # Example emojis
        self.cards = emojis * 2  # Two of each card for matching pairs

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def create_grid(self):
        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(self.root, text="?", font=("Helvetica", 20), width=5, height=3,
                                   bg="#3B3B3B", fg="#FFFFFF", command=lambda i=i, j=j: self.on_card_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

    def on_card_click(self, i, j):
        button = self.buttons[i][j]
        if button["text"] == "?" and not self.first_card:
            self.first_card = (i, j)
            button.config(text=self.cards[i * 4 + j])
        elif button["text"] == "?" and self.first_card:
            self.second_card = (i, j)
            button.config(text=self.cards[i * 4 + j])
            self.root.after(500, self.check_match)

    def check_match(self):
        if self.cards[self.first_card[0] * 4 + self.first_card[1]] == self.cards[self.second_card[0] * 4 + self.second_card[1]]:
            self.buttons[self.first_card[0]][self.first_card[1]].config(bg="#4CAF50")
            self.buttons[self.second_card[0]][self.second_card[1]].config(bg="#4CAF50")
            self.matched_pairs += 1
            if self.matched_pairs == len(self.cards) // 2:
                messagebox.showinfo("Congratulations!", f"You won the game in {self.attempts} attempts!")
        else:
            self.buttons[self.first_card[0]][self.first_card[1]].config(text="?", bg="#3B3B3B")
            self.buttons[self.second_card[0]][self.second_card[1]].config(text="?", bg="#3B3B3B")

        self.first_card = None
        self.second_card = None
        self.attempts += 1

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryPuzzleGame(root)
    root.mainloop()
