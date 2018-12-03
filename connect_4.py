





def draw_board(size):
   board = []
   x= 0
   while x < size:
      board = board + [[""]*size]
      x=x+1
   return board
def print_board(board):
   nice_board = ""
   nums = ""
   for x in range(len(board)):
      for y in range(len(board[x])):
         if str(board[x][y]) == "":
            nice_board = nice_board + "[ ]"
         else:
            nice_board = nice_board + "[" + str(board[x][y]) + "]"
         if y==(len(board)-1):
            print(nice_board)
            nice_board = ''
   for i in range(len(board)):
      nums = nums + " " + str(i)+ "|"
   
   print(nums)
   return nice_board


def choose_your_character():
   valid_response = False
   while valid_response == False:
      player_1 = str(input("Player 1 choose your sign. (Must be a single character)"))
      player_2 = str(input("Player 2 choose your sign. (Must be a single character)"))
      board_size = int(input("How big should the board be? (Integers only!)"))
      if (len(player_1) == 1) and (len(player_2) == 1):
            valid_response = True
        
   return(player_1,player_2,board_size)



def what_column(player):
   res = int(input("What column " + str(player) + "?(choose the corresponding integer seen on the board) "))
   return res

def piece_location(board,num):
   valid_response = False
   while valid_response ==False:
      for x in range(len(board)-1,-2,-1):
         if x == 0 and board[0][num]=="":
            valid_response = True
            return "zero"           
         elif board[x][num] == "":
            print(x)
            valid_response = True
            return x
         elif board[0][num] != "":
            valid_response = True
            return False
      
    


def string_length(board,character):
   row_counter = 0
   col_counter = 0
   longest_string = 0
   for row in range(len(board)):
      row_counter = 0
      for char in range(len(board[row])):
         if board[row][char] == character:
            row_counter = row_counter + 1
            
         else:
            longest_string_new = row_counter
            row_counter = 0
            if longest_string_new > longest_string:
               longest_string = longest_string_new
         if char == len(board[row])-1:
            longest_string_new = row_counter
            if longest_string_new > longest_string:
               longest_string = longest_string_new
   for col in range(len(board)):
      col_counter = 0
      for char in range(len(board[col])):
         if board[char][col] == character:
            col_counter = col_counter + 1
               
         else:
            longest_string_new = col_counter
            col_counter = 0
            if longest_string_new > longest_string:
               longest_string = longest_string_new
         if char == len(board[col])-1:
               longest_string_new = col_counter
               if longest_string_new > longest_string:
                  longest_string = longest_string_new            
   for dev in range(len(board)-3):
         accum_1 = 0
         accum_2 = 0
         accum_3 = 0
         accum_4 = 0
         for iter1 in range(len(board)-dev):
            if board[iter1][iter1+dev]== character:
               accum_1 = accum_1 + 1
            else:
               longest_string_new = accum_1
               accum_1 = 0
               if longest_string_new > longest_string:
                  longest_string = longest_string_new
            if iter1 == len(board)-dev-1:
               longest_string_new = accum_1
               if longest_string_new > longest_string:
                  longest_string = longest_string_new
        
         for iter2 in range(len(board)-dev):
            if board[iter2+dev][iter2]== character:
               accum_2 = accum_2 + 1
            else:
               longest_string_new = accum_2
               accum_2 = 0
               if longest_string_new > longest_string:
                  longest_string = longest_string_new
            if iter2 == len(board)-dev-1:
               longest_string_new = accum_2
               if longest_string_new > longest_string:
                  longest_string = longest_string_new
        
         for iter3 in range(len(board)-dev):
            if board[len(board)-1-iter3][iter3+dev]== character:
               accum_3 = accum_3 + 1
         else:
            longest_string_new = accum_3
            accum_3 = 0
            if longest_string_new > longest_string:
                  longest_string = longest_string_new
         if iter3 == len(board)-dev-1:
            longest_string_new = accum_3
            if longest_string_new > longest_string:
               longest_string = longest_string_new
         for iter4 in range(len(board)-dev):
            if board[len(board)-1-iter4-dev][iter4]== character:
               accum_4 = accum_4 + 1
            else:
               longest_string_new = accum_4
               accum_4 = 0
               if longest_string_new > longest_string:
                  longest_string = longest_string_new
            if iter4 == len(board)-dev-1:
               longest_string_new = accum_4
               if longest_string_new > longest_string:
                  longest_string = longest_string_new
   return longest_string





def is_stalemate(board):
   test_done = False
   while test_done == False:
      for x in range(len(board)):
         for y in range(len(board[x])):
            if board[x][y] == "":
               test_done = True
               return False
      if test_done == False:
         test_done = True
         return True
    
def connect_4():
    
   (player_1_sym,player_2_sym,size) = choose_your_character()
   board = draw_board(size)
   print_board(board)
   game_over = False
   while game_over == False:
      player1_ans = False
      player2_ans = False        
      y = what_column("player_1")  
      x = piece_location(board,y)
      
      if x == False:
         print("That column is full, pick another!")
         y = what_column("player_1")
      
      else:
         if x == "zero":
            x = 0
         board[x][y] = board[x][y]+ player_1_sym
         print_board(board)
         if string_length(board, player_1_sym) > 3:
            game_over = True
            print("Player 1 successfully connected 4!")
            break
         elif is_stalemate(board) == True:
            game_over = True
            print("You both lost!")
            break
      y = what_column("player_2")
      x = piece_location(board,y)
                  
      if x == False:
         print("That column is full, pick another!")
      
      else:
         if x == "zero":
            x = 0
         board[x][y] = player_2_sym
         print_board(board)
         if string_length(board, player_2_sym) > 3:
            game_over = True
            print("Player 2 successfully connected 4!")
         elif is_stalemate(board) == True:
            game_over = True
            print("You both lost!")        
         
connect_4()
