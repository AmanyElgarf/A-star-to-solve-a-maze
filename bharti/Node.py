class Node:
    def __init__(self, x, y):
        self.g = 0
        self.h = 0
        self.f = 0
        self.value = None
        # parent should ba an array of size 2
        self.parent = []
        self.search = 0
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

    def update_h(self, goal):
        self.h = abs(self.x - goal.x) + abs(self.y - goal.y)
        self.f = self.h + self.g

    def update_hnew(self, goalC):
        self.h = goalC - self.g
        self.f = self.h + self.g


    def left_child(self, child):
        self.left_child = child

    def right_child(self, child):
        self.right_child = child

    def top_child(self, child):
        self.top_child = child

    def down_child(self, child):
        self.down_child = child

    def update_search(self, search):
        self.search = search

    def update_g(self, new_g):
        self.g = new_g
        self.f = new_g + self.h

    def update_parent(self, new_parent):
        self.parent = new_parent

    def print(self):
        print("(", self.x, ", ", self.y, ")")

    def traverse_children(self, i):
        if i == 0: return self.right_child
        if i == 1: return self.left_child
        if i == 2: return self.top_child
        return self.down_child





