import copy
import math
import random
import numpy

X = "X"
O = "O"
EMPTY = None
user = None
ai = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in board:
        for j in i:
            if j:
                count += 1
    if count % 2 != 0:
        return ai
    return user

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    board_len = len(board)
    for i in range(board_len):
        for j in range(board_len):
            if board[i][j] == EMPTY:
                res.add((i, j))
    return res

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    curr_player = player(board)
    result_board = copy.deepcopy(board)
    (i, j) = action
    result_board[i][j] = curr_player
    return result_board

def get_horizontal_winner(board):
    # check horizontally
    winner_val = None
    board_len = len(board)
    for i in range(board_len):
        winner_val = board[i][0]
        for j in range(board_len):  # Check three consecutive positions
            if board[i][j] != winner_val:
                winner_val = None
        if winner_val:
            return winner_val
    return winner_val

def get_vertical_winner(board):
    # check vertically
    winner_val = None
    board_len = len(board)
    for i in range(board_len):  # Check three consecutive positions
        winner_val = board[0][i]
        for j in range(board_len):
            if board[i][j] != winner_val:
                winner_val = None
        if winner_val:
            return winner_val
    return winner_val

def get_diagonal_winner(board):
    # check diagonally
    winner_val = None
    board_len = len(board)
    winner_val = board[0][0]
    for i in range(board_len):  # Check three consecutive positions
        if board[i][i] != winner_val:
            winner_val = None
    if winner_val:
        return winner_val
    winner_val = board[0][board_len - 1]
    for i in range(board_len):  # Check three consecutive positions
        j = board_len - 1 - i
        if board[i][j] != winner_val:
            winner_val = None
    return winner_val

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner_val = get_horizontal_winner(board) or get_vertical_winner(board) or get_diagonal_winner(board) or None
    return winner_val

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_val = winner(board)
    if winner_val == X:
        return 1
    elif winner_val == O:
        return -1
    return 0

def maxValue(state):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for action in actions(state):
        v = max(v, minValue(result(state, action)))
    return v

def minValue(state):
    if terminal(state):
        return utility(state)
    v = math.inf
    for action in actions(state):
        v = min(v, maxValue(result(state, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    move = None  # Initialize move variable
    if current_player == X:
        min_val = -math.inf
        for action in actions(board):
            check = minValue(result(board, action))
            if check > min_val:
                min_val = check
                move = action
    else:
        max_val = math.inf
        for action in actions(board):
            check = maxValue(result(board, action))
            if check < max_val:
                max_val = check
                move = action
    return move

if __name__ == "__main__":
    board = initial_state()
    ai_turn = False
    print("Choose a player")
    user = input()
    if user == "X":
        ai = "O"
    else:
        ai = "X"
    while True:
        game_over = terminal(board)
        playr = player(board)
        if game_over:
            winner = winner(board)
            if winner is None:
                print("Game Over: Tie.")
            else:
                print(f"Game Over: {winner} wins.")
            break
        else:
            if user != playr and not game_over:
                if ai_turn:
                    move = minimax(board)
                    board = result(board, move)
                    ai_turn = False
                    print(numpy.array(board))
            elif user == playr and not game_over:
                ai_turn = True
                print("Enter the position to move (row,col)")
                i = int(input("Row:"))
                j = int(input("Col:"))
                if board[i][j] == EMPTY:
                    board = result(board, (i, j))
                    print(numpy.array(board))
if __name__ == "__main__":
    board = initial_state()
    ai_turn = False

    print("Choose a player (X or O):")
    user = input()
    if user == X:
        ai = O
    else:
        ai = X

    while True:
        game_over = terminal(board)
        player_turn = player(board)

        if game_over:
            winner_value = winner(board)
            if winner_value is None:
                print("Game Over: Tie.")
            else:
                print(f"Game Over: {winner_value} wins.")
            break
        else:
            if player_turn == ai and not game_over:
                if ai_turn:
                    move = minimax(board)
                    board = result(board, move)
                    ai_turn = False
                    print(numpy.array(board))
            elif player_turn == user and not game_over:
                ai_turn = True
                print("Enter the position to move (row, col)")
                i = int(input("Row: "))
                j = int(input("Col: "))
                if board[i][j] == EMPTY:
                    board = result(board, (i, j))
                    print(numpy.array(board))
                else:
                    print("Invalid move. Cell is not empty.")

import os, math
def GetWinner(board):
  if board[0] == board[1] and board[1] == board[2]:
    return board[0]
  elif board[3] == board[4] and board[4] == board[5]:
    return board[3]
  elif board[6] == board[7] and board[7] == board[8]:
    return board[6]
  elif board[0] == board[3] and board[3] == board[6]:
    return board[0]
  elif board[1] == board[4] and board[4] == board[7]:
    return board[1]
  elif board[2] == board[5] and board[5] == board[8]:
    return board[2]
  # diagonal
  elif board[0] == board[4] and board[4] == board[8]:
    return board[0]
  elif board[2] == board[4] and board[4] == board[6]:
    return board[2]
def PrintBoard(board):
  """
  Clears the console and prints the current board.
  """
  os.system('cls' if os.name=='nt' else 'clear')
  print(f'''
  {board[0]}|{board[1]}|{board[2]}
  {board[3]}|{board[4]}|{board[5]}
  {board[6]}|{board[7]}|{board[8]}
  ''')
def GetAvailableCells(board):
  """
  Returns a list of indices containing all available cells in a board.
  """
  available = list()
  for cell in board:
    if cell != "X" and cell != "O":
      available.append(cell)
  return available
def minimax(position, depth, alpha, beta, isMaximizing):
  winner = GetWinner(position)
  if winner != None:
    return 10 - depth if winner == "X" else -10 + depth
  if len(GetAvailableCells(position)) == 0:
    return 0
  if isMaximizing:
    maxEval = -math.inf
    for cell in GetAvailableCells(position):
      position[cell - 1] = "X"
      Eval = minimax(position, depth + 1, alpha, beta, False)
      maxEval = max(maxEval, Eval)
      alpha = max(alpha, Eval)
      position[cell - 1] = cell
      if beta <= alpha:
        break # prune
    return maxEval
  else:
    minEval = +math.inf
    for cell in GetAvailableCells(position):
      position[cell - 1] = "O"
      Eval = minimax(position, depth + 1, alpha, beta, True)
      minEval = min(minEval, Eval)
      beta = min(beta, Eval)
      position[cell - 1] = cell
      if beta <= alpha:
        break # prune
    return minEval
def FindBestMove(currentPosition, AI):
  bestVal = -math.inf if AI == "X" else +math.inf
  bestMove = -1
  for cell in GetAvailableCells(currentPosition):
    currentPosition[cell - 1] = AI
    moveVal = minimax(currentPosition, 0, -math.inf, +math.inf, False
  if AI == "X" else True)
    currentPosition[cell - 1] = cell
    if (AI == "X" and moveVal > bestVal):
      bestMove = cell
      bestVal = moveVal
    elif (AI == "O" and moveVal < bestVal):
      bestMove = cell
      bestVal = moveVal
  return bestMove
def main():
  player = input("Play as X or O? ").strip().upper()
  AI = "O" if player == "X" else "X"
  currentGame = [*range(1, 10)]
  # X always starts first.
  currentTurn = "X"
  counter = 0
  while True:
    if currentTurn == AI:
      cell = FindBestMove(currentGame, AI)
      currentGame[cell - 1] = AI
      currentTurn = player
    elif currentTurn == player:
      PrintBoard(currentGame)
      while True:
        humanInput = int(input("Enter Number: ").strip())
        if humanInput in currentGame:
            currentGame[humanInput - 1] = player
            currentTurn = AI
            break
        else:
          PrintBoard(currentGame)
          print("Cell Not Available.")
    if GetWinner(currentGame) != None:
      PrintBoard(currentGame)
      print(f"{GetWinner(currentGame)} WON!!!")
      break
    counter += 1
    if GetWinner(currentGame) == None and counter == 9:
      PrintBoard(currentGame)
      print("Tie.")
      break
if __name__ == "__main__":
  main()
  
