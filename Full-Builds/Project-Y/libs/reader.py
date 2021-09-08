# read each line and parse the student's data
# save each student as a Student object
from typing import List
import libs.creator, array

def parseStudents() -> List:
    students = []
    file = open("./res/Student_Data.csv", "rt")
    file.readline()
    piping = True
    libs.creator._CreationOverseer.usedIds.clear()
    while piping:
        BUFFER: str = file.readline().strip()
        if len(BUFFER) <= 0: piping = False; break
        BUFFER_DATA = BUFFER.split(",")
        # `print(len(BUFFER_DATA))
        BUFFER = libs.creator._Student(BUFFER_DATA[2], BUFFER_DATA[1], int(BUFFER_DATA[3]), int(BUFFER_DATA[0][:4]), BUFFER_DATA[0][4:])
        students.append(BUFFER)
        libs.creator._CreationOverseer.usedIds.append(BUFFER_DATA[0])
    return students

class UI:
    @staticmethod
    def createInterface(list: List) -> None:
        try:
            RUNNING: bool = True
            while RUNNING:
                ui: str = input("> ")
                if ui == "":
                    RUNNING = False
                    continue
                ui_buff = ui.lower().split()
                if len(ui_buff) < 1:
                    print("Invalid Syntax\n")
                    continue
                while len(ui_buff) > 2:
                    ui_buff.pop(2)
                # print("{ub} :: size {s}".format(ub=ui_buff, s=len(ui_buff)))
                sw_1 = {"freshman":0,"sophmore":1,"junior":2,"senior":3,"generate":4,"list":5,"make":6}
                sw_2 = {"age":0,"year":1,"first":2,"last":3,"id":4,"email":5,"amount":6}
                sw_3 = {0:2024,1:2023,2:2022,3:2021}
                grade: int = sw_1.get(ui_buff[0])
                if grade == 4:
                    amnt = int(ui_buff[1])
                    if not libs.creator.generate(amnt):
                        print("Error: Number out of range!\n")
                        continue
                    list = parseStudents()
                    continue
                elif grade == 5:
                    for i in list:
                        print(str(i).replace(",", ", "))
                    print("")
                    continue
                elif grade == 6:
                    name = input("\tName: ").split()
                    firstName: str = name[0]
                    lastName: str = name[1]
                    year: int
                    age: int
                    try:
                        year = int(input("\tYear: "))
                        age = int(input("\tage: "))
                    except Exception:
                        print("Invalid Syntax\n")
                        continue
                    libs.creator.create(libs.creator._Student(firstName, lastName, age, year))
                    print("")
                    continue
                if not len(ui_buff) >= 2:
                    print("Invalid Syntax\n")
                    continue
                command: int = sw_2.get(ui_buff[1])
                gradeYear: int = sw_3.get(grade)
                if grade == None or command == None or gradeYear == None:
                    print("Invalid Syntax\n")
                    continue
                FLAG_COUNTER: bool = False
                SIZE: int = 0
                for i in list:
                    if i.year == gradeYear:
                        if command == 6 or FLAG_COUNTER == True:
                            FLAG_COUNTER = True
                            SIZE += 1
                            continue
                        elif command == 1:
                            print(gradeYear)
                            break
                        elif command == 0:
                            ages = []
                            for k in list:
                                if k.year == gradeYear:
                                    ages.append(k.age)
                            ages.sort()
                            print("{n} - {x} years old".format(n=ages[0], x=ages[-1]))
                            break
                        resp = {2:i.first,3:i.last,4:i.ID,5:i.email}
                        print(resp.get(command))
                if command == 6:
                    if grade == 0:
                        print("There are {num} freshmen".format(num=SIZE))
                    else:
                        print("There are {num} {g}s".format(num=SIZE, g=ui_buff[0]))
                FLAG_COUNTER = False
                SIZE = 0
                ui_buff.clear()
                print("")
        except KeyboardInterrupt:
            pass