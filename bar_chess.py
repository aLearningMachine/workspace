# territory chess
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as ptc

# Parameters
board_size = 4


# Functions

def draw_board(Ver,Ter,Ter_state,Bar,Bar_state):
    Sratio = 0.85
    Barwidth = 0.05
    fig1, ax = plt.subplots()
    ax.scatter(Ver[:,0],Ver[:,1],c = 'black')
    
    for i in range(Ter.shape[0]):
        if Ter_state[i] == 1: # Red territory
            ax.add_patch(ptc.Rectangle(Ter[i,:]-[Sratio,Sratio], Sratio*2, Sratio*2, linewidth=1, edgecolor='r', facecolor='r', alpha = 0.5))
        elif Ter_state[i] == -1: # Blue territory
            ax.add_patch(ptc.Rectangle(Ter[i,:]-[Sratio,Sratio], Sratio*2, Sratio*2, linewidth=1, edgecolor='b', facecolor='b', alpha = 0.5))
    for i in range(Bar.shape[0]):
        plt.text(Bar[i,0]-0.15, Bar[i,1]-0.15, str(i), fontsize=10)
        if Bar_state[i] == 1: # Red bar
            if Bar[i,1]%2 == 1: 
                ax.add_patch(ptc.Rectangle(Bar[i,:]-[0.5*Barwidth,Sratio], Barwidth, Sratio*2, linewidth=1, edgecolor='r', facecolor='r', alpha = 0.9))
            else: 
                ax.add_patch(ptc.Rectangle(Bar[i,:]-[Sratio,0.5*Barwidth], Sratio*2, Barwidth, linewidth=1, edgecolor='r', facecolor='r', alpha = 0.9))
        elif Bar_state[i] == -1: # Blue bar
            if Bar[i,1]%2 == 1: 
                ax.add_patch(ptc.Rectangle(Bar[i,:]-[0.5*Barwidth,Sratio], Barwidth, Sratio*2, linewidth=1, edgecolor='b', facecolor='b', alpha = 0.9))
            else: 
                ax.add_patch(ptc.Rectangle(Bar[i,:]-[Sratio,0.5*Barwidth], Sratio*2, Barwidth, linewidth=1, edgecolor='b', facecolor='b', alpha = 0.9))
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()


def mat_gen(board_size):
    Ter = []; Bar = []; Ver = []; 

    for i in range(2*board_size+1):
        for j in range(2*board_size+1):
            if (i+j)%2 == 1:
                Bar.append([i,j])
            else:
                if (i)%2 == 1:
                    Ter.append([i,j])
                else:
                    Ver.append([i,j])

    Ter = np.array(Ter); Bar = np.array(Bar); Ver = np.array(Ver); 

    Ter_state = np.zeros((Ter.shape[0],1),dtype = 'int'); Bar_state = np.zeros((Bar.shape[0],1),dtype = 'int')
    
    return Ter, Ter_state, Bar, Bar_state, Ver



Ter, Ter_state, Bar, Bar_state, Ver = mat_gen(board_size)
print(Bar)



flag_team = 1 # 1 - Red; -1 - Blue

while int(sum(abs(Ter_state))) < np.shape(Ter)[0]:  # Red starts first
    flag_newTer = 1
    while flag_newTer == 1:
        
        draw_board(Ver,Ter,Ter_state,Bar,Bar_state)
        
        flag_newTer = 0
        neutralBar = 0
        while neutralBar == 0:
            if flag_team == 1:
                input_bar = input("Team Red, input chosen bar: ")
            else:
                input_bar = input("Team Blue, input chosen bar: ")
            input_bar = int(input_bar)
            
            if np.isin(input_bar,np.arange(np.shape(Bar)[0])) and Bar_state[input_bar] == 0:
                neutralBar = 1
            else:
                print("The chosen bar is already taken or out of range, pick another one.")
                neutralBar = 0
        
        
        Bar_state[input_bar] = flag_team
        
        
        
# =============================================================================
#         # Find the neighbouring Ter
#         if Bar[input_bar,1]%2 == 1: # vertical bar
#             if Bar[input_bar,0] == 0: # min boundary in x
#                 neigh_Ter = np.where(np.all(Ter==(Bar[input_bar,:] + [1,0]),axis=1))
#             elif Bar[input_bar,0] == 2*board_size: # max boundary in x
#                 neigh_Ter = np.where(np.all(Ter==(Bar[input_bar,:] - [1,0]),axis=1))
#             else:
#                 neigh_Ter = [np.where(np.all(Ter==(Bar[input_bar,:] - [1,0]),axis=1)),np.where(np.all(Ter==(Bar[input_bar,:] + [1,0]),axis=1))]
#         else: # horizontal bar
#             if Bar[input_bar,1] == 0: # min boundary in y
#                 neigh_Ter = np.where(np.all(Ter==(Bar[input_bar,:] + [0,1]),axis=1))
#             elif Bar[input_bar,1] == 2*board_size: # max boundary in x
#                 neigh_Ter = np.where(np.all(Ter==(Bar[input_bar,:] - [0,1]),axis=1))
#             else:
#                 neigh_Ter = [np.where(np.all(Ter==(Bar[input_bar,:] - [0,1]),axis=1)),np.where(np.all(Ter==(Bar[input_bar,:] + [0,1]),axis=1))]
#         
#         
#         for i in range(np.shape(neigh_Ter)[0]):
# =============================================================================
            
        
        # Find the neighbouring Ter
        if Bar[input_bar,1]%2 == 1: # vertical bar
            if Bar[input_bar,0] == 0: # min boundary in x
                neigh_Ter = abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [1,1]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [2,0]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [1,-1]),axis=1))])
                if neigh_Ter == 3:
                    flag_newTer = 1
                    Ter_state[np.where(np.all(Ter==(Bar[input_bar,:] + [1,0]),axis=1))] = flag_team
            elif Bar[input_bar,0] == 2*board_size: # max boundary in x
                neigh_Ter = abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [-1,1]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [-2,0]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [-1,-1]),axis=1))])
                if neigh_Ter == 3:
                    flag_newTer = 1
                    Ter_state[np.where(np.all(Ter==(Bar[input_bar,:] + [-1,0]),axis=1))] = flag_team
            else:
                neigh_Ter_right = abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [1,1]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [2,0]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [1,-1]),axis=1))])
                neigh_Ter_left = abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [-1,1]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [-2,0]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [-1,-1]),axis=1))])
                if neigh_Ter_right == 3:
                    flag_newTer = 1
                    Ter_state[np.where(np.all(Ter==(Bar[input_bar,:] + [1,0]),axis=1))] = flag_team
                if neigh_Ter_left == 3:
                    flag_newTer = 1
                    Ter_state[np.where(np.all(Ter==(Bar[input_bar,:] + [-1,0]),axis=1))] = flag_team
        else: # horizontal bar
            if Bar[input_bar,1] == 0: # min boundary in y
                neigh_Ter = abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [1,1]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [0,2]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [-1,1]),axis=1))])
                if neigh_Ter == 3:
                    flag_newTer = 1
                    Ter_state[np.where(np.all(Ter==(Bar[input_bar,:] + [0,1]),axis=1))] = flag_team
            elif Bar[input_bar,1] == 2*board_size: # max boundary in y
                neigh_Ter = abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [-1,-1]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [0,-2]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [1,-1]),axis=1))])
                if neigh_Ter == 3:
                    flag_newTer = 1
                    Ter_state[np.where(np.all(Ter==(Bar[input_bar,:] + [0,-1]),axis=1))] = flag_team
            else:
                neigh_Ter_up = abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [1,1]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [0,2]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [-1,1]),axis=1))])
                neigh_Ter_bot = abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [-1,-1]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [0,-2]),axis=1))])+abs(Bar_state[np.where(np.all(Bar==(Bar[input_bar,:] + [1,-1]),axis=1))])
                if neigh_Ter_up == 3:
                    flag_newTer = 1
                    Ter_state[np.where(np.all(Ter==(Bar[input_bar,:] + [0,1]),axis=1))] = flag_team
                if neigh_Ter_bot == 3:
                    flag_newTer = 1
                    Ter_state[np.where(np.all(Ter==(Bar[input_bar,:] + [0,-1]),axis=1))] = flag_team
        
        if flag_newTer == 1:
            print("Another play granted.")
        
        if int(sum(abs(Ter_state))) == np.shape(Ter)[0]: # all bars are chosen, game ended. 
            draw_board(Ver,Ter,Ter_state,Bar,Bar_state)
            break; 
        
        
    flag_team *= -1 # to the other team


R_Ter = np.count_nonzero(Ter_state == 1)
B_Ter = np.count_nonzero(Ter_state == -1)

print("Game ended.")

if R_Ter > B_Ter:
    print('Team Red won, by %d : %d. ' % (R_Ter, B_Ter))
    
elif R_Ter < B_Ter:
    print('Team Blue won, by %d : %d. ' % (R_Ter, B_Ter))
    
else:
    print('Game is a Draw, %d : %d. ' % (R_Ter, B_Ter))
    

Performance = ((R_Ter-B_Ter)**2*np.sign(R_Ter-B_Ter))/((R_Ter+B_Ter)**2)
        


# Script ended here. 