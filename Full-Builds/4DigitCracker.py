# This is to be used for fun, and not for anything illegal.
# If you do I'm not responsible

import time
import os
import random
cls = lambda: os.system("CLS")
SOLVED = False
SOL = ""
Average = 1.27
tryHard = 5004
r = 0


def Setup():
    global SOLVED, SOL
    SOLVED = False
    SOL = ""

def Assign():
    global SOL, r, f, g, e
    if r == 1:
        SOL = input("Solution: ")
        cls()
        print("--=--=--=--=--=--=--=--=--=--")
        print("Solution: {}".format(f))
        print("Broken in {}/10,000 lines".format(g))
        print("Elapsed time: {} seconds".format(e))
        print("Average time: {} seconds".format(Average))
        print("Used {} times!".format(tryHard))
        print("--=--=--=--=--=--=--=--=--=--")
        return
    r = 1
    cls()
    print("--=--=--=--=--=--=--=--=--=--")
    print("Solution: ")
    print("Broken in 0/10,000 lines")
    print("Elapsed time: 0 seconds")
    print("Average time: {} seconds".format(Average))
    print("Used {} times!".format(tryHard))
    print("--=--=--=--=--=--=--=--=--=--")
    SOL = input("Solution: ")
    cls()
    print("--=--=--=--=--=--=--=--=--=--")
    print("Solution: ")
    print("Broken in 0/10,000 lines")
    print("Elapsed time: 0 seconds")
    print("Average time: {} seconds".format(Average))
    print("Used {} times!".format(tryHard))
    print("--=--=--=--=--=--=--=--=--=--")
    
    #if len(SOL) < 4 or len(SOL) > 4:
    #    print("\nPlease enter a 4 digit code")
    #    Main()


def Solution():
    global SOLVED, SOL
    startTime = time.time()
    y = 1
    Attempts = []
    Orderer = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]
    while SOLVED != True:
        if y > 10000:
            print("Error Solution Not Found!")
            break
        Orderer = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]
        MASTER = ""
        random.shuffle(Orderer)
        for i in range(4):
            MASTER = MASTER + str(Orderer[i - 1])
        if MASTER in Attempts:
            continue
        #print("{}: ".format(y), MASTER, sep="")
        print("Trying: {0}!".format(MASTER), end="\r")
        if MASTER == SOL:
            global Average, tryHard, e, f, g
            tryHard += 1
            finalTime = round(time.time() - startTime, 2)
            e = finalTime
            f = MASTER
            g = y
            if finalTime > Average:
                Average = Average + 0.01
            elif finalTime < Average:
                Average = Average - 0.01
            cls()
            print("--=--=--=--=--=--=--=--=--=--")
            print("Solution: {}".format(MASTER))
            print("Broken in {}/10,000 lines".format(y))
            print("Elapsed time: {} seconds".format(finalTime))
            print("Average time: {} seconds".format(Average))
            print("Used {} times!".format(tryHard))
            print("--=--=--=--=--=--=--=--=--=--")
            SOLVED = True
        Attempts.append(MASTER)

        MASTER = ""
        Orderer.clear()
        y += 1

def Main():
    while True:
        try:
            Setup()
            Assign()
            Solution()
        except KeyboardInterrupt:
            exit()

Main()


# Written by MayoIsASauce on github, uploaded 1/28/20
