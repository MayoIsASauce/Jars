import random

class _CreationOverseer:
    usedIds: list = []
    firstNames: str = ["Timothy", "John", "Marcus", "Matthew", "Todd", "Jeremy", "Lucas", "Brendan", "Colin", "Gregory", "Breanna", "Tom"]
    lastNames: str = ["Doe", "O'Hanna", "Stevens", "Smith", "August", "Johnson", "Miller", "Jones", "Williams", "Anderson", "Lewis"]
    years: int = [2022,2023,2024,2025]

class _Student:
    def __init__(self, Fname, Lname, Age, Year, Id = ""):
        failed: bool = False
        self.first = Fname
        self.last = Lname
        self.age = Age
        self.year = Year
        if Id == "":
            triedIds: list = []
            while True:
                # print("tried: " + str(len(triedIds)))
                # print("master: " + str(len(_CreationOverseer.usedIds)))
                if len(triedIds) >= 999:
                    failed = True
                    # print("FAILED: " + self.year)
                    break
                newID = "{0}{1}{2}{3}".format(self.year, random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
                print(newID)
                if (newID in triedIds) or (newID in _CreationOverseer.usedIds):
                    # print("newID in tried or in master")
                    triedIds.append(newID)
                    continue
                break
            self.ID = newID if not failed else "-999"
        else: self.ID = Id
        self.email = "{inital}{Last}{ID}@sjvhs.com".format(inital=self.first[0].lower(), Last=self.last.lower(), ID=self.ID)
    def __str__(self) -> str:
        return "{0},{1},{2},{3},{4}\n".format(self.ID, self.last, self.first, self.age, self.email)
    first: str
    last: str
    age: int
    year: int
    ID: str
    email: str

def create(student: _Student) -> bool:
    file = open("./res/Student_Data.csv", "at")
    file.write(str(student))
    file.close()
    return True

def generate(amnt: int) -> bool:
    year_locks: bool = [False,False,False,False]
    if amnt > 3996 or len(_CreationOverseer.usedIds) >=  3996:
        return False
    for i in range(amnt):
        _fname = _CreationOverseer.firstNames[random.randint(0, len(_CreationOverseer.firstNames)-1)]
        _lname = _CreationOverseer.lastNames[random.randint(0, len(_CreationOverseer.lastNames)-1)]
        percentChance = random.randint(0,100)
        if percentChance <= 25 and not year_locks[0]:
            _year = _CreationOverseer.years[0]
            if random.randint(0,1):
                _age: int = 18
            else:
                _age: int = 17
        elif percentChance <= 50 and not year_locks[1]:
            _year = _CreationOverseer.years[1]
            if random.randint(0,1):
                _age: int = 17
            else:
                _age: int = 16
        elif percentChance <= 75 and not year_locks[2]:
            _year = _CreationOverseer.years[2]
            if random.randint(0,1):
                _age: int = 16
            else:
                _age: int = 15
        elif percentChance <= 100 and not year_locks[3]:
            _year = _CreationOverseer.years[3]
            if random.randint(0,1):
                _age: int = 15
            else:
                _age: int = 14
        else:
            return True
        _newStudent: _Student = _Student(_fname, _lname, _age, _year)
        if _newStudent.ID != "-999":
            create(str(_newStudent))
            _CreationOverseer.usedIds.append(_newStudent.ID)
        else:
            years = {2022:0,2023:1,2024:2,2025:3}
            year_locks[years.get(_year)] = True
            i-1
    return True
