from colour import Color

class Visual:
    def __init__(self, c, m, distance):
        self.master = m
        self.canvas = c
        self.distance = distance
        self.colors = list(Color("#00FF00").range_to(Color("#FF0000"), 100))
        self.startNode = None
        self.goalNode = None
        self.mazeSize = 0

    def showMaze(self, maze):
        self.mazeSize = len(maze)
        for x in range(0, self.mazeSize):
            for y in range(0, self.mazeSize):
                cell = maze[x][y]
                y1 = (x * self.distance )+self.distance
                x1 = (y * self.distance )+self.distance
                y2 = y1 + self.distance
                x2 = x1 + self.distance
                if cell.cost != 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="#778899", outline="#778899")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF", outline="#FFFFFF")
        self.master.update()

    def blocked(self, cell):
        x = cell.y * self.distance
        y = cell.x * self.distance
        x1 = x+self.distance
        y1 = y+self.distance
        x2 = x1+self.distance
        y2 = y1+self.distance
        if cell.cost != 1:
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="#000000", outline="#000000")

    def start(self, sN):
        self.startNode = sN
        x = self.startNode.y * self.distance
        y = self.startNode.x * self.distance
        x1 = x+self.distance
        y1 = y+self.distance
        x2 = x1+self.distance
        y2 = y1+self.distance
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#000000", outline="#000000")
        self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill='#FF0000', outline='#FF0000')
        self.master.update()

    def goal(self, cell):
        self.goalNode = cell
        x = cell.y * self.distance
        y = cell.x * self.distance
        x1 = x+self.distance
        y1 = y+self.distance
        x2 = x1+self.distance
        y2 = y1+self.distance
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#000000", outline="#000000")
        self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill='#00FF00', outline='#00FF00')
        self.master.update()

    def inOpen(self, cell):
        if (cell == self.startNode) or (cell == self.goalNode): return
        x = cell.y * self.distance
        y = cell.x * self.distance
        x1 = x + self.distance
        y1 = y + self.distance
        x2 = x1 + self.distance
        y2 = y1 + self.distance
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF", outline="#FFFFFF")
        self.canvas.create_oval(x1+2, y1+2, x2-2, y2-2, fill='white', outline='blue')
        #self.master.update()

    def inClosed(self, cell):
        if (cell == self.startNode) or (cell == self.goalNode): return
        percent = cell.h/self.startNode.h
        index = int(percent * 99)
        while (index > 99):
            percent = cell.g / self.goalNode.g
            index = 99-int(percent * 99)
        current = self.colors[index]
        x = cell.y * self.distance
        y = cell.x * self.distance
        x1 = x + self.distance
        y1 = y + self.distance
        x2 = x1 + self.distance
        y2 = y1 + self.distance
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF", outline="#FFFFFF")
        self.canvas.create_oval(x1+2, y1+2, x2-2, y2-2, fill=current, outline=current)
        #self.master.update()

    def pathLine(self, steps):
        parent1 = steps.pop(0)
        parent = parent1
        for current in steps:
            x = parent.y * self.distance
            y = parent.x * self.distance
            x1 = x + self.distance
            y1 = y + self.distance
            x2 = x1 + self.distance
            y2 = y1 + self.distance
            x1 = (x1 + x2) // 2
            y1 = (y1 + y2) // 2

            x = current.y * self.distance
            y = current.x * self.distance
            x2 = x + self.distance
            y2 = y + self.distance
            x3 = x2 + self.distance
            y3 = y2 + self.distance
            x2 = (x2 + x3) // 2
            y2 = (y2 + y3) // 2
            self.canvas.create_line(x1, y1, x2, y2, fill='purple', width=3)
            parent = current
            self.master.update()
        steps.insert(0, parent1)
        return steps

    def finalPath(self, maze, steps):
        self.showMaze(maze)
        self.start(self.startNode)
        self.goal(self.goalNode)
        self.pathLine(steps)


    def noPath(self):
        self.canvas.create_text( self.mazeSize*self.distance//2, self.mazeSize*self.distance//2, text="Path not found")
        self.master.update()