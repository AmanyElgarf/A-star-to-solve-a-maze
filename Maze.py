from Node import Node
import random


class Maze:
    def __init__(self):
        pass

    def generate_actual_maze(self, size):
        maze = Maze().generate_blank_maze(size)
        start = maze[random.randint(0, size - 1)][random.randint(0, size - 1)]
        open = []
        open.append(start)
        closed = set()
        while (open != []):
            current = open.pop()
            if current in closed:
                continue
            closed.add(current)
            index = [0, 1, 2, 3]
            random.shuffle(index)
            for j in range(0, 4):
                i = index[j]
                child = current.traverse_children(i)
                if (child is None): continue
                if (child not in closed) & (child not in open):
                    isBlocked = random.randint(1, 101)
                    if isBlocked > 70: child.cost = float("inf")
                    open.append(child)
        return maze


    def generate_blank_maze(self, size):
        maze = []
        for i in range(0, size):
            row = [None for x in range(size)]
            for k in range(0, size):
                cell = Node(i, k)
                row[k] = cell
            maze.append(row)

        for p in range(0, size):
            for j in range(0, size):
                if j != 0:
                    maze[p][j].left_child = maze[p][j - 1]
                if j != size - 1:
                    maze[p][j].right_child = maze[p][j + 1]
                if p != 0:
                    maze[p][j].top_child = maze[p - 1][j]
                if p != size - 1:
                    maze[p][j].down_child = maze[p + 1][j]
        return maze


    def generate_fifty_gridworlds(self, size):
        libOfMazes = []
        for x in range(0, 50):
            maze = Maze().generate_actual_maze(size)
            libOfMazes.append(maze)
        return libOfMazes
