import random
from SolveMaze import SolveMaze
from Maze import Maze
from OpenList import OpenList
from tkinter import *
from Visual import Visual

class Main:
    def traverse_path(self, goal_node, start_node):
        path = [goal_node]
        currentNode = goal_node
        while currentNode is not start_node:
            currentNode = currentNode.parent
            path.append(currentNode)
        return path

    def blockage_status_of_children(self, start_node, start_node_actual, w):
        for i in range(0, 4):
            if i == 0 and start_node_actual.right_child is not None:
                start_node.right_child.cost = start_node_actual.right_child.cost
                w.blocked(start_node.right_child)
            elif i == 1 and start_node_actual.left_child is not None:
                start_node.left_child.cost = start_node_actual.left_child.cost
                w.blocked(start_node.left_child)
            elif i == 2 and start_node_actual.top_child is not None:
                start_node.top_child.cost = start_node_actual.top_child.cost
                w.blocked(start_node.top_child)
            elif i == 3 and start_node_actual.down_child is not None:
                start_node.down_child.cost = start_node_actual.down_child.cost
                w.blocked(start_node.down_child)
        w.master.update()

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

        w.showMaze(agent_maze)
        w.start(start_node)
        self.blockage_status_of_children(start_node, start_node_actual, w)

        print("start", start_node.x, start_node.y, goal_node.x, goal_node.y)
        solvedMaze = []
        w.goal(goal_node)
        w.start(start_node)
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

            SolveMaze().forward_A_star(open_list, closed_list, goal_node, agent_maze, w)

            if open_list.is_empty is True and goal_node not in closed_list:
                print("I can't reach the target")
                break

            path = self.traverse_path(goal_node, start_node)

            # parent = path.pop()
            # while path != [] and solvedMaze != []:
            #     i = path.pop()
            #     if i.cost == actual_maze[i.x][i.y].cost:
            #         if i in solvedMaze:
            #             for i in range(solvedMaze)
            #             solvedMaze.pop()
            #             parent = i
            #         else:
            #             solvedMaze.append(parent)
            #             path.append(i)
            #             break
            path.reverse()
            path = w.pathLine(path)
            w.master.update()
            for i in path:
                if i.cost == actual_maze[i.x][i.y].cost:
                    if i in solvedMaze:
                        del solvedMaze[solvedMaze.index(i)+1: len(solvedMaze)]
                        continue
                    solvedMaze.append(i)
                else:
                    start_node = solvedMaze.pop()
                    start_node_actual = actual_maze[start_node.x][start_node.y]
                    self.blockage_status_of_children(start_node, start_node_actual, w)
                    break




            if solvedMaze[len(solvedMaze)-1] == goal_node:
                print("I reached the goal: ")
                w.showMaze(actual_maze)
                w.start(w.startNode)
                w.goal(w.goalNode)
                w.pathLine(solvedMaze)
                for a in solvedMaze:
                    a.print()
                break

        mainloop()
        return


Main().main_A_forward(25)