from Node import Node

class Maze:
    def __init__(self):
        pass

    def generate_actual_maze(self, size):

        list =[]

        for i in range(0, size):
            listt = [None for _ in range(size)]
            for k in range(0, size):
                cell = Node(i, k)
                listt[k] = cell
            list.append(listt)

        for p in range(0, size):
            for j in range(0, size):
                if j != 0:
                    list[p][j].left_child = list[p][j-1]
                if j != size-1:
                    list[p][j].right_child = list[p][j + 1]
                if p != 0:
                    list[p][j].top_child = list[p-1][j]
                if p != size-1:
                    list[p][j].down_child = list[p + 1][j]


    def generate_blank_maze(self, size):
        pass

    def generate_fifty_gridworlds(self):
        pass


Maze().generate_actual_maze(3)