from Node import Node
import math
import random


class Maze:
    def __init__(self):
        pass

    def generate_actual_maze(self, size):
        maze = Maze().generate_blank_maze(size)
        #randomly choose a start cell of the blank maze
        a = []
        for x in range(0, 2):
            r = random.randint(0, size-1)
            a.append(r)

        #create and open and closed list, add start to open
        #print("Start:", a[0], ",", a[1])
        start = maze[a[0]][a[1]]
        open = []
        open.append(start)
        closed = set()

        #while there are unexpanded cells, keep visiting cells
        while (open != []):
            current = open.pop()
            #if cell has been expanded, don't add its neighbors to open list (aka continue)
            if current in closed: 
                continue
            #otherwise add to closed list, and expand
            closed.add(current)
            #randomly access each child, 
            # but ensure that each child is accessed 
            # and that the same child is not accessed more 
            # than once 
            index = [0, 1, 2, 3]
            random.shuffle(index)
            for j in range(0, 4):
                i = index[j]
                child = None
                if i == 0: child = current.right_child
                if i ==1: child = current.left_child
                if i ==2: child = current.top_child
                if i ==3: child = current.down_child
                if (child is None): continue
                #add child to open list (even if blocked to make sure all neighbors visited)
                if (child not in closed) & (child not in open): 
                    isBlocked = random.randint(1, 101)
                    if isBlocked > 70: child.cost = math.inf
                    open.append(child)

        
        #if len(closed) == size*size: print("True")
        #else: print(false)
        #for i in range(0, size):
        #    for j in range(0, size):
        #        if maze[i][j].cost == 1: print("o ", end =""),
        #        else: print("x ", end =""),
        #    print("\n")

    def generate_blank_maze(self, size):
        maze =[]

        for i in range(0, size):
            row = [None for x in range(size)]
            for k in range(0, size):
                cell = Node(i, k)
                row[k] = cell
            maze.append(row)

        for p in range(0, size):
            for j in range(0, size):
                if j != 0:
                    maze[p][j].left_child = maze[p][j-1]
                if j != size-1:
                    maze[p][j].right_child = maze[p][j + 1]
                if p != 0:
                    maze[p][j].top_child = maze[p-1][j]
                if p != size-1:
                    maze[p][j].down_child = maze[p + 1][j]
        return maze

    def generate_fifty_gridworlds(self, size):
        libOfMazes = []
        for x in range(0, 50):
            maze = Maze().generate_actual_maze(size)
            libOfMazes.append(maze)
        return libOfMazes

lib = Maze().generate_fifty_gridworlds(5)