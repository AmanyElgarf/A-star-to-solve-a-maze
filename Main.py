import random
from SolveMaze import SolveMaze
from Maze import Maze
from OpenList import OpenList
import math


class Main:
    def __init__(self):
        pass

    def traverse_path(self, goal_node):
        path = []
        index = [goal_node.x, goal_node.y]
        currentNode = goal_node
        while index != [-1, -1]:
            path.append(index)
            for i in range(0,4):
                parentNode = currentNode.traverse_children(i)
                if parentNode is not None:
                    if currentNode.parent == [parentNode.x, parentNode.y]:
                        currentNode = parentNode
                        index = [parentNode.x, parentNode.y]
                        break
                    elif currentNode.parent == [-1, -1]:
                        index = [-1, -1]
                        break
        #print("Path: ")
        #for a in reversed(path):
        #    print( "(", a[0], ", ", a[1], ")")
        #print()
        return path

    def main(self, size):

        counter = 0
        agent_maze = Maze().generate_blank_maze(size)
        actual_maze = Maze().generate_actual_maze(size)

        while True:
            start_node = agent_maze[random.randint(0, size-1)][random.randint(0, size-1)]
            goal_node = agent_maze[random.randint(0, size-1)][random.randint(0, size-1)]
            start_node_actual = actual_maze[start_node.x][start_node.y]
            goal_node_actual = actual_maze[goal_node.x][goal_node.y]
            if (start_node_actual.cost == 1) & (goal_node_actual.cost == 1) & (start_node != goal_node):
                print(start_node, goal_node)
                break

        #tell agent map whether immediate cells are blocked or not
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

        while start_node != goal_node:
            counter += 1
            start_node.update_g(0)
            start_node.update_h(goal_node)
            start_node.update_search(counter)
            start_node.update_parent([-1, -1])

            goal_node.update_g(float("inf"))
            goal_node.update_h(goal_node)
            goal_node.update_search(counter)

            open_list = OpenList()
            open_list.insert(start_node)
            closed_list = set()

            SolveMaze().forward_A_star(open_list, closed_list, goal_node, counter)

            if open_list.is_empty is True:
                print("I can't reach the target")
                return

            path = self.traverse_path(goal_node)

            parentIndex = path.pop()
            parentNode = actual_maze[ parentIndex[0] ][ parentIndex[1] ]
            solvedMaze.append(parentNode)

            for currentIndex in reversed(path):
                currentNode = actual_maze[currentIndex[0]][currentIndex[1]]

                isChild = False
                for j in range(0,4):
                    child = parentNode.traverse_children(j)
                    if child is not None:
                        child.print()
                        if child == currentNode:
                            isChild = True
                            break
                if isChild:
                    if currentNode.cost != 1:
                        start_node = agent_maze[ parentNode.x][ parentNode.y]
                        agent_maze[ currentNode.x][ currentNode.y ].cost = float("inf")
                        solvedMaze.pop()
                        break
                    else:
                        parentNode = currentNode
                        solvedMaze.append(parentNode)
                else:
                    print("A* search error, parent does not have such child")
                    return

            if agent_maze[parentNode.x][parentNode.y] == goal_node:
                print("I reached the goal: ")
                for a in solvedMaze:
                    a.print()
                return


Main().main(3)


