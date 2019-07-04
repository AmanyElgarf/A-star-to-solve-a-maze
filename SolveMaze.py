from Maze import Maze
from PriorityQueue import PriorityQueue
from Node import Node

import math
class SolveMaze:

    def forward_A_star(self, open_list, closed_list, start_node, goal_node, counter):

        while goal_node.f > open_list.get_min().f:
            current = open_list.del_min()
            closed_list.add(current)
            child = Node()
            child = None
            for i in range(0, 4):
                if i == 0: child = current.right_child
                if i ==1: child = current.left_child
                if i ==2: child = current.top_child
                if i ==3: child = current.down_child
                if child is None: i += 1
                if child.counter < counter:
                    child.g = math.inf
                    child.counter = counter
                if child.g > current.g + child.cost:
                    child.g = current.g + child.cost
                    child.parent = [current.x, current.y]
                    child.h = child.manhattan_distance(child, goal_node)
                    child.f = child.g + child.h
                    open_list.insert(child)


