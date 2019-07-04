import math

class Node:
    def  __init__(self, x, y):
        self.g = None
        self.h = None
        # self.f = self.g + self.h
        self.value = None
        self.parent = [2]
        self.counter = 0
        # not parent of the path is null
        # start is ngative
        self.cost = 1
#         to calculate manhattan distance
        self.x = x
        self.y = y
        self.left_child = None
        self.right_child = None
        self.top_child = None
        self.down_child = None


    def manhattan_distance(self, current_cell, goal):
        return abs(current_cell.x - goal.x) + abs(current_cell.y - goal.y)

    def left_child(self, child):
        self.left_child = child

    def right_child(self, child):
        self.right_child = child

    def top_child(self, child):
        self.top_child = child

    def down_child(self, child):
        self.down_child = child









