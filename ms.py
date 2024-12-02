# minesweeper solver
# -1 for nothing
# "*" for bomb
# "s" for safe
w=0
h=0
board=[]
def guessable(board,h,w):
    lst=[]
    for i in range(h):
        for j in range(w):
            if board[i][j]==-1:
                t=0
                for a in range(-1,2):
                    for b in range(-1,2):                    
                        if 0<=(i+a)<h and 0<=(j+b)<w:
                            if board[i+a][j+b] in range(1,9):
                                t=1
                                break
                if t==1:
                    lst.append((i,j))
                    
    return lst
def check(board,h,w):
    for i in range(h):
        for j in range(w):
            if board[i][j] in range(1,9):
                t=0
                g=0
                for a in [-1,0,1]:
                    for b in [-1,0,1]:
                        if 0<=(i+a)<h and 0<=(j+b)<w:
                            if board[i+a][j+b] == "*":
                                t+=1
                                g+=1
                            if board[i+a][j+b] == -1 :
                                g+=1

                if not t<=board[i][j]<=g:
                    return False
    return True
p_board=[]
import copy
def solver(lst,brd):
    board1=copy.deepcopy(brd)
    board2=copy.deepcopy(brd)
    global p_board,h,w
    if not lst:
        p_board.append(brd)        
        return 
    i,j=lst[0]
    board1[i][j]="*"
    lst2=lst.copy()
    lst2.pop(0)
    if check(board1,h,w):
        solver(lst2,board1)
        
    board2[i][j]="s"
    if check(board2,h,w):
        solver(lst2,board2)
        
def compile_solve():
    global board,p_board 

    lst=guessable(board,h,w)
    solver(lst,board)

    bombs=set()
    safe=set()
    for i in range(len(p_board)):
        brd=p_board[i]
        bombs_aux=[]
        safe_aux=[]
        for a in range(h):
            for b in range(w):
                if brd[a][b]=="*":
                    bombs_aux.append((a,b))
                if brd[a][b]=="s":
                    safe_aux.append((a,b))
        if i==0:
            bombs=set(bombs_aux)
            safe=set(safe_aux)
        else:
            bombs=bombs.intersection(set(bombs_aux))
            safe=safe.intersection(set(safe_aux))

    for i in bombs:
        board[i[0]][i[1]]="*"

    for i in safe:
        board[i[0]][i[1]]="s"

    p_board.clear()

    dic={"bombs":bombs,"safe":safe}
    return dic
