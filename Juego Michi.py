import time
#PROYECTO MICHI (TIC TAC TOE):
# - La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
# - El usuario (por ejemplo, tu) jugará utilizando las 'O's.
# - El primer movimiento es de la maquina: siempre coloca una 'X' en el
#   centro del tablero.
# - Todos los cuadros están numerados comenzando con el 1 hasta el 9.
# - El usuario ingresa su movimiento introduciendo el numero de cuadro
#   elegido. El numero debe de ser valido, por ejemplo un valor entero mayor
#   que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
# - El programa verifica si el juego ha terminado.
#   Existen cuatro posibles veredictos: el juego continua, el juego termina
#   en empate, tu ganas, o la maquina gana.
# - La maquina responde con su movimiento y se verifica el estado del juego.
# - No se debe implementar algún tipo de inteligencia artificial, la maquina
#   elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

board=[[1,2,3],[4,"X",6],[7,8,9]]
def lista():
    global pc
    pc=[]
    for i in board:
        for j in i:
            if j!="O" and j!="X":
                pc.append(j)
            else:
                continue
    

def DisplayBoard():
    print("\
+-------+-------+-------+\n\
+       +       +       +\n\
+  ",board[0][0],"  +  ",board[0][1],"  +  ",board[0][2],"  +  \n\
+       +       +       +\n\
+-------+-------+-------+")
    print("\
+-------+-------+-------+\n\
+       +       +       +\n\
+  ",board[1][0],"  +  ",board[1][1],"  +  ",board[1][2],"  +  \n\
+       +       +       +\n\
+-------+-------+-------+")
    print("\
+-------+-------+-------+\n\
+       +       +       +\n\
+  ",board[2][0],"  +  ",board[2][1],"  +  ",board[2][2],"  +  \n\
+       +       +       +\n\
+-------+-------+-------+")

def EnterMove():
    move=int(input("Ingreso tu movimiento:"))
    if move==board[0][0]:
        board[0][0]="O"
        DisplayBoard()

    elif move==board[0][1]:
        board[0][1]="O"
        DisplayBoard()

    elif move==board[0][2]:
        board[0][2]="O"
        DisplayBoard()

    elif move==board[1][0]:
        board[1][0]="O"
        DisplayBoard()

    elif move==board[1][1]:
        board[1][1]="O"
        DisplayBoard()

    elif move==board[1][2]:
        board[1][2]="O"
        DisplayBoard()

    elif move==board[2][0]:
        board[2][0]="O"
        DisplayBoard()

    elif move==board[2][1]:
        board[2][1]="O"
        DisplayBoard()   

    elif move==board[2][2]:
        board[2][2]="O"
        DisplayBoard()
     

def DrawMove():
         print("Me toca, dejame pensar...")
         time.sleep(4)
         lista()
         import random
         a=random.choice(pc)
         print(a)
         if a==board[0][0]:
            board[0][0]="X"
            DisplayBoard()
            print("Listo!, tu turno..\t")
            
         elif a==board[0][1]:
            board[0][1]="X"
            DisplayBoard()
            print("Listo!, tu turno..\t")

         elif a==board[0][2]:
            board[0][2]="X"
            DisplayBoard()
            print("Listo!, tu turno..\t")

         elif a==board[1][0]:
            board[1][0]="X"
            DisplayBoard()
            print("Listo!, tu turno..\t")

         elif a==board[1][1]:
            board[1][1]="X"
            DisplayBoard()
            print("Listo!, tu turno..\t")

         elif a==board[1][2]:
            board[1][2]="X"
            DisplayBoard()
            print("Listo!, tu turno..\t")

         elif a==board[2][0]:
            board[2][0]="X"
            DisplayBoard()
            print("Listo!, tu turno..\t")

         elif a==board[2][1]:
            board[2][1]="X"
            DisplayBoard()
            print("Listo!, tu turno..\t")

         elif a==board[2][2]:
            board[2][2]="X"
            DisplayBoard()
            print("Listo!, tu turno..\t")
         
            
def VictoryFor():
 while True:
        EnterMove()
 #Lista en caso usted gane
        if ["O","O","O"] in board:
            print("Usted a ganado")
            return False
            
        elif board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
            print("Usted a ganado")
            return False
       
        elif board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
            print("Usted a ganado")
            return False
          
        
  #Lista en caso usted gane
      
         
        else:
            DrawMove()
            if board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
                print("Lo lamento, pero soy una computadora por algo noob")
                return False
            
            elif board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
                print("Lo lamento, pero soy una computadora por algo noob")
                return False
                
            elif board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
                print("Lo lamento, pero soy una computadora por algo noob")
                return False
            elif board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
                print("Lo lamento, pero soy una computadora por algo noob")
                return False
                
            elif board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
                print("Lo lamento, pero soy una computadora por algo noob")
                return False
              
            elif ["X","X","X"] in board:
                print("Lo lamento, pero soy una computadora por algo noob")
                return False
        

DisplayBoard()
VictoryFor()



time.sleep(5)    
    
        
