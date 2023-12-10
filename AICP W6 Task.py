#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Step 1: Initialize the board as a list of empty spaces
board = [" " for _ in range(9)]

# Step 2: Defining all the possible winning combinations
winning_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

# Step 3: Function to display the game board
def display_board():
    for i in range(0,9,3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--|---|--")

# Step 4:Checking if a player has won
def check_winner(player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Step 5: Checking if the board is full
def is_board_full():
    return " " not in board

# Step 6: Now this the the main loop for the game
current_player = "X"

while True:
    display_board()

    # Step 7: Get the player's move
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

    # Step 8: Checking if the space chosen by they player is empty
    if board[move] == " ":
        board[move] = current_player
    else:
        print("Invalid move. The space is already taken. Try again.")
        continue

    # Step 9: Checking if the current player has won
    if check_winner(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break

    # Step 10: Checking if the board is full to make a tie
    if is_board_full():
        display_board()
        print("It's a tie!")
        break

    # Step 11: Switching from one player to another
    current_player = "O" if current_player == "X" else "X"


# In[ ]:




