from tkinter import E


def show_game_board():
    for row in game:
        for item in row:
              print(item,end=" ")
        print()

game=[['-','-','-'],
      ['-','-','-'],
      ['-','-','-']]

save_move1_row=[]
save_move1_col=[]
save_move2_row=[]
save_move2_col=[]

def choose():
    
    while(1):
        roww=input("row : ")
        if (  roww.isdigit() and int(roww)>=0 and int(roww)<=2 ):
                 row=int(roww)
                 break
        else:
            print("enter beetwen 0 and 3")
   
    while(1):
        coll=(input("col : "))
       
        if( coll.isdigit() and int(coll)>=0 and int(coll)<=2  ):
                col=int(coll)
                break
        else:
                 print("enter beetwen 0 and 3")
    return row , col




def check():
    special_condition1 = 0
    for i in range (0, len(save_move1_col)):
        win = 1
        win1 = 1    
        if (save_move1_col[i]==save_move1_row[i]):
            special_condition1 += 1  
        for j in range (i+1, len(save_move1_col)):
                  
            
            if save_move1_col[i]==save_move1_col[j]:
                    win+=1
                    if(win==3):
                        break
            elif save_move1_row[i]==save_move1_row[j]:
                    win1+=1
                    if(win1==3):
                        break
        if(win==3 or win1 == 3 or special_condition1 ==3):
            print (" winner is player1")
            return True
            break
        
    special_condition2 = 0
    for i in range (0, len(save_move2_col)):
        win2 = 1
        win3 = 1
        if (save_move2_col[i]==save_move2_row[i]):
            special_condition2 += 1
        for j in range (i+1, len(save_move2_col)):
                  
            
            if save_move2_row[i]==save_move2_row[j]:
                    win2+=1
                    if(win2==3):
                        break
            elif save_move2_col[i]==save_move2_col[j]:
                    win3+=1
                    if(win3==3):
                        break
        
        if(win2==3 or win3 == 3 or special_condition2==3):
            print (" winner is player2")
            return True
            break
    if(game[1][1]==game[0][2]==game[2][0]=="x"):
        print (" winner is player1")
        return True
    elif(game[1][1]==game[0][2]==game[2][0]=="o"):
        print (" winner is player2")
        return True


round = 0  
while (1):
    
    while(1):
    
        print("player1")
        row , col=choose()
        if (game[row][col] == '-') :
            game[row][col]='x'
            save_move1_row.append(row)
            save_move1_col.append(col)
            break
        else :
            print("deghat kon")

    show_game_board()
    round  += 1
    
    if check() :
        break
    elif round ==9:
        print ("We dont have winner")
        break

    while(1):

        print("player2")
        row,col=choose()
        if( game[row][col] == '-') :
            game[row][col]='o'
            save_move2_row.append(row)
            save_move2_col.append(col)
            
            break
        else :
            print("deghat kon")
            
    show_game_board()
    round += 1
    
    
    if check() :
        break

    
    

