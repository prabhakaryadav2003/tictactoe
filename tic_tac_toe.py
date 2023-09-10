#python 3.7.1
#By Prabhakar Yadav

import random
#checks if gameover
def gameover(state):
  add=0
  times=0
  
  #check rows
  if add<3 and times==0:
    for i in range(0,3):  
      add=add+state[i]
    times=times+1
    
  if add<3 and times==1:
    add=0
    for i in range(3,6):
      add=add+state[i]
    times=times+1
           
  if add<3 and times==2:
    add=0
    for i in range(6,9):
      add=add+state[i]
    times=times+1

  #check columns
        
  if add<3 and times==3: 
    add=0
    for i in range (0,8,3):
      add=add+state[i]
    times=times+1
        
  if add<3 and times==4:
    add=0
    for i in range(1,8,3):
      add=add+state[i]
    times=times+1
       
  if add<3 and times==5:
    add=0
    for i in range(2,9,3):
      add=add+state[i]
    times=times+1

  #check diagonals
        
  if add<3 and times==6:
    add=0
    for i in range(0,9,4):
      add=add+state[i]
    times=times+1
        
  if add<3 and times==7: 
    add=0
    for i in range(2,7,2):
      add=add+state[i]
    times=times+1
    
  if add==3 :
    
    if state==xstate:
      print("X wins\n")
    elif state==ostate:
      print("O wins\n")
    replay()  
    
  elif sum(xstate)+sum(ostate)==9:
      print("It's a tie\n")
      replay()
    
  if add<3 and times==8 :
    turncheck()

#Asks user to replay
def replay():
  
  replay=input("Do you want to play again (Y/N) ? :")
  if replay=="Y" or replay=="y":
    main()   
  elif replay=="N" or replay=="n":
    print("Thank You For Playing") 
    exit()
  else :
    print("Invalid Input!\nPlease enter Y or N")

#Prints x and o in grid  
def changer(block):
  if xstate[block-1]==1 :
    return "X"
  elif ostate[block-1]==1 :
    return "O"
  else :
    return block
    
#Prints board    
def printBoard() :
  
  print(f"\n {changer(1)} | {changer(2)} | {changer(3)} ")
  print("-------------")
  print(f" {changer(4)} | {changer(5)} | {changer(6)} ")
  print("-------------")
  print(f" {changer(7)} | {changer(8)} | {changer(9)} \n")

#initalize game  
def main() :

  print("*"*200)
  print("\nWelcome to tic tac toe\n")

  for i in range(0, 9):
    xstate[i]=0
    ostate[i]=0
  printBoard()
  turncheck()

#checks turn and take input
def turncheck():
  global turn, choice
  valid=("1","2","3","4","5","6","7","8","9")
  while turn==0 :
    choice=(input("O's Turn : "))
    if choice not in valid :
      print("Invalid Input! \nEnter an integer from 1 to 9")
      turncheck() 
    else :
      choice=int(choice)-1
      if xstate[choice]==0 and ostate[choice]==0:
        ostate[choice]=1
      else :
        print("Block already selected \nChoose different block")
        turncheck()
        
    turn=1
    printBoard()
    gameover(ostate)
    turncheck() 
    
  while turn==1 :
    choice=(input("X's Turn : "))
    if choice not in valid :
      print("Invalid Input! \nEnter an integer from 1 to 9")
      turncheck()
    else :
      choice=int(choice)-1
      if xstate[choice]==0 and ostate[choice]==0:
         xstate[choice]=1
      else :
        print("Block already selected \nChoose different block")
        turncheck()
    
    turn=0
    printBoard()
    gameover(xstate)
    turncheck() 
    
#initalizition and define global variables

turn=random.randint(0, 1)
choice=" "
xstate=[0,0,0,0,0,0,0,0,0]
ostate=[0,0,0,0,0,0,0,0,0]
if __name__=='__main__':main()