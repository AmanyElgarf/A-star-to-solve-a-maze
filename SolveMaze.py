from OpenList import OpenList


class SolveMaze:
    def forward_A_star(self, start_node,  goal_node, actual_maze):
        counter = 0
        open_list = OpenList()
        open_list.insert(start_node)
        closed_list = set()
        while open_list.is_empty() is False:
            counter += 1
            current = open_list.del_min()
            if current == goal_node:
                return
            if current in closed_list:
                continue
            closed_list.add(current)

            for i in range(0, 4):
                child = current.traverse_children(i)
                if child is None:
                    continue
                if child.cost != 1:
                    continue
                if child in closed_list:
                    continue
                if open_list.contains(child) is False:
                    child.update_g(float("inf"))
                    child.update_h(goal_node)
                if child.g > current.g + child.cost:
                    newG = current.g + child.cost
                    child.update_g(newG)
                    child.parent = actual_maze[current.x][current.y]
                    open_list.insert(child)
        if open_list.is_empty() is True and goal_node not in closed_list:
            return "I can't reach the target"


