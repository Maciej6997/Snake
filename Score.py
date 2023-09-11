from turtle import Turtle

with open('data.txt', mode = 'r') as file:
    h_score = file.read()

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.reset_turtle()
        self.high_score = int(h_score)
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score = {self.score} High Score = {self.high_score}', False, align='center')

    def reset_turtle(self):
        """
        Reset actual score-turtle options
        """
        self.reset()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.speed('fastest')




    #def game_over(self):
     #   self.goto(0, 0)
      #  self.write(f'GAME OVER, your score = {self.score}', False, align='center')

    def reset_score(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = -1
        self.update_score()
