import random
from SolveMaze import SolveMaze
from Maze import Maze
from OpenList import OpenList


class Main:
    def __init__(self, size):
        self.agent_maze = Maze().generate_blank_maze(size)
        self.actual_maze = Maze().generate_actual_maze(size)
        self.size = size

    def traverse_path(self, goal_node, start_node):
        path = [goal_node]
        currentNode = goal_node
        while currentNode is not start_node:
            currentNode = currentNode.parent
            path.append(currentNode)
        return path

    def bolckage_status_of_children(self, start_node, start_node_actual):
        if start_node_actual.right_child is not None:
            start_node.right_child.cost = start_node_actual.right_child.cost
        if start_node_actual.left_child is not None:
            start_node.left_child.cost = start_node_actual.left_child.cost
        if start_node_actual.top_child is not None:
            start_node.top_child.cost = start_node_actual.top_child.cost
        if start_node_actual.down_child is not None:
            start_node.down_child.cost = start_node_actual.down_child.cost

    def main_A_forward(self):
        counter = 0

        while True:
            start_node = self.agent_maze[random.randint(0, self.size-1)][random.randint(0, self.size-1)]
            goal_node = self.agent_maze[random.randint(0, self.size-1)][random.randint(0, self.size-1)]
            start_node_actual = self.actual_maze[start_node.x][start_node.y]
            goal_node_actual = self.actual_maze[goal_node.x][goal_node.y]
            if (start_node_actual.cost == 1) & (goal_node_actual.cost == 1) & (start_node != goal_node):
                break

        self.bolckage_status_of_children(start_node, start_node_actual)

        print("start", start_node.x, start_node.y, goal_node.x, goal_node.y)

        solvedMaze = []

        while start_node is not goal_node:
            counter += 1
            start_node.update_g(0)
            start_node.update_h(goal_node)
            start_node.update_search(counter)

            goal_node.update_g(float("inf"))
            goal_node.update_search(counter)

            open_list = OpenList()
            open_list.insert(start_node)
            closed_list = set()

            SolveMaze().forward_A_star(open_list, closed_list, goal_node, self.agent_maze)

            if open_list.is_empty is True and goal_node not in closed_list:
                print("I can't reach the target")
                return

            path = self.traverse_path(goal_node, start_node)
            path.reverse()

            for i in path:
                if i.cost == self.actual_maze[i.x][i.y].cost:
                    solvedMaze.append(i)
                else:
                    start_node = solvedMaze.pop()
                    start_node_actual = self.actual_maze[start_node.x][start_node.y]
                    self.bolckage_status_of_children(start_node, start_node_actual)
                    break

            if solvedMaze[len(solvedMaze)-1] == goal_node:
                print("I reached the goal: ")
                for a in solvedMaze:
                    a.print()
                return

for i in range(10):
    Main(101).main_A_forward()
