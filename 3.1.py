import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.name = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        # precondition: face east
        t.setheading(0)
        t.penup()
        t.goto(self.dxpos - self.dwidth // 2, self.dypos)
        t.pendown()

        for _ in range(2):
            t.forward(self.dwidth)
            t.left(90)
            t.forward(self.dheight)
            t.left(90)

            # postcondition
            t.penup()
            t.goto(self.dxpos, self.dypos)
            t.setheading(0)

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        # precondition
        t.setheading(0)
        t.penup()
        t.goto(self.dxpos - self.dwidth // 2, self.dypos)
        t.pendown()
        t.color("white")

        for _ in range(2):
            t.forward(self.dwidth)
            t.left(90)
            t.forward(self.dheight)
            t.left(90)

            t.color("black")
            t.penup()
            t.goto(self.dxpos, self.dypos)
            t.setheading(0)


class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        t.setheading(0)
        t.penup()
        t.goto(self.pxpos - self.pthick // 2, self.pypos)
        t.pendown()

        for _ in range(2):
            t.forward(self.pthick)
            t.left(90)
            t.forward(self.plength)
            t.left(90)

            t.penup()
            t.goto(self.pxpos, self.pypos)
            t.setheading(0)

    def pushdisk(self, disk):
        disk.cleardisk()

        new_y = self.pypos + self.toppos
        disk.newpos(self.pxpos, new_y)
        disk.showdisk()

        self.stack.append(disk)
        self.toppos += disk.dheight

    def popdisk(self):
        disk = self.stack.pop()
        self.toppos -= disk.dheight

        disk.cleardisk()
        disk.newpos(disk.dxpos, self.pypos + self.plength + 20)
        disk.showdisk()

        return disk
    

class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)

        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()

        for i in range(n):
            d = Disk("d"+str(i),
            0,
            i*20,
            20,
            (n-i)*30)
            self.startp.pushdisk(d)

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n-1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)




