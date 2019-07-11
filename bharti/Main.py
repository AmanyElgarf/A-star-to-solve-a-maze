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

        self.agent_maze = Maze().generate_blank_maze(size)
        self.actual_maze = Maze().generate_actual_maze(size)

        #start and goal positions that are not blocked
        #remove start == goal node if statement before submitting
        a = []
        start_node = None
        goal_node = None
        start_node_actual = None
        goal_node_actual = None

        while True:
            a = []
            for x in range(4):
                r = random.randint(0, size-1)
                a.append(r)
            start_node = self.agent_maze[ a[0] ][ a[1] ]
            goal_node = self.agent_maze[ a[2] ][ a[3] ]
            start_node_actual = self.actual_maze[ start_node.x ][ start_node.y ]
            goal_node_actual = self.actual_maze[ goal_node.x ][ goal_node.y ]
            if (start_node_actual.cost == 1) & (goal_node_actual.cost == 1) & (start_node != goal_node):
                print(a)
                break

        #tell agent map whether immediate cells are blocked or not
        for i in range(0, 4):
            child = start_node_actual.traverse_children(i)
            if child is not None:
                if i == 0:
                    start_node.right_child.cost = child.cost
                elif i == 1:
                    start_node.left_child.cost = child.cost
                elif i == 2:
                    start_node.top_child.cost = child.cost
                else:
                    start_node.down_child.cost = child.cost

        solvedMaze = []
        self.counter = 0
        while start_node != goal_node:
            start_node.update_g(0)
            start_node.update_h(goal_node)
            start_node.update_parent([-1, -1])

            goal_node.update_g(float("inf"))
            goal_node.update_h(goal_node)

            open_list = OpenList()
            open_list.insert(start_node)
            closed_list = set()

            SolveMaze().forward_A_star(open_list, closed_list, goal_node, self.counter)

            if open_list.is_empty() is True and goal_node not in closed_list:
                print("I can't reach the target")
                return

            path = self.traverse_path(goal_node)

            parentIndex = path.pop()
            parentNode = self.actual_maze[ parentIndex[0] ][ parentIndex[1] ]
            solvedMaze.append(parentNode)

            for currentIndex in reversed(path):
                currentNode = self.actual_maze[currentIndex[0]][currentIndex[1]]

                isChild = False
                for j in range(0,4):
                    child = parentNode.traverse_children(j)
                    if child is not None:
                        #child.print()
                        if child == currentNode:
                            isChild = True
                            break
                if isChild:
                    if currentNode.cost != 1:
                        start_node = self.agent_maze[ parentNode.x][ parentNode.y]
                        self.agent_maze[ currentNode.x][ currentNode.y ].cost = float("inf")
                        solvedMaze.pop()
                        break
                    else:
                        parentNode = currentNode
                        solvedMaze.append(parentNode)
                else:
                    print("A* search error, parent does not have such child")
                    return

            if self.agent_maze[parentNode.x][parentNode.y] == goal_node:
                print("I reached the goal: ")
                #for a in solvedMaze:
                #    a.print()
                return


for x in range(0, 51):
    print(x)
    Main().main(101)
    print()



