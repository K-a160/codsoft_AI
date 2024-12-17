import tkinter as tk
from tkinter import messagebox
import sys
import random

# Constants for players
HUMAN_PLAYER = 'X'
AI_PLAYER = 'O'

# Function to check if the board has a winner
def check_winner(board, player):
    # Check horizontal, vertical, and diagonal lines
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full (tie condition)
def is_full(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, AI_PLAYER):
        return 10 - depth
    if check_winner(board, HUMAN_PLAYER):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -sys.maxsize
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = AI_PLAYER
                    evaluation = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = '-'
                    max_eval = max(max_eval, evaluation)
                    alpha = max(alpha, evaluation)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = sys.maxsize
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = HUMAN_PLAYER
                    evaluation = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = '-'
                    min_eval = min(min_eval, evaluation)
                    beta = min(beta, evaluation)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for AI
def find_best_move(board):
    best_val = -sys.maxsize
    best_move = (-1, -1)
    alpha = -sys.maxsize
    beta = sys.maxsize

    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                board[row][col] = AI_PLAYER
                move_val = minimax(board, 0, False, alpha, beta)
                board[row][col] = '-'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (row, col)
    return best_move

# Function to print the board (optional, for debugging)
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# GUI Class
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_widgets()
    
    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text='-', font=('Arial', 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.player_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    
    def player_move(self, row, col):
        if self.board[row][col] == '-':
            self.board[row][col] = HUMAN_PLAYER
            self.buttons[row][col].config(text=HUMAN_PLAYER)
            if check_winner(self.board, HUMAN_PLAYER):
                messagebox.showinfo("Game Over", "Congratulations! You win!")
                self.reset_board()
                return
            elif is_full(self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
                return
            self.ai_move()
    
    def ai_move(self):
        row, col = find_best_move(self.board)
        self.board[row][col] = AI_PLAYER
        self.buttons[row][col].config(text=AI_PLAYER)
        if check_winner(self.board, AI_PLAYER):
            messagebox.showinfo("Game Over", "AI wins! Better luck next time!")
            self.reset_board()
        elif is_full(self.board):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_board()
    
    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = '-'
                self.buttons[row][col].config(text='-')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()