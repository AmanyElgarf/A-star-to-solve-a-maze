
import math

class SolveMaze:

    def forward_A_star(self, open_list, closed_list, start_node, goal_node, counter):

        while goal_node.f > open_list.get_min().f:
            current = open_list.del_min()
            closed_list.add(current)
            child = start_node

            for i in range(0, 4):
                if i == 0:
                    child = start_node.right_child
                    if child is None:
                        i += 1
                if i == 1:
                    child = start_node.left_child
                    if child is None:
                        i += 1
                if i == 2:
                    child = start_node.top_child
                    if child is None:
                        i += 1
                if i == 3:
                    child = start_node.down_child
                    if child is None:
                        i += 1

                if child.search < counter:
                    child.g = math.inf
                    child.search = counter

                if child.g > start_node.g + child.cost:
                    child.g = start_node.g + child.cost
                    child.parent = [start_node.x, start_node.y]
                    child.h = child.manhattan_distance(child, goal_node)
                    open_list.insert(child)


