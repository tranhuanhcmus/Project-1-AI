from xmlrpc.client import Fault
from matplotlib.pyplot import draw_if_interactive
import numpy as np
import math
from algorithm import *
from make_obstacle import *
from UI import *

# COLOR
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
PURPLE=(128,0,128)
ORANGE=(255,165,0)
GREY=(128,128,128)
TURQUOISE=(64,224,208)

WIDTH=600
WIN=pygame.display.set_mode(SIZE)
pygame.display.set_caption("A Graph")

background_color = (234, 212, 252)


class Spot:
    def __init__(self,row,col,width,height,total_rows,total_cols):
        self.row=row
        self.col=col
        self.x=row*width
        self.y=col*height
        self.color=WHITE
        self.neighbors=[]
        self.width=width
        self.height=height
        self.total_rows=total_rows
        self.total_cols=total_cols

    def get_pos(self):
        return self.row,self.col

    def is_closed(self):
        return self.color==RED

    def is_open(self):
        return self.color==GREEN
    
    def is_barrier(self):
        return self.color==BLACK

    def is_start(self):
        return self.color==ORANGE
    
    def is_end(self):
        return self.color==TURQUOISE 
    
    def reset(self):
        self.color=WHITE

    def make_closed(self):
        self.color=RED

    def make_open(self):
        self.color=GREEN
    
    def make_barrier(self):
        self.color=BLACK

    def make_start(self):
        self.color=ORANGE
    
    def make_end(self):
        self.color=TURQUOISE 

    def make_path(self):
        self.color=PURPLE

    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_cols - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])


def make_grid(rows,width,cols,height):
    grid=[]
    w=width//rows
    h=height//cols
    for i in range (rows):
        grid.append([])
        for j in range (cols):
            spot=Spot(i,j,w,h, rows,cols)
            grid[i].append(spot) 
    return grid

def draw_grid(win,rows,width,cols,height):
    w=width//rows
    h=height//cols
    for i in range (cols):
        pygame.draw.line(win,GREY,(0,i*h),(width,i*h))
        for j in range (rows):
            pygame.draw.line(win,GREY,(j*w,0),(j*w,height))


def draw(win,grid,rows,width,cols,height,list): #// sửa vt 
    win.fill(RED)
    for row in grid:
        for spot in row:
            spot.draw(win)
    
    draw_grid(win,rows,width,cols,height)
    for index in range(2,len(list)):
        vt = np.array(list[index])
        make_obstacle(grid,vt)
#    vt = np.array([11, 1, 11, 6, 14, 6, 14, 1])
#    vt2 = np.array([4, 4, 5, 9, 8, 10, 9, 5])
#    vt3 = np.array([8, 12, 8, 17, 13, 12])

#    make_obstacle(grid, vt)
#    make_obstacle(grid, vt2)
#    make_obstacle(grid, vt3)

    pygame.display.update()

def get_clicked_pos(pos,rows,width,cols,height):#
    w=width//rows
    h=height//cols
    y,x=pos
    
    row=y//w
    col=x//h

    return row,col

def main(findPath,win, width,height,list):#// SUA ROW COL START END ,ROWS,COLS,start,end
    ROWS = list[0][0]
    COLS= list[0][1]
    grid = make_grid(ROWS, width,COLS,height)
    start = grid[list[1][0]][list[1][1]]
    end = grid[list[1][2]][list[1][3]]
    start.make_start()
    end.make_end()
    run = True
    while run:
        draw(win, grid, ROWS, width,COLS,height,list)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width,COLS,height)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width,COLS,height)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    findPath(lambda: draw(win, grid, ROWS, width,COLS,height,list), grid, start, end)
                    # A_Star(lambda: draw(win, grid, ROWS, width,COLS,height), grid, start, end)
                    # GBFS(lambda: draw(win, grid, ROWS, width,COLS,height), grid, start, end)
                    # BFS(lambda: draw(win, grid, ROWS, width,COLS,height), grid, start, end)
                    # UCS(lambda: draw(win, grid, ROWS, width,COLS,height), grid, start, end)
                    # DFS(lambda: draw(win, grid, ROWS, width,COLS,height), grid, start, end)

                if event.key == pygame.K_DELETE:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width,COLS,height)

    pygame.quit()

def docfile(filename):
    file_object = open(filename,'r')
    print(file_object)

    new_data=[]

    for index in range(0,2):
        data=file_object.readline()
        data=data[0:-1]
        data = list(data.split(' '))
        data = list(map(int,data))
        new_data.append(data)

    leng=file_object.readline()
    leng=leng[0:-1]
    leng=int(leng)
    for index in range(0,leng):
        data=file_object.readline()
        data=data[0:-1]
        data = list(data.split(' '))
        data = list(map(int,data))
        new_data.append(data)
    return new_data
def Home(WIN):
    list = docfile('input.txt')
    while True:
        hp=HomePage()
        hp.draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                #check mouseover and clicked conditions

                if hp.A_Star.rect.collidepoint(pos):
                    main(A_Star,WIN,SIZE[0],SIZE[1],list)
                if hp.BFS.rect.collidepoint(pos):
                    main(BFS,WIN,SIZE[0],SIZE[1],list)
                if hp.GBFS.rect.collidepoint(pos):
                    main(GBFS,WIN,SIZE[0],SIZE[1],list)
                if hp.UCS.rect.collidepoint(pos):
                    main(UCS,WIN,SIZE[0],SIZE[1],list)
                if hp.IDS.rect.collidepoint(pos):
                    main(DFS,WIN,SIZE[0],SIZE[1],list)
               
                    
                
      
        hp.update()

Home(WIN)