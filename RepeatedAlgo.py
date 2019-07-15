from SolveMaze import SolveMaze
from tkinter import *
from Metrics import Metrics


class RepeatedAlgo:
    def __init__(self, size, actual_maze, agent_maze, start_node, goal_node, start_node_actual, goal_node_actual, algo_type):
        self.agent_maze = agent_maze
        self.actual_maze = actual_maze
        self.size = size
        self.solvedMaze = []
        self.start_node = start_node
        self.goal_node = goal_node
        self.start_node_actual = start_node_actual
        self.goal_node_actual = goal_node_actual
        self.w = None
        self.algo_type = algo_type

    def repeated_algorithm(self):
        start_node = self.start_node
        self.w = Metrics().initializeVisuals(7, self.start_node, self.goal_node, self.size, self.actual_maze, self.agent_maze)
        Metrics().blockage_status_of_children(start_node, self.start_node_actual, self.w)
        self.goal_node.update_g(float("inf"))
        lastClosedList = set()
        while start_node is not self.goal_node:
            passed = 0
            if self.algo_type == 0:
                passed = SolveMaze().forward_A_star(start_node, self.goal_node, self.agent_maze, self.w)
            elif self.algo_type == 1:
                passed = SolveMaze().forward_A_star_in_favor_of_smaller_g(start_node, self.goal_node, self.agent_maze, self.w)
            elif self.algo_type == 2:
                passed = SolveMaze().backward_A_star(start_node, self.goal_node, self.agent_maze, self.w)
            elif self.algo_type == 3:
                passed = SolveMaze().adaptive_A_star(start_node, self.goal_node, lastClosedList, self.w)

            if passed == 0:
                print("I can't reach the target")
                self.w.noPath()
                break

            path, x = Metrics().traverse_path( self.goal_node, start_node, self.algo_type)
            if self.algo_type == 2:
                self.w.pathLine(x)
            else:
                path.reverse()
                self.w.pathLine(path)

            for i in path:
                if i.cost == self.actual_maze[i.x][i.y].cost:
                    if i in self.solvedMaze:
                        if i in self.solvedMaze:
                            del self.solvedMaze[self.solvedMaze.index(i) + 1: len(self.solvedMaze)]
                            continue
                    self.solvedMaze.append(i)
                else:
                    start_node = self.solvedMaze.pop()
                    start_node_actual = self.actual_maze[start_node.x][start_node.y]
                    Metrics().blockage_status_of_children(start_node, start_node_actual, self.w)
                    break
            if self.solvedMaze[len(self.solvedMaze)-1] == self.goal_node:
                print("I reached the goal")
                self.w.finalPath(self.actual_maze, self.solvedMaze)
                break
        mainloop()

