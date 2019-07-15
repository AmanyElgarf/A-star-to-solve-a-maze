from OpenList import OpenList
from OpenListInFavorOfSmallerG import OpenListInFavorOfSmallerG


class SolveMaze:

    def forward_A_star(self, start_node,  goal_node, actual_maze, w):
        start_node.update_g(0)
        start_node.update_h(goal_node)
        goal_node.update_g(float("inf"))
        open_list = OpenList()
        open_list.insert(start_node)
        closed_list = set()
        while open_list.is_empty() is False:
            current = open_list.del_min()
            if current == goal_node:
                return
            if current in closed_list:
                continue
            closed_list.add(current)
            w.inClosed(current)
            #w.master.update()
            for i in range(0, 4):
                child = current.traverse_children(i)
                if child is None: continue
                if child.cost != 1: continue
                if child in closed_list: continue
                if open_list.contains(child) is False:
                    child.update_g(float("inf"))
                    child.update_h(goal_node)
                if child.g > current.g + child.cost:
                    newG = current.g + child.cost
                    child.update_g(newG)
                    child.parent = actual_maze[current.x][current.y]
                    open_list.insert(child)
                    w.inOpen(child)
                    # w.master.update()
        w.master.update()
        if open_list.is_empty() is True and goal_node not in closed_list:
            return 0
        return 1

    def forward_A_star_in_favor_of_smaller_g(self, start_node,  goal_node, actual_maze, w):
        start_node.update_g(0)
        start_node.update_h(goal_node)
        goal_node.update_g(float("inf"))
        open_list = OpenListInFavorOfSmallerG()
        open_list.insert(start_node)
        closed_list = set()
        while open_list.is_empty() is False:
            current = open_list.del_min()
            if current == goal_node:
                return
            if current in closed_list:
                continue
            closed_list.add(current)
            w.inClosed(current)
            #w.master.update()
            for i in range(0, 4):
                child = current.traverse_children(i)
                if child is None: continue
                if child.cost != 1: continue
                if child in closed_list: continue
                if open_list.contains(child) is False:
                    child.update_g(float("inf"))
                    child.update_h(goal_node)
                if child.g > current.g + child.cost:
                    newG = current.g + child.cost
                    child.update_g(newG)
                    child.parent = actual_maze[current.x][current.y]
                    open_list.insert(child)
                    w.inOpen(child)
                    # w.master.update()
        w.master.update()
        if open_list.is_empty() is True and goal_node not in closed_list:
            return 0
        return 1

    def backward_A_star(self, start_node,  goal_node, actual_maze, w):
        goal_node.update_g(0)
        goal_node.update_h(start_node)
        start_node.update_g(float("inf"))
        open_list = OpenList()
        open_list.insert(goal_node)
        closed_list = set()
        while open_list.is_empty() is False:
            current = open_list.del_min()
            if current == start_node:
                return
            if current in closed_list:
                continue
            closed_list.add(current)
            w.inClosedB(current)
            #w.master.update()
            for i in range(0, 4):
                child = current.traverse_children(i)
                if child is None: continue
                if child.cost != 1: continue
                if child in closed_list: continue
                if open_list.contains(child) is False:
                    child.update_g(float("inf"))
                    child.update_h(start_node)
                if child.g > current.g + child.cost:
                    newG = current.g + child.cost
                    child.update_g(newG)
                    child.parent = actual_maze[current.x][current.y]
                    open_list.insert(child)
                    w.inOpen(child)
                    # w.master.update()
        w.master.update()
        if open_list.is_empty() is True and start_node not in closed_list:
            return 0

        return 1    
       
    def adaptive_A_star(self, start_node, goal_node, lastClosedList, w):
        lastGoalCost = goal_node.g
        start_node.update_g(0)
        if lastGoalCost == float("inf"):
            start_node.update_h(goal_node)
        else:
            start_node.update_hnew(lastGoalCost)
        goal_node.update_g(float("inf"))
        open_list = OpenList()
        open_list.insert(start_node)
        closed_list = set()
        while (open_list.is_empty() is False):
            current = open_list.del_min()
            if current == goal_node:
                closed_list.add(current)
                lastClosedList.update(closed_list)
                return 1
            if current in closed_list: continue
            closed_list.add(current)
            w.inClosed(current)
            # w.master.update()
            for i in range(0, 4):
                child = current.traverse_children(i)
                if child is None: continue
                if child.cost != 1: continue
                if child in closed_list: continue
                if open_list.contains(child) == False:
                    if ( len(lastClosedList)==0 and lastGoalCost == float("inf")) or (child.h == 0):
                        child.update_h(goal_node)
                    elif child in lastClosedList:
                        child.update_hnew(lastGoalCost)
                    child.update_g(float("inf"))
                if child.g > current.g + child.cost:
                    newG = current.g + child.cost
                    child.update_g(newG)
                    child.parent = current
                    open_list.insert(child)
                    w.inOpen(child)
                    # w.master.update()
                # w.master.update()
        w.master.update()
        lastClosedList.update(closed_list)
        if open_list.is_empty() is True and goal_node not in closed_list:
            return 0
        return 1
