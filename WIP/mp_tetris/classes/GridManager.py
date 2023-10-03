from enum import Enum
from classes.Pieces import Piece, p_Long, p_Square

color_dict:dict[tuple[int,int,int]] = {
    0: (88, 82, 110), # BASE COLOR
    1: (252, 227, 3), # O PIECE COLOR
    2: (3, 240, 252), # I PIECE COLOR
    3: (255, 132, 43), # L PIECE COLOR
    4: (245, 118, 245), # J PIECE COLOR
    5: (227, 34, 50), # S PIECE COLOR
    6: (108, 189, 75), # Z PIECE COLOR
    7: (137, 49, 204), # T PIECE COLOR
}

class GridPiece(Enum):
    oPiece = 0
    iPiece = 1
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
    
    def editObject(self, piece:GridPiece, pos:tuple[int,int], rot:int, add_remove:int):
        x,y = pos
        if piece == GridPiece.oPiece:
            self.t_squares[y][x] = 1 * add_remove
            self.t_squares[y][x+1] = 1 * add_remove
            self.t_squares[y+1][x] = 1 * add_remove
            self.t_squares[y+1][x+1] = 1 * add_remove
        elif piece == GridPiece.iPiece:
            if rot == 0 or rot == 2:
                self.t_squares[y][x] = 2 * add_remove
                self.t_squares[y+1][x] = 2 * add_remove
                self.t_squares[y+2][x] = 2 * add_remove
                self.t_squares[y+3][x] = 2 * add_remove
            else:
                self.t_squares[y][x] = 2 * add_remove
                self.t_squares[y][x+1] = 2 * add_remove
                self.t_squares[y][x+2] = 2 * add_remove
                self.t_squares[y][x+3] = 2 * add_remove
        elif piece == GridPiece.lPiece:
            if rot == 2:
                self.t_squares[y][x] = 3 * add_remove
                self.t_squares[y][x+1] = 3 * add_remove
                self.t_squares[y][x+2] = 3 * add_remove
                self.t_squares[y-1][x+2] = 3 * add_remove
            elif rot == 3:
                self.t_squares[y][x] = 3 * add_remove
                self.t_squares[y][x+1] = 3 * add_remove
                self.t_squares[y+1][x] = 3 * add_remove
                self.t_squares[y+2][x] = 3 * add_remove
            elif rot == 4:
                self.t_squares[y][x] = 3 * add_remove
                self.t_squares[y][x+1] = 3 * add_remove
                self.t_squares[y][x+2] = 3 * add_remove
                self.t_squares[y+1][x+2] = 3 * add_remove
            else:
                self.t_squares[y][x] = 3 * add_remove
                self.t_squares[y+1][x] = 3 * add_remove
                self.t_squares[y+2][x] = 3 * add_remove
                self.t_squares[y+2][x+1] = 3 * add_remove
        elif piece == GridPiece.jPiece:
            self.t_squares[y][x] = 4 * add_remove
            self.t_squares[y+1][x] = 4 * add_remove
            self.t_squares[y+2][x] = 4 * add_remove
            self.t_squares[y+2][x-1] = 4 * add_remove
        elif piece == GridPiece.sPiece:
            self.t_squares[y][x] = 5 * add_remove
            self.t_squares[y][x+1] = 5 * add_remove
            self.t_squares[y+1][x] = 5 * add_remove
            self.t_squares[y+1][x-1] = 5 * add_remove
        elif piece == GridPiece.zPiece:
            self.t_squares[y][x] = 6 * add_remove
            self.t_squares[y][x-1] = 6 * add_remove
            self.t_squares[y+1][x] = 6 * add_remove
            self.t_squares[y+1][x+1] = 6 * add_remove
        elif piece == GridPiece.tPiece:
            self.t_squares[y][x] = 7 * add_remove
            self.t_squares[y][x+1] = 7 * add_remove
            self.t_squares[y][x-1] = 7 * add_remove
            self.t_squares[y+1][x] = 7 * add_remove

    def removeObject(self, piece:GridPiece, pos:tuple[float,float])->None:
        x,y = pos
        if piece == GridPiece.oPiece:
            self.t_squares[y][x] = 0
            self.t_squares[y][x+1] = 0
            self.t_squares[y+1][x] = 0
            self.t_squares[y+1][x+1] = 0
        elif piece == GridPiece.iPiece:
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

    def equiv(self, piece:Piece) -> GridPiece:
        d = {
            p_Long: GridPiece.iPiece,
            p_Square: GridPiece.oPiece
        }
        return d[type(piece)]
    
    def __str__(self) -> str:
        return "\n".join(list(map(str, [l for l in self.t_squares])))
