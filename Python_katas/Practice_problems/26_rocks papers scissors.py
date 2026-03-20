import tkinter as tk
import random
from tkinter import ttk
from tkinter import messagebox

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.comp_score = 0

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Rock Paper Scissors",
                 font=("Arial", 18, "bold")).pack(pady=10)

        self.result_label = ttk.Label(self.root, text="Make your move!",
                                     font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.choice_label = ttk.Label(self.root, text="",
                                     font=("Arial", 11))
        self.choice_label.pack(pady=5)

        self.score_label = ttk.Label(self.root,
                                    text="Score → You: 0 | Computer: 0",
                                    font=("Arial", 12, "bold"))
        self.score_label.pack(pady=10)

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="🪨 Rock", width=12,
                  command=lambda: self.play("r")).grid(row=0, column=0, padx=5)

        ttk.Button(btn_frame, text="📃 Paper", width=12,
                  command=lambda: self.play("p")).grid(row=0, column=1, padx=5)

        ttk.Button(btn_frame, text="✂️ Scissors", width=12,
                  command=lambda: self.play("s")).grid(row=0, column=2, padx=5)

        style = ttk.Style()
        style.configure("Danger.TButton",
                        background="red",
                        font=("Arial", 11, "bold"))

        ttk.Button(self.root, text="Reset Game",
                   command=self.reset_game,
                   style="Danger.TButton").pack(pady=20)

    def play(self, user):
        comp = random.choice(self.choices)

        user_map = {"r": "Rock", "p": "Paper", "s": "Scissors"}
        self.choice_label.config(
            text=f"You chose {user_map[user]} | Computer chose {comp.capitalize()}")

        if user == comp[0]:
            self.result_label.config(text="🤝 It's a Draw!")

        elif (user == "p" and comp == "rock") or \
             (user == "s" and comp == "paper") or \
             (user == "r" and comp == "scissors"):
            self.user_score += 1
            self.result_label.config(text="🎉 You Win this round!")

        else:
            self.comp_score += 1
            self.result_label.config(text="😢 You Lose this round!")

        self.update_score()
        self.check_winner()

    def update_score(self):
        self.score_label.config(
            text=f"Score → You: {self.user_score} | Computer: {self.comp_score}")

    def check_winner(self):
        if self.user_score == 2:
            messagebox.showinfo("Game Over", "🏆 You won the match!")
            self.reset_game()
        elif self.comp_score == 2:
            messagebox.showinfo("Game Over", "💻 Computer won the match!")
            self.reset_game()

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.result_label.config(text="Make your move!")
        self.choice_label.config(text="")
        self.update_score()


# -------- RUN APP --------
root = tk.Tk()
app = RockPaperScissorsGUI(root)
root.mainloop()
