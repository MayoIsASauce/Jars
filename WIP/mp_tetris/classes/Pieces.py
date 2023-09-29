# contains definitions for cool tetris pieces
from dataclasses import dataclass
from pygame import Rect

class Square():
    def __init__(self, color, x:float, y:float) -> None:
        self.color = color
        self.x = x
        self.y = y
        self.w = 45.0
        self.h = 45.0
    
    def getRect(self) -> Rect:
        return Rect(self.x, self.y, self.w, self.h)

class Piece():
    def __init__(self, x:float, y:float) -> None:
        self.squares:list[Square] = []
        self.__spacing__ = 47.0

    def moveAllX(self, amount:float):
        for square in self.squares:
            square.x += amount
    
    def moveAllY(self, amount:float):
        for square in self.squares:
            square.y += amount

class p_Square(Piece):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(x, y)

        self.color = (252, 227, 3)

        self.squares.append(Square(self.color, x, y))
        self.squares.append(Square(self.color, x+self.__spacing__, y))

        self.squares.append(Square(self.color, x, y+self.__spacing__))
        self.squares.append(Square(self.color, x+self.__spacing__, y+self.__spacing__))

class p_Long(Piece):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(x, y)
        self.color = (3, 240, 252)

        for i in range(4):
            self.squares.append(Square(self.color, x, y+(self.__spacing__*i)))
