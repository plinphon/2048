from turtle import Screen, Turtle
import random
from score import Score

class Tile:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)  
        self.tiles = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
        self.t = Turtle()
        self.score = Score()
        self.score.write_score(self.tiles)
        self.t.hideturtle()
        self.screen.title("2048 Game")
        self.screen.setup(width=600, height=400)
        self.random_spawn()
        self.draw_tiles()
        self.screen.listen()
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")
        self.screen.onkey(self.left, "Left")
        self.screen.onkey(self.right, "Right")

    def draw_tiles(self): 
        self.t.speed(0)
        self.t.pu()
        self.t.goto(-80, 80)
        for r in range(4):
            for c in range(4):
                num = self.tiles[r][c]
                if num is not None:
                    self.t.pu()
                    self.t.goto(c * 40 - 80, 80 - r * 40)
                    self.t.pd()
                    self.t.write(str(num), align='center', font=('Arial', 16, 'normal'))
    
            
    def random_spawn(self):
        while True:
            c = random.randint(0,3)
            r = random.randint(0,3)
            if self.tiles[r][c] == None:
                self.tiles[r][c] = 2
                break
    
 
    def down(self):
        w=0
        while True:
            n = 0
            for c in range(4):
                for r in range(4):
                    if r < 3:
                        if self.tiles[r][c] != None and self.tiles[r+1][c] == None:
                            self.tiles[r+1][c] = self.tiles[r][c]
                            self.tiles[r][c] = None
                            n = 1
                        elif w == 1 and r+1 == 3:
                            continue
                        elif self.tiles[r][c] == self.tiles[r+1][c] and self.tiles[r][c] !=None:
                            self.tiles[r+1][c] *= 2
                            self.tiles[r][c] = None
                            n = 1
                            if r+1 == 3:
                                w=1
                        else:
                            continue
                    else:
                        continue
            if n == 0:
                self.random_spawn()
                self.t.clear()
                self.draw_tiles()
                self.score.write_score(self.tiles)
                break
    def up(self):
        w=0
        while True:
            n = 0
            for c in range(4):
                for r in range(4):
                    if r > 0:
                        if self.tiles[r][c] != None and self.tiles[r-1][c] == None:
                            self.tiles[r-1][c] = self.tiles[r][c]
                            self.tiles[r][c] = None
                            n = 1
                        elif w == 1 and r-1 == 0:
                            continue
                        elif self.tiles[r][c] == self.tiles[r-1][c] and self.tiles[r][c] != None:
                            self.tiles[r-1][c] *= 2
                            self.tiles[r][c] = None
                            n = 1
                            if r-1 == 0:
                                w=1
                        else:
                            continue
                    else:
                        continue
            if n == 0:
                self.random_spawn()
                self.t.clear()
                self.draw_tiles()
                self.score.write_score(self.tiles)
                break

    def left(self):
        w=0
        while True:
            n = 0
            for c in range(4):
                for r in range(4):
                    if c > 0 :
                        if self.tiles[r][c] != None and self.tiles[r][c-1] == None:
                            self.tiles[r][c-1] = self.tiles[r][c]
                            self.tiles[r][c] = None
                            n = 1
                        elif w == 1 and c-1 == 0:
                            continue
                        elif self.tiles[r][c] == self.tiles[r][c-1] and self.tiles[r][c] !=None:
                            self.tiles[r][c-1] *= 2
                            self.tiles[r][c] = None
                            n = 1
                            if c-1 == 0:
                                w=1
                        else:
                            continue
                    else:
                        continue
           
            if n == 0:
                self.random_spawn()
                self.t.clear()
                self.draw_tiles()
                self.score.write_score(self.tiles)
                break
    
    def right(self):
        w=0
        while True:
            n = 0
            for c in range(4):
                for r in range(4):
                    if c < 3 :
                        if self.tiles[r][c] != None and self.tiles[r][c+1] == None:
                            self.tiles[r][c+1] = self.tiles[r][c]
                            self.tiles[r][c] = None
                            n = 1
                        elif w == 1 and c+1 == 3:
                            continue
                        elif self.tiles[r][c] == self.tiles[r][c+1] and self.tiles[r][c] != None:
                            self.tiles[r][c+1] *= 2
                            self.tiles[r][c] = None
                            n = 1
                            if c+1 == 3:
                                w=1
                        else:
                            continue
                    else:
                        continue
            if n == 0:
                self.random_spawn()
                self.t.clear()
                self.draw_tiles()
                self.score.write_score(self.tiles)
                break
