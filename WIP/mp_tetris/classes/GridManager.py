from enum import Enum

color_dict:dict[int, tuple[int,int,int]] = {
    0: (88, 82, 110), # BASE COLOR
    1: (252, 227, 3), # O PIECE COLOR
    2: (3, 240, 252), # I PIECE COLOR
    3: (255, 132, 43), # L PIECE COLOR
    4: (50, 40, 247), # J PIECE COLOR
    5: (227, 34, 50), # S PIECE COLOR
    6: (108, 189, 75), # Z PIECE COLOR
    7: (199, 91, 245), # T PIECE COLOR
}

class GridPiece(Enum):
    oPiece = "oPiece"
    iPiece = "iPiece"
    sPiece = "sPiece"
    zPiece = "zPiece"
    lPiece = "lPiece"
    jPiece = "jPiece"
    tPiece = "tPiece"

def lowest_square(piece:GridPiece, xy:tuple[int,int], rot:int) -> int:
    x, y = xy
    match piece:
        case GridPiece.oPiece:
            return y+1
        case GridPiece.iPiece:
            if rot == 2 or rot == 0:
                return y + 2
            else:
                return y
        case GridPiece.lPiece:
            if rot == 3:
                return y
            else:
                return y + 1
        case GridPiece.jPiece:
            if rot == 1:
                return y
            else:
                return y + 1
        case GridPiece.sPiece:
            if rot == 0 or rot == 2:
                return y
            else:
                return y + 1
        case GridPiece.zPiece:
            if rot == 0 or rot == 2:
                return y
            else:
                return y + 1
        case GridPiece.tPiece:
            if rot == 2:
                return y
            else:
                return y + 1

def right_square(piece:GridPiece, xy:tuple[int,int], rot:int) -> int:
    x, y = xy

    match piece:
        case GridPiece.oPiece:
            return x+1
        case GridPiece.iPiece:
            match rot:
                case 0:
                    return x
                case 1:
                    return x + 1
                case 2:
                    return x
                case 3:
                    return x + 2
        case GridPiece.lPiece:
            if rot == 2:
                return x
            else:
                return x + 1
        case GridPiece.jPiece:
            if rot == 0:
                return x
            else:
                return x + 1
        case GridPiece.sPiece:
            return x + 1
        case GridPiece.zPiece:
            return x + 1
        case GridPiece.tPiece:
            if rot == 1:
                return x
            else:
                return x + 1

def left_square(piece:GridPiece, xy:tuple[int,int], rot:int) -> int:
    x, y = xy

    match piece:
        case GridPiece.oPiece:
            return x
        case GridPiece.iPiece:
            match rot:
                case 0:
                    return x
                case 1:
                    return x - 2
                case 2:
                    return x
                case 3:
                    return x - 1
        case GridPiece.lPiece:
            if rot == 0:
                return x
            else:
                return x - 1
        case GridPiece.jPiece:
            if rot == 2:
                return x
            else:
                return x - 1
        case GridPiece.sPiece:
            if rot == 0 or rot == 2:
                return x - 1
            else:
                return x
        case GridPiece.zPiece:
            if rot == 0 or rot == 2:
                return x - 1
            else:
                return x
        case GridPiece.tPiece:
            if rot == 3:
                return x
            else:
                return x - 1

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
            if rot == 0:
                self.t_squares[y][x] = 2 * add_remove
                if y > 0:
                    self.t_squares[y-1][x] = 2 * add_remove
                self.t_squares[y+1][x] = 2 * add_remove
                self.t_squares[y+2][x] = 2 * add_remove
            elif rot == 1:
                self.t_squares[y][x] = 2 * add_remove
                self.t_squares[y][x+1] = 2 * add_remove
                self.t_squares[y][x-1] = 2 * add_remove
                self.t_squares[y][x-2] = 2 * add_remove
            elif rot == 2:
                self.t_squares[y][x] = 2 * add_remove
                self.t_squares[y+1][x] = 2 * add_remove
                if y > 0:
                    self.t_squares[y-1][x] = 2 * add_remove
                if y > 1:
                    self.t_squares[y-2][x] = 2 * add_remove
            elif rot == 3:
                self.t_squares[y][x] = 2 * add_remove
                self.t_squares[y][x-1] = 2 * add_remove
                self.t_squares[y][x+1] = 2 * add_remove
                self.t_squares[y][x+2] = 2 * add_remove
        elif piece == GridPiece.lPiece:
            if rot == 0:
                self.t_squares[y][x] = 3 * add_remove
                if y > 0:
                    self.t_squares[y-1][x] = 3 * add_remove
                self.t_squares[y+1][x] = 3 * add_remove
                self.t_squares[y+1][x+1] = 3 * add_remove
            elif rot == 1:
                self.t_squares[y][x] = 3 * add_remove
                self.t_squares[y][x+1] = 3 * add_remove
                self.t_squares[y][x-1] = 3 * add_remove
                self.t_squares[y+1][x-1] = 3 * add_remove
            elif rot == 2:
                if y > 0:
                    self.t_squares[y-1][x-1] = 3 * add_remove
                if y > 0:
                    self.t_squares[y-1][x] = 3 * add_remove
                self.t_squares[y][x] = 3 * add_remove
                self.t_squares[y+1][x] = 3 * add_remove
            elif rot == 3:
                self.t_squares[y][x-1] = 3 * add_remove
                self.t_squares[y][x] = 3 * add_remove
                self.t_squares[y][x+1] = 3 * add_remove
                if y > 0:
                    self.t_squares[y-1][x+1] = 3 * add_remove
        elif piece == GridPiece.jPiece:
            if rot == 0:
                if y > 0:
                    self.t_squares[y-1][x] = 4 * add_remove
                self.t_squares[y][x] = 4 * add_remove
                self.t_squares[y+1][x] = 4 * add_remove
                self.t_squares[y+1][x-1] = 4 * add_remove
            elif rot == 1:
                if y > 0:
                    self.t_squares[y-1][x-1] = 4 * add_remove
                self.t_squares[y][x-1] = 4 * add_remove
                self.t_squares[y][x] = 4 * add_remove
                self.t_squares[y][x+1] = 4 * add_remove
            elif rot == 2:
                if y > 0:
                    self.t_squares[y-1][x] = 4 * add_remove
                if y > 0:
                    self.t_squares[y-1][x+1] = 4 * add_remove
                self.t_squares[y][x] = 4 * add_remove
                self.t_squares[y+1][x] = 4 * add_remove
            elif rot == 3:
                self.t_squares[y][x-1] = 4 * add_remove
                self.t_squares[y][x] = 4 * add_remove
                self.t_squares[y][x+1] = 4 * add_remove
                self.t_squares[y+1][x+1] = 4 * add_remove
        elif piece == GridPiece.sPiece:
            if rot == 0 or rot == 2:
                self.t_squares[y][x-1] = 5 * add_remove
                self.t_squares[y][x] = 5 * add_remove
                if y > 0:
                    self.t_squares[y-1][x] = 5 * add_remove
                if y > 0:
                    self.t_squares[y-1][x+1] = 5 * add_remove
            elif rot == 1 or rot == 3:
                if y > 0:
                    self.t_squares[y-1][x] = 5 * add_remove
                self.t_squares[y][x] = 5 * add_remove
                self.t_squares[y][x+1] = 5 * add_remove
                self.t_squares[y+1][x+1] = 5 * add_remove
        elif piece == GridPiece.zPiece:
            if rot == 0 or rot == 2:
                self.t_squares[y][x+1] = 6 * add_remove
                self.t_squares[y][x] = 6 * add_remove
                if y > 0:
                    self.t_squares[y-1][x] = 6 * add_remove
                if y > 0:
                    self.t_squares[y-1][x-1] = 6 * add_remove
            elif rot == 1 or rot == 3:
                if y > 0:
                    self.t_squares[y-1][x+1] = 6 * add_remove
                self.t_squares[y][x] = 6 * add_remove
                self.t_squares[y][x+1] = 6 * add_remove
                self.t_squares[y+1][x] = 6 * add_remove
        elif piece == GridPiece.tPiece:
            if rot == 0:
                self.t_squares[y][x-1] = 7 * add_remove
                self.t_squares[y][x] = 7 * add_remove
                self.t_squares[y][x+1] = 7 * add_remove
                self.t_squares[y+1][x] = 7 * add_remove
            elif rot == 1:
                if y > 0:
                    self.t_squares[y-1][x] = 7 * add_remove
                self.t_squares[y][x-1] = 7 * add_remove
                self.t_squares[y][x] = 7 * add_remove
                self.t_squares[y+1][x] = 7 * add_remove
            elif rot == 2:
                if y > 0:
                    self.t_squares[y-1][x] = 7 * add_remove
                self.t_squares[y][x] = 7 * add_remove
                self.t_squares[y][x-1] = 7 * add_remove
                self.t_squares[y][x+1] = 7 * add_remove
            elif rot == 3:
                self.t_squares[y][x+1] = 7 * add_remove
                self.t_squares[y][x] = 7 * add_remove
                if y > 0:
                    self.t_squares[y-1][x] = 7 * add_remove
                self.t_squares[y+1][x] = 7 * add_remove

    def testSpace(self, piece:GridPiece, pos:tuple[int,int], rot):
        def __check__(ns:list[int]):
            for n in ns:
                if n != 0:
                    return False
            return True

        x, y = pos
        if piece == GridPiece.oPiece:
            return __check__([
                self.t_squares[y][x],
                self.t_squares[y][x+1],
                self.t_squares[y+1][x],
                self.t_squares[y+1][x+1]])
        elif piece == GridPiece.iPiece:
            if rot == 0:
                return __check__([
                self.t_squares[y][x],
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y+1][x],
                self.t_squares[y+2][x]])
            elif rot == 1:
                return __check__([
                self.t_squares[y][x],
                self.t_squares[y][x+1],
                self.t_squares[y][x-1],
                self.t_squares[y][x-2]])
            elif rot == 2:
                return __check__([
                self.t_squares[y][x],
                self.t_squares[y+1][x],
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y-2][x] if y > 1 else 0])
            elif rot == 3:
                return __check__([
                self.t_squares[y][x],
                self.t_squares[y][x-1],
                self.t_squares[y][x+1],
                self.t_squares[y][x+2]])
        elif piece == GridPiece.lPiece:
            if rot == 0:
                return __check__([
                self.t_squares[y][x],
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y+1][x],
                self.t_squares[y+1][x+1]
                ])
            elif rot == 1:
                return __check__([
                self.t_squares[y][x],
                self.t_squares[y][x+1],
                self.t_squares[y][x-1],
                self.t_squares[y+1][x-1]
                ])
            elif rot == 2:
                return __check__([
                self.t_squares[y-1][x-1] if y > 0 else 0,
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y][x],
                self.t_squares[y+1][x]
                ])
            elif rot == 3:
                return __check__([
                self.t_squares[y][x-1],
                self.t_squares[y][x],
                self.t_squares[y][x+1],
                self.t_squares[y-1][x+1] if y > 0 else 0
                ])
        elif piece == GridPiece.jPiece:
            if rot == 0:
                return __check__([
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y][x],
                self.t_squares[y+1][x],
                self.t_squares[y+1][x-1],
                ])
            elif rot == 1:
                return __check__([
                self.t_squares[y-1][x-1] if y > 0 else 0,
                self.t_squares[y][x-1],
                self.t_squares[y][x],
                self.t_squares[y][x+1]
                ])
            elif rot == 2:
                return __check__([
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y-1][x+1] if y > 0 else 0,
                self.t_squares[y][x],
                self.t_squares[y+1][x]
                ])
            elif rot == 3:
                return __check__([
                self.t_squares[y][x-1],
                self.t_squares[y][x],
                self.t_squares[y][x+1],
                self.t_squares[y+1][x+1]
                ])
        elif piece == GridPiece.sPiece:
            if rot == 0 or rot == 2:
                return __check__([
                self.t_squares[y][x-1],
                self.t_squares[y][x],
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y-1][x+1] if y > 0 else 0
                ])
            elif rot == 1 or rot == 3:
                return __check__([
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y][x],
                self.t_squares[y][x+1],
                self.t_squares[y+1][x+1]
                ])
        elif piece == GridPiece.zPiece:
            if rot == 0 or rot == 2:
                return __check__([
                self.t_squares[y][x+1],
                self.t_squares[y][x],
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y-1][x-1] if y > 0 else 0
                ])
            elif rot == 1 or rot == 3:
                return __check__([
                self.t_squares[y-1][x+1] if y > 0 else 0,
                self.t_squares[y][x],
                self.t_squares[y][x+1],
                self.t_squares[y+1][x]
                ])
        elif piece == GridPiece.tPiece:
            if rot == 0:
                return __check__([
                self.t_squares[y][x-1],
                self.t_squares[y][x],
                self.t_squares[y][x+1],
                self.t_squares[y+1][x]
                ])
            elif rot == 1:
                return __check__([
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y][x-1],
                self.t_squares[y][x],
                self.t_squares[y+1][x]
                ])
            elif rot == 2:
                return __check__([
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y][x],
                self.t_squares[y][x-1],
                self.t_squares[y][x+1]
                ])
            elif rot == 3:
                return __check__([
                self.t_squares[y][x+1],
                self.t_squares[y][x],
                self.t_squares[y-1][x] if y > 0 else 0,
                self.t_squares[y+1][x]
                ])


    def __str__(self) -> str:
        return "\n".join(list(map(str, [l for l in self.t_squares])))