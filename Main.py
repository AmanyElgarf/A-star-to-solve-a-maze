import random
from SolveMaze import SolveMaze
from Maze import Maze
from OpenList import OpenList


class Main:
    def traverse_path(self, goal_node, start_node):
        path = []
        index = [goal_node.x, goal_node.y]
        currentNode = goal_node
        while currentNode is not start_node:
            path.append(index)
            currentNode = currentNode.parent
            index = [currentNode.x, currentNode.y]
        path.append([start_node.x, start_node.y])
        return path

    def main_A_forward(self, size):
        counter = 0
        agent_maze = Maze().generate_blank_maze(size)
        actual_maze = Maze().generate_actual_maze(size)

        while True:
            start_node = agent_maze[random.randint(0, size-1)][random.randint(0, size-1)]
            goal_node = agent_maze[random.randint(0, size-1)][random.randint(0, size-1)]
            start_node_actual = actual_maze[start_node.x][start_node.y]
            goal_node_actual = actual_maze[goal_node.x][goal_node.y]
            if (start_node_actual.cost == 1) & (goal_node_actual.cost == 1) & (start_node != goal_node):
                break

        for i in range(0, 4):
            if i == 0 and start_node_actual.right_child is not None:
                start_node.right_child.cost = start_node_actual.right_child.cost
            elif i == 1 and start_node_actual.left_child is not None:
                start_node.left_child.cost = start_node_actual.left_child.cost
            elif i == 2 and start_node_actual.top_child is not None:
                start_node.top_child.cost = start_node_actual.top_child.cost
            elif i == 3 and start_node_actual.down_child is not None:
                start_node.down_child.cost = start_node_actual.down_child.cost

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

            SolveMaze().forward_A_star(open_list, closed_list, goal_node, agent_maze)

            if open_list.is_empty is True and goal_node not in closed_list:
                print("I can't reach the target")
                return

            path = self.traverse_path(goal_node, start_node)

            parentIndex = path.pop()
            parentNode = actual_maze[parentIndex[0]][parentIndex[1]]
            solvedMaze.append(parentNode)

            # compare with actual maze
            for currentIndex in reversed(path):
                currentNode = actual_maze[currentIndex[0]][currentIndex[1]]
                isChild = False
                for j in range(0, 4):
                    child = parentNode.traverse_children(j)
                    if child is not None:
                        if child == currentNode:
                            isChild = True
                            break
                if isChild:
                    if currentNode.cost != 1:
                        start_node = agent_maze[ parentNode.x][ parentNode.y]
                        agent_maze[currentNode.x][currentNode.y].cost = float("inf")
                        solvedMaze.pop()
                        break
                    else:
                        parentNode = currentNode
                        solvedMaze.append(parentNode)
                else:
                    return

            if agent_maze[parentNode.x][parentNode.y] == goal_node:
                print("I reached the goal: ")
                for a in solvedMaze:
                    a.print()
                return
