from enum import Enum

class GridPiece(Enum):
    SquarePiece = 0
    LongPiece = 1
    sPiece = 2
    zPiece = 3
    lPiece = 4
    jPiece = 5
    tPiece = 6

class GridManager():
    def __init__(self) -> None:
        self.t_squares = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    def spawnObject(self, piece:GridPiece, pos:tuple[int,int], rot:int):
        x,y = pos
        if piece == GridPiece.SquarePiece:
            self.t_squares[y][x] = 1
            self.t_squares[y][x+1] = 1
            self.t_squares[y+1][x] = 1
            self.t_squares[y+1][x+1] = 1
        elif piece == GridPiece.LongPiece:
            if rot == 2:
                self.t_squares[y][x] = 1
                self.t_squares[y][x+1] = 1
                self.t_squares[y][x+2] = 1
                self.t_squares[y][x+3] = 1
            else:
                self.t_squares[y][x] = 1
                self.t_squares[y+1][x] = 1
                self.t_squares[y+2][x] = 1
                self.t_squares[y+3][x] = 1
        elif piece == GridPiece.lPiece:
            if rot == 2:
                self.t_squares[y][x] = 1
                self.t_squares[y][x+1] = 1
                self.t_squares[y][x+2] = 1
                self.t_squares[y-1][x+2] = 1
            elif rot == 3:
                self.t_squares[y][x] = 1
                self.t_squares[y][x+1] = 1
                self.t_squares[y+1][x] = 1
                self.t_squares[y+2][x] = 1
            elif rot == 4:
                self.t_squares[y][x] = 1
                self.t_squares[y][x+1] = 1
                self.t_squares[y][x+2] = 1
                self.t_squares[y+1][x+2] = 1
            else:
                self.t_squares[y][x] = 1
                self.t_squares[y+1][x] = 1
                self.t_squares[y+2][x] = 1
                self.t_squares[y+2][x+1] = 1
        elif piece == GridPiece.jPiece:
            self.t_squares[y][x] = 1
            self.t_squares[y+1][x] = 1
            self.t_squares[y+2][x] = 1
            self.t_squares[y+2][x-1] = 1
        elif piece == GridPiece.sPiece:
            self.t_squares[y][x] = 1
            self.t_squares[y][x+1] = 1
            self.t_squares[y+1][x] = 1
            self.t_squares[y+1][x-1] = 1
        elif piece == GridPiece.zPiece:
            self.t_squares[y][x] = 1
            self.t_squares[y][x-1] = 1
            self.t_squares[y+1][x] = 1
            self.t_squares[y+1][x+1] = 1
        elif piece == GridPiece.tPiece:
            self.t_squares[y][x] = 1
            self.t_squares[y][x+1] = 1
            self.t_squares[y][x-1] = 1
            self.t_squares[y+1][x] = 1

    def removeObject(self, piece:GridPiece, pos:tuple[float,float])->None:
        x,y = pos
        if piece == GridPiece.SquarePiece:
            self.t_squares[y][x] = 0
            self.t_squares[y][x+1] = 0
            self.t_squares[y+1][x] = 0
            self.t_squares[y+1][x+1] = 0
        elif piece == GridPiece.LongPiece:
            self.t_squares[y][x] = 0
            self.t_squares[y+1][x] = 0
            self.t_squares[y+2][x] = 0
            self.t_squares[y+3][x] = 0
        elif piece == GridPiece.lPiece:
            self.t_squares[y][x] = 0
            self.t_squares[y+1][x] = 0
            self.t_squares[y+2][x] = 0
            self.t_squares[y+2][x+1] = 0
        elif piece == GridPiece.jPiece:
            self.t_squares[y][x] = 0
            self.t_squares[y+1][x] = 0
            self.t_squares[y+2][x] = 0
            self.t_squares[y+2][x-1] = 0
        elif piece == GridPiece.sPiece:
            self.t_squares[y][x] = 0
            self.t_squares[y][x+1] = 0
            self.t_squares[y+1][x] = 0
            self.t_squares[y+1][x-1] = 0
        elif piece == GridPiece.zPiece:
            self.t_squares[y][x] = 0
            self.t_squares[y][x-1] = 0
            self.t_squares[y+1][x] = 0
            self.t_squares[y+1][x+1] = 0
        elif piece == GridPiece.tPiece:
            self.t_squares[y][x] = 0
            self.t_squares[y][x+1] = 0
            self.t_squares[y][x-1] = 0
            self.t_squares[y+1][x] = 0

    def __str__(self) -> str:
        return "\n".join(list(map(str, [l for l in self.t_squares])))
