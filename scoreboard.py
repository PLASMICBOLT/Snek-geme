from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.refresh()
    def refresh(self):
        self.goto(0,265)
        self.clear()
        self.color('white')
        self.write(f'Scoreboard: {self.score}',True, 'center', ('arial',16,'normal'))
        self.color('black')
    def game_over(self):
        self.goto(0,0)
        self.color('white')
        self.write('GAME OVER', True, 'center', ('arial', 20, 'normal'))
        self.color('black')
