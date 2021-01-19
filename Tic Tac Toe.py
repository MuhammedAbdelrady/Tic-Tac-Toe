#---------------Globel Variables------
game_still_going = True
winner= None
current_player="X"
#---------------Finish Of The global Variables---------
#Alligin The Game Border
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
#Show Game Border
def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])


#------Main Loop For Calling All other Functions
def play_game():
    display_board()     #to display the layout border
    while game_still_going:         #loop
        #First level
        handle_turn (current_player)
        #Second level to check if the game is over or not
        check_if_game_over()
        #swap between the two players if the game not finished
        flip_player()
    #Print The Winner
    if winner == "X" or winner == "O":
      print (winner + "  won.")
      print ("Congratulation.")
    elif winner == None :
      print("Tie.")


###################First level#####################
def handle_turn(player):
    position = input("Choose a position from 1 to 9: ")
    position = int(position)-1
    board[position]=player
    display_board()


##################Second Level#######################
def check_if_game_over ():
    check_if_win()
    check_if_tie()

def check_if_tie():
    return
def check_if_win():
    global winner
    #we must check rows , column and diagonals
    row_winner=check_rows()
    column_winner=check_column()
    diagonal_winner=check_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner :
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going
    row_1=board[0]==board[1]==board[2] != "-"
    row_2=board[3]==board[4]==board[5] != "-"
    row_3=board[6]==board[7]==board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going=False
    if row_1:
        return board[0]
    elif row_2 :
        return board[3]
    elif row_3:
        return board[6]
    return

def check_column():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

################Third Level ######################
#Used For Taake Turnes for each two signs <"X" & "O">
def flip_player ():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return

play_game()