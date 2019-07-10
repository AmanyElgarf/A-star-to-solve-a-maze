import math


class SolveMaze:
    def forward_A_star(self, open_list, closed_list, goal_node, counter):
        counter = 0
        while (open_list.is_empty() is False):
            counter += 1
            print()
            print("Forward A* #", counter)
            current = open_list.del_min()
            if current in closed_list: continue
            closed_list.add(current)
            for i in range(0, 4):
                child = current.traverse_children(i)
                if child is None: continue
                if (open_list.contains(child) == False) or (child not in closed_list):
                    child.g = math.inf
                    child.h = child.update_h(goal_node)
                #    child.search = counter
                if child not in closed_list:
                    if (child.cost != 1):
                        closed_list.add(child)
                        continue
                    print("Inserting child to open: ", print(child))
                    if child.g > current.g + child.cost:
                        child.g = current.g + child.cost
                        child.parent = [current.x, current.y]
                        open_list.insert(child)

    def backward_A_star(self, open_list, closed_list, goal_node, counter):
        while goal_node.f > open_list.get_min().f:
            current = open_list.del_min()
            closed_list.add(current)
            child = current

            for i in range(0, 4):
                if i == 0:
                    child = current.right_child
                    if child is None:
                        i += 1
                if i == 1:
                    child = current.left_child
                    if child is None:
                        i += 1
                if i == 2:
                    child = current.top_child
                    if child is None:
                        i += 1
                if i == 3:
                    child = current.down_child
                    if child is None:
                        i += 1

                if child.search < counter:
                    child.g = math.inf
                    child.search = counter

                if child.g > current.g + child.cost:
                    child.g = current.g + child.cost
                    child.parent = [current.x, current.y]
                    child.h = child.manhattan_distance(child, goal_node)
                    open_list.insert(child)

