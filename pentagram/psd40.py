import turtle as t
from typing import Literal

class Character:
    def __init__(self, pen: t.Turtle, scale: float, x: float, y: float) -> None:
        self.pen = pen
        self.create_pen()
        self.s = scale
        self.x = x
        self.y = y
        #(0.5 a, 0.16246 a) | (0.118034 a, 0.16246 a) | (0, 0.525731 a) | (-0.118034 a, 0.16246 a) | (-0.5 a, 0.16246 a)
        #(-0.190983 a, -0.0620541 a) | (-0.309017 a, -0.425325 a) | (0, -0.200811 a) | (0.309017 a, -0.425325 a) | (0.190983 a, -0.0620541 a)
        
        self.points = {"t": {"x": x * self.s, "y": (y + 0.525731) * self.s},
                       "mr": {"x": (x + 0.5) * self.s, "y": (y + 0.16246) * self.s},
                       "ml": {"x": (x - 0.5) * self.s, "y": (y + 0.16246) * self.s},
                       "br": {"x": (x + 0.309017) * self.s, "y": (y - 0.425325) * self.s},
                       "bl": {"x": (x - 0.309017) * self.s, "y": (y - 0.425325) * self.s}, 
                       "tmr": {"x": (x + 0.25) * self.s, "y": (y + 0.3440955) * self.s},
                       "tml": {"x": (x - 0.25) * self.s, "y": (y + 0.3440955) * self.s},
                       "mbr": {"x": (x + 0.4045085) * self.s, "y": (y - 0.1314325) * self.s},
                       "mbl": {"x": (x - 0.4045085) * self.s, "y": (y - 0.1314325) * self.s},
                       "brl": {"x": x * self.s, "y": (y - 0.425325) * self.s}, 
                       "itr": {"x": (x + 0.118034) * self.s, "y": (y + 0.16246) * self.s},
                       "itl": {"x": (x - 0.118034) * self.s, "y": (y + 0.16246) * self.s},
                       "imr": {"x": (x + 0.190983) * self.s, "y": (y - 0.0620541) * self.s},
                       "iml": {"x": (x - 0.190983) * self.s, "y": (y - 0.0620541) * self.s},
                       "ib": {"x": x * self.s, "y": (y - 0.200811) * self.s},
                       "itrl": {"x": (x) * self.s, "y": (y + 0.16246) * self.s},
                       "itmr": {"x": (x + 0.1545085) * self.s, "y": (y + 0.05020295) * self.s},
                       "itml": {"x": (x - 0.1545085) * self.s, "y": (y + 0.05020295) * self.s},
                       "imrb": {"x": (x + 0.0954915) * self.s, "y": (y - 0.13143255) * self.s},
                       "imlb": {"x": (x - 0.0954915) * self.s, "y": (y - 0.13143255) * self.s}}
        self.chardict = {'0': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 34, 35, 36], 
                         '1': [9, 25, 26, 27], 
                         '2': [0, 1, 4, 5, 8, 9, 13, 14, 15, 18], 
                         '3': [0, 1, 4, 5, 6, 9, 12, 13, 38], 
                         '4': [8, 9, 25, 26, 27, 37, 38], 
                         '5': [0, 1, 4, 5, 11, 12, 21, 23], 
                         #'5': [0, 1, 4, 5, 16, 17, 20, 21], 
                         '6': [0, 1, 3, 4, 5, 19, 20, 21, 38, 39], 
                         '7': [0, 1, 2, 3, 9, 23, 24], 
                         '8': [0, 1, 3, 4, 5, 6, 8, 9, 28, 29, 30, 37, 38, 39], 
                         '9': [0, 1, 2, 3, 4, 5, 8, 9, 13, 14, 17, 18],
                         'A': [10, 11, 12, 14, 17, 19, 20, 21], 
                         'B': [0, 1, 4, 5, 12, 13, 19, 20, 21, 38], 
                         'C': [0, 1, 4, 5, 6, 7, 8, 9], 
                         'D': [0, 1, 2, 3, 4, 5, 19, 20, 21], 
                         'E': [0, 1, 4, 5, 19, 20, 21, 38], 
                         'F': [0, 1, 19, 20, 21, 38], 
                         'G': [0, 1, 3, 4, 5, 6, 7, 8, 9, 38, 39], 
                         'H': [2, 3, 19, 20, 21, 38, 39], 
                         'I': [25, 26, 27], 
                         'J': [4, 5, 10, 11, 12, 19],
                         'K': [16, 17, 19, 20, 21, 28, 29], 
                         'L': [4, 5, 19, 20, 21], 
                         'M': [2, 3, 10, 11, 13, 19, 20, 21], 
                         'N': [2, 3, 10, 11, 12, 19, 20, 21], 
                         'O': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                         'P': [0, 1, 13, 38, 19, 20, 21], 
                         'Q': [0, 1, 6, 7, 8, 9, 13, 14, 15, 16, 17], 
                         'R': [0, 1, 13, 38, 19, 20, 21, 31, 32], 
                         'S': [0, 1, 3, 4, 5, 6, 8, 9, 37, 38, 39], 
                         'T': [19, 20, 21, 22, 23, 24], 
                         'U': [2, 3, 4, 5, 19, 20, 21], 
                         'V': [6, 7, 13, 14, 15], 
                         'W': [2, 3, 12, 14, 15, 19, 20, 21], 
                         'X': [31, 32, 33, 34, 35, 36], 
                         'Y': [10, 11, 13, 14, 15], 
                         'Z': [4, 5, 22, 23, 34, 35], 
                         ' ': [], 
                         '*': [10, 12, 13, 15, 16, 18, 19, 21, 22, 24], 
                         '^': list(range(40))}

    def create_pen(self) -> None:
        self.pen.speed(999)
        self.pen.width(3)

    def move(self, move_x: float, move_y: float) -> None:
        self.pen.pu()
        self.pen.goto(move_x, move_y)
        self.pen.pd()

    def lines(self, line: int) -> None:
        match line:
            case 0:
                self.move(self.points["t"]["x"], self.points["t"]["y"])
                self.pen.goto(self.points["tmr"]["x"], self.points["tmr"]["y"])
            case 1:
                self.move(self.points["tmr"]["x"], self.points["tmr"]["y"])
                self.pen.goto(self.points["mr"]["x"], self.points["mr"]["y"])
            case 2:
                self.move(self.points["mr"]["x"], self.points["mr"]["y"])
                self.pen.goto(self.points["mbr"]["x"], self.points["mbr"]["y"])
            case 3:
                self.move(self.points["mbr"]["x"], self.points["mbr"]["y"])
                self.pen.goto(self.points["br"]["x"], self.points["br"]["y"])
            case 4:
                self.move(self.points["br"]["x"], self.points["br"]["y"])
                self.pen.goto(self.points["brl"]["x"], self.points["brl"]["y"])
            case 5:
                self.move(self.points["brl"]["x"], self.points["brl"]["y"])
                self.pen.goto(self.points["bl"]["x"], self.points["bl"]["y"])
            case 6:
                self.move(self.points["bl"]["x"], self.points["bl"]["y"])
                self.pen.goto(self.points["mbl"]["x"], self.points["mbl"]["y"])
            case 7:
                self.move(self.points["mbl"]["x"], self.points["mbl"]["y"])
                self.pen.goto(self.points["ml"]["x"], self.points["ml"]["y"])
            case 8:
                self.move(self.points["ml"]["x"], self.points["ml"]["y"])
                self.pen.goto(self.points["tml"]["x"], self.points["tml"]["y"])
            case 9:
                self.move(self.points["tml"]["x"], self.points["tml"]["y"])
                self.pen.goto(self.points["t"]["x"], self.points["t"]["y"])
            case 10:
                self.move(self.points["t"]["x"], self.points["t"]["y"])
                self.pen.goto(self.points["itr"]["x"], self.points["itr"]["y"])
            case 11:
                self.move(self.points["itr"]["x"], self.points["itr"]["y"])
                self.pen.goto(self.points["imr"]["x"], self.points["imr"]["y"])
            case 12:
                self.move(self.points["imr"]["x"], self.points["imr"]["y"])
                self.pen.goto(self.points["br"]["x"], self.points["br"]["y"])
            case 13:
                self.move(self.points["mr"]["x"], self.points["mr"]["y"])
                self.pen.goto(self.points["imr"]["x"], self.points["imr"]["y"])
            case 14:
                self.move(self.points["imr"]["x"], self.points["imr"]["y"])
                self.pen.goto(self.points["ib"]["x"], self.points["ib"]["y"])
            case 15:
                self.move(self.points["ib"]["x"], self.points["ib"]["y"])
                self.pen.goto(self.points["bl"]["x"], self.points["bl"]["y"])
            case 16:
                self.move(self.points["br"]["x"], self.points["br"]["y"])
                self.pen.goto(self.points["ib"]["x"], self.points["ib"]["y"])
            case 17:
                self.move(self.points["ib"]["x"], self.points["ib"]["y"])
                self.pen.goto(self.points["iml"]["x"], self.points["iml"]["y"])
            case 18:
                self.move(self.points["iml"]["x"], self.points["iml"]["y"])
                self.pen.goto(self.points["ml"]["x"], self.points["ml"]["y"])
            case 19:
                self.move(self.points["bl"]["x"], self.points["bl"]["y"])
                self.pen.goto(self.points["iml"]["x"], self.points["iml"]["y"])
            case 20:
                self.move(self.points["iml"]["x"], self.points["iml"]["y"])
                self.pen.goto(self.points["itl"]["x"], self.points["itl"]["y"])
            case 21:
                self.move(self.points["itl"]["x"], self.points["itl"]["y"])
                self.pen.goto(self.points["t"]["x"], self.points["t"]["y"])
            case 22:
                self.move(self.points["ml"]["x"], self.points["ml"]["y"])
                self.pen.goto(self.points["itl"]["x"], self.points["itl"]["y"])
            case 23:
                self.move(self.points["itl"]["x"], self.points["itl"]["y"])
                self.pen.goto(self.points["itr"]["x"], self.points["itr"]["y"])
            case 24:
                self.move(self.points["itr"]["x"], self.points["itr"]["y"])
                self.pen.goto(self.points["mr"]["x"], self.points["mr"]["y"])
            case 25:
                self.move(self.points["t"]["x"], self.points["t"]["y"])
                self.pen.goto(self.points["itrl"]["x"], self.points["itrl"]["y"])
            case 26:
                self.move(self.points["itrl"]["x"], self.points["itrl"]["y"])
                self.pen.goto(self.points["ib"]["x"], self.points["ib"]["y"])
            case 27:
                self.move(self.points["ib"]["x"], self.points["ib"]["y"])
                self.pen.goto(self.points["brl"]["x"], self.points["brl"]["y"])
            case 28:
                self.move(self.points["mr"]["x"], self.points["mr"]["y"])
                self.pen.goto(self.points["itmr"]["x"], self.points["itmr"]["y"])
            case 29:
                self.move(self.points["itmr"]["x"], self.points["itmr"]["y"])
                self.pen.goto(self.points["iml"]["x"], self.points["iml"]["y"])
            case 30:
                self.move(self.points["iml"]["x"], self.points["iml"]["y"])
                self.pen.goto(self.points["mbl"]["x"], self.points["mbl"]["y"])
            case 31:
                self.move(self.points["br"]["x"], self.points["br"]["y"])
                self.pen.goto(self.points["imrb"]["x"], self.points["imrb"]["y"])
            case 32:
                self.move(self.points["imrb"]["x"], self.points["imrb"]["y"])
                self.pen.goto(self.points["itl"]["x"], self.points["itl"]["y"])
            case 33:
                self.move(self.points["itl"]["x"], self.points["itl"]["y"])
                self.pen.goto(self.points["tml"]["x"], self.points["tml"]["y"])
            case 34:
                self.move(self.points["bl"]["x"], self.points["bl"]["y"])
                self.pen.goto(self.points["imlb"]["x"], self.points["imlb"]["y"])
            case 35:
                self.move(self.points["imlb"]["x"], self.points["imlb"]["y"])
                self.pen.goto(self.points["itr"]["x"], self.points["itr"]["y"])
            case 36:
                self.move(self.points["itr"]["x"], self.points["itr"]["y"])
                self.pen.goto(self.points["tmr"]["x"], self.points["tmr"]["y"])
            case 37:
                self.move(self.points["ml"]["x"], self.points["ml"]["y"])
                self.pen.goto(self.points["itml"]["x"], self.points["itml"]["y"])
            case 38:
                self.move(self.points["itml"]["x"], self.points["itml"]["y"])
                self.pen.goto(self.points["imr"]["x"], self.points["imr"]["y"])
            case 39:
                self.move(self.points["imr"]["x"], self.points["imr"]["y"])
                self.pen.goto(self.points["mbr"]["x"], self.points["mbr"]["y"])

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