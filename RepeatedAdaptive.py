from SolveMaze import SolveMaze
from Maze import Maze
from tkinter import *
from Metrics import Metrics


class RepeatedAdaptive:
    def __init__(self, size, actual_maze, agent_maze, start_node, goal_node, start_node_actual, goal_node_actual):
        self.agent_maze = agent_maze
        self.actual_maze = actual_maze
        self.size = size
        self.solvedMaze = []
        self.start_node = start_node
        self.goal_node = goal_node
        self.start_node_actual = start_node_actual
        self.goal_node_actual = goal_node_actual
        self.w = None

    def repeated_adaptive(self):
        start_node = self.start_node
        self.w = Metrics().initializeVisuals(7, self.start_node, self.goal_node, self.size, self.actual_maze, self.agent_maze)
        Metrics().blockage_status_of_children(start_node, self.start_node_actual, self.w)
        self.goal_node.update_g(float("inf"))
        lastClosedList = set()
        while start_node is not self.goal_node:
            if SolveMaze().adaptive_A_star(start_node, self.goal_node, lastClosedList, self.w) == 0:
                print("I can't reach the target")
                self.w.noPath()
                break
            path = Metrics().traverse_path(self.goal_node, start_node)
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

#
# size = 20
# actual_maze = Maze().generate_actual_maze(size)
# agent_maze = Maze().generate_blank_maze(size)
# start_node_actual, goal_node_actual, start_node, goal_node = Metrics().generate_random_start_and_goal_nodes(
#             actual_maze, agent_maze, size)
# RepeatedAdaptive(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual, goal_node_actual).repeated_adaptive()