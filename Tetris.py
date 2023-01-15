from threading import Thread

def config():
    from os import system
    from time import sleep   
    system("mode con cols=45 lines=24")
    if __name__ == '__main__': 
        Setup().run()

class Rendering():
    def StdRender(self):
        print("\n\n")
        print("╔",end="")
        print("═"*21, end="")
        print("╗")
        for j in range(5, 26):  
            print("║ ",end="")
            for i in range(10):
                print(map[j][i+1], end=" ")
            if j == 10:
                print("║     SCORE: ", Score)
                continue
            if j == 11:
                print("║     LEVEL: ", level,"")
                continue
            if j == 13:
                print("║     NEXT SHAPE: """)
                continue
            if j == 14:
                print("║     ",nsg[1][3],nsg[1][4],nsg[1][5],nsg[1][6],"")
                continue
            if j == 15:
                print("║     ",nsg[2][3],nsg[2][4],nsg[2][5],nsg[2][6],"")
                continue
            if j == 16:
                print("║     ",nsg[3][3],nsg[3][4],nsg[3][5],nsg[3][6],"")
                continue
            if j == 17:
                print("║     ",nsg[4][3],nsg[4][4],nsg[4][5],nsg[4][6],"")
                continue
            print("║")
        print("╚", end="")
        print("═"*21, end="")
        print("╝")

class Spawn():
    @classmethod
    def STDspawn(self):    
        from random import randint
        global shape,nextshape, nsg
        shapes_number,temp_shape = randint(0,6),["I","J","L","O","Z","T","S"]
        if nextshape != None:
            shape = Settings().shapes()[temp_shape[nextshape]]
            nextshape = randint(0,6)
        else:
            nextshape = randint(0,6)
            for i in range(7):
                if shapes_number == i: shape = Settings().shapes()[temp_shape[i]]
        Settings().shapes(),Settings().Other()
        for i in range(0,8,2): map[shape[rotate[face]]["Item"][i]] [shape[rotate[face]]["Item"][i+1]] = icon
        for i in range(0,8,2):nsg[Settings().shapes()[temp_shape[nextshape]]["N"]["Item"][i]] [Settings().shapes()[temp_shape[nextshape]]["N"]["Item"][i+1]] = "■"

class Settings():
    @classmethod
    def shapes(self):
        shape = {"I":{"N": {"Item": [1,5,2,5,3,5,4,5],"DZ":{"Left":[1,4,2,4,3,4,4,4],"Right":[1,6,2,6,3,6,4,6],"Bottom":[5,5]}},"E": {"Item": [2,3,2,4,2,5,2,6],"DZ":{"Left":[2,2],"Right":[2,7],"Bottom":[3,3,3,4,3,5,3,6]}},"S": {"Item": [1,4,2,4,3,4,4,4],"DZ":{"Left":[1,3,2,3,3,3,4,3],"Right":[1,5,2,5,3,5,4,5],"Bottom":[5,4]}},"W": {"Item": [3,3,3,4,3,5,3,6],"DZ":{"Left":[3,2],"Right":[3,7],"Bottom":[4,3,4,4,4,5,4,6]}}},"J":{"N": {"Item": [2,5,3,5,4,4,4,5],"DZ":{"Left":[2,4,3,4,4,3],"Right":[2,6,3,6,4,6],"Bottom":[5,4,5,5]}},"E": {"Item": [2,4,3,4,3,5,3,6],"DZ":{"Left":[2,3,3,3],"Right":[3,7],"Bottom":[4,4,4,5,4,6]}},"S": {"Item": [2,5,2,6,3,5,4,5],"DZ":{"Left":[2,4,3,4,4,4],"Right":[2,7,3,6,4,6],"Bottom":[3,6,5,5]}},"W": {"Item": [3,4,3,5,3,6,4,6],"DZ":{"Left":[3,3,4,5],"Right":[3,7,4,7],"Bottom":[4,4,4,5,5,6]}}},"L":{"N": {"Item": [2,5,3,5,4,5,4,6],"DZ":{"Left":[2,4,3,4,4,4],"Right":[2,6,3,6,4,7],"Bottom":[5,5,5,6]}},"E": {"Item": [3,4,3,5,3,6,4,4],"DZ":{"Left":[3,3,4,3],"Right":[3,7,4,5],"Bottom":[4,5,4,6,5,4]}},"S": {"Item": [2,4,2,5,3,5,4,5],"DZ":{"Left":[2,3,3,4,4,4],"Right":[2,6,3,6,4,6],"Bottom":[3,4,5,5]}},"W": {"Item": [2,6,3,4,3,5,3,6],"DZ":{"Left":[3,3],"Right":[2,7,3,7],"Bottom":[4,4,4,5,4,6]}}},"O":{"N": {"Item": [3,5,3,6,4,5,4,6],"DZ":{"Left":[3,4,4,4],"Right":[3,7,4,7],"Bottom":[5,5,5,6]}},"E": {"Item": [3,5,3,6,4,5,4,6],"DZ":{"Left":[3,4,4,4],"Right":[3,7,4,7],"Bottom":[5,5,5,6]}},"S": {"Item": [3,5,3,6,4,5,4,6],"DZ":{"Left":[3,4,4,4],"Right":[3,7,4,7],"Bottom":[5,5,5,6]}},"W": {"Item": [3,5,3,6,4,5,4,6],"DZ":{"Left":[3,4,4,4],"Right":[3,7,4,7],"Bottom":[5,5,5,6]}}},"Z":{"N": {"Item": [3,4,3,5,4,5,4,6],"DZ":{"Left":[3,3,4,4],"Right":[4,7],"Bottom":[4,4,5,5,5,6]}},"E": {"Item": [2,5,3,4,3,5,4,4],"DZ":{"Left":[3,3,4,3],"Right":[2,6,3,6,4,5],"Bottom":[4,5,5,4]}},"S": {"Item": [2,4,2,5,3,5,3,6],"DZ":{"Left":[2,3,3,4],"Right":[3,7],"Bottom":[3,4,4,5,4,6]}},"W": {"Item": [2,6,3,5,3,6,4,5],"DZ":{"Left":[3,4,4,4],"Right":[2,7,3,7,4,6],"Bottom":[4,6,5,5]}}},"T":{"N": {"Item": [3,5,4,4,4,5,4,6],"DZ":{"Left":[4,3],"Right":[4,7],"Bottom":[5,4,5,5,5,6]}},"E": {"Item": [3,5,4,5,4,6,5,5],"DZ":{"Left":[3,4,4,4,5,4],"Right":[4,7,5,6],"Bottom":[5,6,6,5]}},"S": {"Item": [4,4,4,5,4,6,5,5],"DZ":{"Left":[4,3,5,4],"Right":[4,7,5,6],"Bottom":[5,4,5,6,6,5]} },"W": {"Item": [3,5,4,4,4,5,5,5],"DZ":{"Left":[4,3,5,4],"Right":[3,6,4,6,5,6],"Bottom":[5,4,6,5]}}},"S":{"N": {"Item": [3,5,3,6,4,4,4,5],"DZ":{"Left":[4,3],"Right":[3,7,4,6],"Bottom":[4,6,5,4,5,5]}},"E": {"Item": [2,4,3,4,3,5,4,5],"DZ":{"Left":[2,3,3,3,4,4],"Right":[3,6,4,6],"Bottom":[4,4,5,5]}},"S": {"Item": [2,5,2,6,3,4,3,5],"DZ":{"Left":[3,3],"Right":[2,7,3,6],"Bottom":[3,6,4,4,4,5]}},"W": {"Item": [2,5,3,5,3,6,4,6],"DZ":{"Left":[2,4,3,4,4,5],"Right":[3,7,4,7],"Bottom":[4,5,5,6]}}}}
        return shape
    def maps(self):
        global map
        map = [ ["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D"," "," "," "," "," "," "," "," "," "," ","D"],["D","D","D","D","D","D","D","D","D","D","D","D"] ]
    @classmethod
    def Other(self):
        from random import choice
        global icon, rotate, face, FPS,difficulty,lock,nsg
        nsg = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
        icon = choice("ODQ@0")
        lock = False
        rotate = ["N","E","S","W"]
        face = 0
        difficulty = 1
        FPS = 75
    def private(self):
        global Score, gameover,difficulty,level,nextshape
        nextshape = None
        level = 1
        gameover = False
        Score = 0

class Overlay():
    def gameovers(self):
        from time import sleep
        from os import system
        global gameover
        gameover = True
        system("cls")
        print("\n\n\n\n\n\n                GAME OVER\n\n             Your score: ",Score)
        sleep(5)
        system("cls")
        SetupStart = Setup().start() 

class Setup(Thread):
    def run(self):
        from time import sleep
        from os import system
        provt,maps,shap,settings,spawn,move,tk = Settings().private(),Settings().maps(),Settings().shapes(), Settings().Other(), Spawn().STDspawn(),Movement().start(),Tick().start()
        while gameover == False:
                system("cls")
                Rendering().StdRender()
                #sleep(1/FPS)
                 
class Movement(Thread):
    def left(self):
        temp_shape = ["Left","Right","Bottom"]
        for n in range(4):
            for i in range(1, len(shape[rotate[n]]["Item"]), 2): shape[rotate[n]]["Item"][i] -= 1
            for j in range(3): 
                for b in range(1, len(shape[rotate[n]]["DZ"][temp_shape[j]]), 2): shape[rotate[n]]["DZ"][temp_shape[j]][b] -= 1
    def right(self):
        temp_shape = ["Left","Right","Bottom"]
        for n in range(4):
            for i in range(1, len(shape[rotate[n]]["Item"]), 2): shape[rotate[n]]["Item"][i] += 1
            for j in range(3): 
                for b in range(1, len(shape[rotate[n]]["DZ"][temp_shape[j]]), 2): shape[rotate[n]]["DZ"][temp_shape[j]][b] += 1
    def rotate(self):
        global face
        if face == 3: face = 0
        else: face += 1 
        for i in range(0, len(shape[rotate[face]]["Item"]), 2):
            if map[shape[rotate[face]]["Item"][i]] [shape[rotate[face]]["Item"][i+1]] == "D" or map[shape[rotate[face]]["Item"][i]] [shape[rotate[face]]["Item"][i+1]] == icon:
                if face == 0:
                    face = 3
                else:
                    face -= 1
    def run(self):
        from msvcrt import getch
        global position,difficulty, Score
        while gameover == False:  
            key = ord(getch())
            if key == 80:
                Tick.clear(self)
                Tick.fall(self)
                colinfo = Collisions.FloorCollision()
                if colinfo == 'EXIT':
                    continue
            if key == 77: # Right
                colinfo = Collisions.RightWallCollision()
                if colinfo != 'EXIT':
                    Tick.clear(self)
                    Movement.right(self)
            if key == 75: # Left
                colinfo = Collisions.LeftWallCollision()
                if colinfo != 'EXIT':
                    Tick.clear(self)
                    Movement.left(self)
            if key == 32: # Rotate
                Tick.clear(self)
                Movement.rotate(self)

class Fall(Thread):
    def run(self):
        from time import sleep
        while gameover == False:
            if lock == False:
                Tick.clear(self)
                if map[5][1] != " " or map[5][2] != " " or map[5][3] != " " or map[5][4] != " " or map[5][5] != " " or map[5][6] != " " or map[5][7] != " " or map[5][8] != " " or map[5][9] != " " or map[5][10] != " ":
                        Overlay().gameovers()
                        break
                Tick.fall(self)
                sleep(difficulty/level)

class Tick(Thread):
    def fall(self):
        temp_shape = ["Left","Right","Bottom"]
        for n in range(4):
            for i in range(0, len(shape[rotate[n]]["Item"]), 2): shape[rotate[n]]["Item"][i] += 1
            for j in range(3): 
                for b in range(0, len(shape[rotate[n]]["DZ"][temp_shape[j]]), 2): shape[rotate[n]]["DZ"][temp_shape[j]][b] += 1 
    def shape_place(self):
        Tick.clear(self)
        j,h = 0,1
        for i in range(4):
            map[shape[rotate[face]]["Item"][j]][shape[rotate[face]]["Item"][h]] = icon
            j += 2
            h += 2
    def clear(self):
        j,h = 0,1
        for i in range(4):
            map[shape[rotate[face]]["Item"][j]][shape[rotate[face]]["Item"][h]] = " "
            j += 2
            h += 2      
    def run(self):
        from time import sleep
        global lock,Score,level
        f = Fall().start()
        while gameover == False:  
            Tick.clear(self)
            Tick.shape_place(self)
            colinfo = Collisions.FloorCollision()
            if colinfo == 'EXIT':
                Tick.clear(self)
                Tick.shape_place(self)
                colinfo = Collisions.FloorCollision()
                if colinfo == 'EXIT':
                    Spawn.STDspawn()
                    for d in range(21):
                        for j in range(6,26):                          
                            if map[j][1] != " " and map[j][2] != " " and map[j][3] != " " and map[j][4] != " " and map[j][5] != " " and map[j][6] != " " and map[j][7] != " " and map[j][8] != " " and map[j][9] != " " and map[j][10] != " ":
                                for i in range(11):map[j][i] = 'X'
                                sleep(0.1)
                                for i in range(11):map[j][i] = ' '
                                sleep(0.2)
                                for g in range(21):
                                    for i in range(1,11):
                                        map[j][i] = map[j-1][i]
                                        map[j-1][i] = " "
                                    j -= 1
                                if Score == 100: level += 1
                                if Score == 200:level += 1
                                if Score == 300:level += 1
                                if Score == 400:level += 1
                                if Score == 500:level += 1
                                if Score == 600:level += 1
                                Score += 20
                                sleep(1)
                                break
                                
            sleep(1/1024)

class Collisions():
    def FloorCollision():
        for i in range(0, len(shape[rotate[face]]["DZ"]['Bottom']), 2):
            if map[shape[rotate[face]]["DZ"]['Bottom'][i]] [shape[rotate[face]]["DZ"]['Bottom'][i+1]] != " ":
                return 'EXIT'
    def RightWallCollision():
        for i in range(0, len(shape[rotate[face]]["DZ"]['Right']), 2):
            if map[shape[rotate[face]]["DZ"]['Right'][i]] [shape[rotate[face]]["DZ"]['Right'][i+1]] != " ":
                return 'EXIT'
    def LeftWallCollision():
        for i in range(0, len(shape[rotate[face]]["DZ"]['Left']), 2):
            if map[shape[rotate[face]]["DZ"]['Left'][i]] [shape[rotate[face]]["DZ"]['Left'][i+1]] != " ":
                return 'EXIT'

config()