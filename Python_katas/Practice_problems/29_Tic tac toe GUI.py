import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x350")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.buttons = [[None]*3 for _ in range(3)]

        self.create_board()
        self.create_reset_button()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def create_reset_button(self):
        reset_btn = tk.Button(
            self.root,
            text="New Game",
            font=("Arial", 12),
            command=self.reset_game
        )
        reset_btn.grid(row=3, column=0, columnspan=3, sticky="we", pady=10)

    def on_click(self, row, col):
        btn = self.buttons[row][col]

        if btn["text"] == "":
            btn["text"] = self.current_player

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} Wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.buttons

        # Rows & Columns
        for i in range(3):
            if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] != "":
                return True
            if b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] != "":
                return True

        # Diagonals
        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] != "":
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] != "":
            return True

        return False

    def check_draw(self):
        for row in self.buttons:
            for btn in row:
                if btn["text"] == "":
                    return False
        return True

    def reset_game(self):
        self.current_player = "X"
        for row in self.buttons:
            for btn in row:
                btn.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
