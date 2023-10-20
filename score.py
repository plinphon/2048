from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 120)
        self.score = 0
        self.score_position = (0,120)
        self.highscore_position = (0, 230)
    
    def write_score(self,lis):
        self.clear()
        for r in range(4):
            for c in range(4):
                if lis[r][c] != None:
                    self.score += lis[r][c]
        
        self.goto(self.score_position)
        self.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))
        