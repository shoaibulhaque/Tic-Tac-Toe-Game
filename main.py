from random import randrange

def display_board(board):
  print("+-------" * 3,"+", sep="")
  for row in range(3):
    print("|       " * 3,"|", sep="")
    for col in range(3):
      print("|   " + str(board[row][col]) + "   ", end="")
    print("|")
    print("|       " * 3,"|",sep="")
    print("+-------" * 3,"+",sep="")


def enter_move(board, filled_index, eq_values):  
  while True:
    user_mov = int(input("Enter your move:"))
    if user_mov < 0 or user_mov > 10:
      print("Invalid choice  !")
      continue

    else:
      if user_mov not in filled_index.keys():
        row, col = eq_values[user_mov]
        board[row][col] = 'O'
        filled_index[user_mov] = 'O'
        break
      
      else:
        print("Field is already filled !")
        continue

    
      

def victory_for(board, sgn):
  if sgn == "X":	# are we looking for X?
    who = 'me'	# yes - it's computer's side
  elif sgn == "O": # ... or for O?
    who = 'you'	# yes - it's our side
  else:
    who = None	# we should not fall here!
  cross1 = cross2 = True  # for diagonals
  for rc in range(3):
    if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
      return who
    if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
      return who
    if board[rc][rc] != sgn: # check 1st diagonal
      cross1 = False
    if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
      cross2 = False
  if cross1 or cross2:
    return who
  return None
  
  
  


def draw_move(board, filled_index,eq_values):

  while True:
    print("draw_move")
    comp_move = randrange(1, 10)
    if comp_move not in filled_index.keys():
      row, col = eq_values[comp_move]
      board[row][col] = 'X'
      filled_index[comp_move] = 'X'
      break
      
    else:
      continue
      

  
  
  
eq_values = {1: (0,0),2: (0,1), 3: (0,2),4: (1,0),6: (1,2),7:(2,0),8: (2,1), 9:(2,2)}
board = [[1,2,3],[4,"X",6],[7,8,9]]
filled_index = {5: 'X'}


hum_turn = True
while True:
  display_board(board)
  if hum_turn:
    enter_move(board,filled_index,eq_values)
    victor = victory_for(board, 'O')
  else:
    draw_move(board,filled_index,eq_values)
    victor = victory_for(board, 'X')

  if victor != None:
    break

  if len(filled_index) == 9:
    break
    
  hum_turn = not hum_turn



display_board(board)
if victor == "me":
  print("I won")

elif victor == "you":
  print("you won !")

else:
  print("Tie !")


