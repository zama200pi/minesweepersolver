import ms
import pygame


minesweeper.h=18
minesweeper.w=10
step=22

win_w,win_h=minesweeper.w*step,minesweeper.h*step

for i in range(minesweeper.h):
    minesweeper.board.append([-1 for j in range(minesweeper.w)])

pygame.init()

screen=pygame.display.set_mode((win_w,win_h))

font = pygame.font.Font(None, 32)


txt_color={
1:(0,0,255),
2:(0,255,0),
3:(255,0,0),
4:(160,32,240),
5:(255,255,0),
6:(255,165,0),
7:(160,165,0),
8:(160,32,0)
}

bomb_clr=(255,0,0)
safe_clr=(0,0,255)

num_surface_clr=(255,255,255)

brd_clr_1=(0,190,0)
brd_clr_2=(0,255,0)

cursor_clr=(127,127,127)

loop=True

pos=(0,0) #y,x

cursor_change_key={
pygame.K_UP:(-1,0),
pygame.K_DOWN:(1,0),
pygame.K_LEFT:(0,-1),
pygame.K_RIGHT:(0,1)
}

def key_to_num(key):
    if key==pygame.K_e :return -1  #erase
    if key==pygame.K_ASTERISK or key==pygame.K_KP_MULTIPLY: return "*"
    if key==pygame.K_s :return "s"
    if key==pygame.K_0 or key==pygame.K_KP0:return 0
    if key==pygame.K_1 or key==pygame.K_KP1:return 1
    if key==pygame.K_2 or key==pygame.K_KP2:return 2
    if key==pygame.K_3 or key==pygame.K_KP3:return 3
    if key==pygame.K_4 or key==pygame.K_KP4:return 4
    if key==pygame.K_5 or key==pygame.K_KP5:return 5
    if key==pygame.K_6 or key==pygame.K_KP6:return 6
    if key==pygame.K_7 or key==pygame.K_KP7:return 7
    if key==pygame.K_8 or key==pygame.K_KP8:return 8
    if key==pygame.K_9 or key==pygame.K_KP9:return 9
    
def display():
    for i in range(minesweeper.h):
        for j in range(minesweeper.w):
            if (i+j)%2:
                pygame.draw.rect(screen,brd_clr_1,(j*step,i*step,step,step))
            else :
                pygame.draw.rect(screen,brd_clr_2,(j*step,i*step,step,step))
    for i in range(minesweeper.h):
        for j in range(minesweeper.w):
            n=minesweeper.board[i][j]
            if n!=-1:
                if n in range(1,9):
                    pygame.draw.rect(screen,num_surface_clr,(j*step,i*step,step,step))
                    img=font.render(str(n),True,txt_color[n])
                    screen.blit(img,(j*step,i*step))
                elif n==0:
                    pygame.draw.rect(screen,num_surface_clr,(j*step,i*step,step,step))
                elif n=="*":
                    pygame.draw.rect(screen,bomb_clr,(j*step,i*step,step,step))
                elif n=="s":
                    pygame.draw.rect(screen,safe_clr,(j*step,i*step,step,step))
    #pos cursor

    pygame.draw.rect(screen,cursor_clr,(pos[1]*step,pos[0]*step,step,step),width=3)
    
    pygame.display.update()

while loop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            loop=False
            break
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            pos=y//step,x//step
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                print(minesweeper.board)
                print(minesweeper.p_board)
                minesweeper.compile_solve()
            elif event.key in cursor_change_key.keys():
                if 0<=pos[0]+cursor_change_key[event.key][0]<minesweeper.h and 0<=pos[1]+cursor_change_key[event.key][1]<minesweeper.w:
                    pos=(pos[0]+cursor_change_key[event.key][0],pos[1]+cursor_change_key[event.key][1])
            else:
                minesweeper.board[pos[0]][pos[1]]=key_to_num(event.key)
            

    display()



print(minesweeper.compile_solve())
