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

    def changeXY(self, x:float, y:float):
        self.x = x
        self.y = y

class Piece():
    def __init__(self, x:float, y:float, column:int) -> None:
        self.squares:list[Square] = []
        self.base:tuple[float,float] = (x,y)

        self.column = column
        self.row = 0
        self.__spacing__ = 47.0

    def moveAllX(self, amount:float):
        for square in self.squares:
            square.x += amount
        self.base = (self.base[0]+amount, self.base[1])
    
    def moveAllY(self, amount:float):
        for square in self.squares:
            square.y += amount
        self.base = (self.base[0], self.base[1]+amount)
    
    def rot(self,rot:int):
        pass

class p_Square(Piece):
    def __init__(self, x:float, y:float, column:int) -> None:
        super().__init__(x, y, column)

        self.color = (252, 227, 3)

        self.squares.append(Square(self.color, x, y))
        self.squares.append(Square(self.color, x+self.__spacing__, y))

        self.squares.append(Square(self.color, x, y+self.__spacing__))
        self.squares.append(Square(self.color, x+self.__spacing__, y+self.__spacing__))
    
    def rot(self, rot:int):
        pass

class p_Long(Piece):
    def __init__(self, x:float, y:float, column:int) -> None:
        super().__init__(x, y, column)
        self.color:tuple[int,int,int] = (3, 240, 252)

        for i in range(4):
            self.squares.append(Square(self.color, x, y+(self.__spacing__*i)))
    
    def rot(self, rot:int):
        x, y = self.base

        for square in self.squares:
            square.changeXY(self.base[0], self.base[1])
        if rot == 0:
            for i in range(4):
                self.squares[i] = Square(self.color, x, y+(self.__spacing__*i))
        elif rot == 1:
            for i in range(4):
                self.squares[i] = Square(self.color, x+(self.__spacing__*i), y)

