from tkinter import *
from Node import Node
from Maze import Maze
from colour import Color

class Visual:
    def __init__(self, c, m):
        self.master = m
        self.canvas = c
        self.distance = distance
        self.colors = list(Color("#00FF00").range_to(Color("#FF0000"), 100))


    def showBlankMaze(self):
        for x in range(self.distance, canvas_width, self.distance):
            self.canvas.create_line(x, 0, x, canvas_height, fill="#476042")
        # horizontal lines at an interval of "line_distance" pixel
        for y in range(self.distance, canvas_height, self.distance):
            self.canvas.create_line(0, y, canvas_width, y, fill="#476042")
        # self.canvas.update()

    def showMaze(self, maze):
        size = len(maze)
        for x in range(0, size):
            for y in range(0, size):
                cell = maze[x][y]
                y1 = (x * self.distance )+self.distance
                x1 = (y * self.distance )+self.distance
                y2 = y1 + self.distance
                x2 = x1 + self.distance
                if cell.cost != 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="#E8E8E8", outline="#E8E8E8")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF", outline="#FFFFFF")

    def blocked(self, cell):
        x = cell.y * self.distance
        y = cell.x * self.distance
        x1 = x+self.distance
        y1 = y+self.distance
        x2 = x1+self.distance
        y2 = y1+self.distance
        self.canvas.create_rectangle(x1,y1,x2,y2, fill='#E8E8E8', outline='#E8E8E8')

    def start(self, cell):
        x = cell.y * self.distance
        y = cell.x * self.distance
        x1 = x+self.distance
        y1 = y+self.distance
        x2 = x1+self.distance
        y2 = y1+self.distance
        self.canvas.create_oval(x1,y1,x2,y2, fill='#FF0000', outline='#FF0000')

    def goal(self, cell):
        x = cell.y * self.distance
        y = cell.x * self.distance
        x1 = x+self.distance
        y1 = y+self.distance
        x2 = x1+self.distance
        y2 = y1+self.distance
        self.canvas.create_oval(x1,y1,x2,y2, fill='#00FF00', outline='#00FF00')


    def inOpen(self, cell):
        x = cell.y * self.distance
        y = cell.x * self.distance
        x1 = x + self.distance
        y1 = y + self.distance
        x2 = x1 + self.distance
        y2 = y1 + self.distance
        self.canvas.create_oval(x1, y1, x2, y2, fill='white', outline='blue')

    def inClosed(self, cell, start):
        percent = cell.h/start.h
        index = int(percent * 99)
        current = self.colors[index]
        x = cell.y * self.distance
        y = cell.x * self.distance
        x1 = x + self.distance
        y1 = y + self.distance
        x2 = x1 + self.distance
        y2 = y1 + self.distance
        self.canvas.create_oval(x1, y1, x2, y2, fill=current, outline=current)

    def pathLine(self, parent, current):
        x = parent.y * self.distance
        y = parent.x * self.distance
        x1 = x + self.distance
        y1 = y + self.distance
        x2 = x1 + self.distance
        y2 = y1 + self.distance
        x1 = (x1+x2)//2
        y1 = (y1+y2)//2

        x = current.y * self.distance
        y = current.x * self.distance
        x2 = x + self.distance
        y2 = y + self.distance
        x3 = x2 + self.distance
        y3 = y2 + self.distance
        x2 = (x2+x3)//2
        y2 = (y2+y3)//2
        self.canvas.create_oval(x1,y1,x2,y2, fill='#EFF769', width=3)


# master = Tk()
# mazeSize = 101
# distance = 6
# maze = Maze().generate_actual_maze(mazeSize)
# for i in range(0, mazeSize):
#     for j in range(0, mazeSize):
#         if maze[i][j].cost == 1:
#             print("o ", end=""),
#         else:
#             print("x ", end=""),
#     print("\n")
# canvas_width = mazeSize*distance+distance*2
#     # mazeSize*5+10
# canvas_height = mazeSize*distance+distance*2
#     # mazeSize*5+10
# canV = Canvas(master,
#            width=canvas_width,
#            height=canvas_height)
# w = Visual(canV, master)
# canV.pack()
# # w.showBlankMaze()
# w.showMaze(maze)
# start = Node(2,2)
# cell1 = Node(34,43)
# end = Node(99, 99)
#
# start.update_h(end)
# cell1.update_h(end)
# end.update_h(end)
#
# w.start(start)
# w.goal(end)
# w.inClosed(start, start)
# w.inClosed(cell1, start)
# mainloop()
