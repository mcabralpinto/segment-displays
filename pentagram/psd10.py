import turtle as t
from math import sqrt

class Character:
    def __init__(self, pen: t.Turtle, scale: float, x: float, y: float) -> None:
        self.pen = pen
        self.create_pen()
        self.s = scale
        self.x = x
        self.y = y
        self.points = {"top": {"x": x * self.s, "y": (y + sqrt((5 - sqrt(5)) / 10)) * self.s},
                       "midright": {"x": (x + 1 / 2) * self.s, "y": (y + sqrt((5 - 2 * sqrt(5)) / 20)) * self.s},
                       "midleft": {"x": (x - 1 / 2) * self.s, "y": (y + sqrt((5 - 2 * sqrt(5)) / 20)) * self.s},
                       "bottright": {"x": (x + (sqrt(5) - 1) / 4) * self.s, "y": (y - sqrt((5 + sqrt(5)) / 40)) * self.s},
                       "bottleft": {"x": (x - (sqrt(5) - 1) / 4) * self.s, "y": (y - sqrt((5 + sqrt(5)) / 40)) * self.s}}
        self.chardict = {'0': [0, 1, 2, 3, 4, 6], '1': [4, 5], '2': [0, 2, 4, 6], '3': [0, 1, 2, 9], '4': [4, 5, 9], 
                         '5': [1, 2, 4, 9], '6': [1, 2, 3, 4, 6], '7': [0, 1, 4], '8': [0, 2, 4, 6, 7], '9': [0, 1, 2, 4, 9],
                         'A': [5, 8, 9], 'B': [0, 2, 5, 6], 'C': [0, 2, 3, 4], 'D': [0, 1, 2, 8], 'E': [0, 2, 3, 4, 9], 
                         'F': [3, 4, 9], 'G': [1, 2, 3, 4], 'H': [1, 8, 9], 'I': [8], 'J': [2, 3, 5],'K': [3, 4, 7, 9], 
                         'L': [2, 8], 'M': [1, 4, 6, 8], 'N': [1, 5, 8], 'O': [0, 1, 2, 3, 4], 'P': [0, 8, 9], 
                         'Q': [0, 3, 4, 6, 7], 'R': [0, 3, 4, 7, 9], 'S': [0, 2, 4, 7], 'T': [8, 9], 'U': [1, 2, 8], 
                         'V': [3, 6], 'W': [1, 3, 5, 8], 'X': [6, 7], 'Y': [1, 2, 7], 'Z': [2, 6, 9], 
                         ' ': [], '(': [3, 4], ')': [0, 1], '=': [2, 9], '+': [5, 9], '-': [9], '*': [5, 6], 
                         '\\': [5], '/': [8], '_': [2]}

    def create_pen(self) -> None:
        self.pen.speed()
        self.pen.width(3)

    def move(self, move_x: float, move_y: float) -> None:
        self.pen.pu()
        self.pen.goto(move_x, move_y)
        self.pen.pd()

    def lines(self, line: int) -> None:
        match line:
            case 0:
                self.move(self.points["top"]["x"], self.points["top"]["y"])
                self.pen.goto(self.points["midright"]["x"], self.points["midright"]["y"])
            case 1:
                self.move(self.points["midright"]["x"], self.points["midright"]["y"])
                self.pen.goto(self.points["bottright"]["x"], self.points["bottright"]["y"])
            case 2:
                self.move(self.points["bottright"]["x"], self.points["bottright"]["y"])
                self.pen.goto(self.points["bottleft"]["x"], self.points["bottleft"]["y"])
            case 3:
                self.move(self.points["bottleft"]["x"], self.points["bottleft"]["y"])
                self.pen.goto(self.points["midleft"]["x"], self.points["midleft"]["y"])
            case 4:
                self.move(self.points["midleft"]["x"], self.points["midleft"]["y"])
                self.pen.goto(self.points["top"]["x"], self.points["top"]["y"])
            case 5:
                self.move(self.points["top"]["x"], self.points["top"]["y"])
                self.pen.goto(self.points["bottright"]["x"], self.points["bottright"]["y"])
            case 6:
                self.move(self.points["midright"]["x"], self.points["midright"]["y"])
                self.pen.goto(self.points["bottleft"]["x"], self.points["bottleft"]["y"])
            case 7:
                self.move(self.points["bottright"]["x"], self.points["bottright"]["y"])
                self.pen.goto(self.points["midleft"]["x"], self.points["midleft"]["y"])
            case 8:
                self.move(self.points["bottleft"]["x"], self.points["bottleft"]["y"])
                self.pen.goto(self.points["top"]["x"], self.points["top"]["y"])
            case 9:
                self.move(self.points["midleft"]["x"], self.points["midleft"]["y"])
                self.pen.goto(self.points["midright"]["x"], self.points["midright"]["y"])

    def penta(self) -> None:
        for i in range(10):
            self.lines(i)

if __name__ == "__main__":
    SIZE = 45
    X_PADDING = 1.2
    Y_PADDING = 1.5
    SPACE = 27
    ROWS = int(input())

    for i in range(ROWS):
        word = input().upper()
        start_x = -(len(word) - 1) / 2
        start_y = ((ROWS - 1) / 2) - i

        for j, letter in enumerate(word):
            new = Character(t.Turtle(), SIZE, start_x + (j % SPACE) * X_PADDING, start_y - (j // SPACE) * Y_PADDING)
            for line in new.chardict[letter]:
                new.lines(line)
            new.pen.hideturtle()
 
    t.exitonclick()