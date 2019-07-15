import random
from SolveMaze import SolveMaze
from Maze import Maze
from Visual import Visual
from tkinter import *
from Metrics import Metrics

class RepeatedAdaptive:
    def __init__(self, size):
        self.agent_maze = Maze().generate_blank_maze(size)
        self.actual_maze = Maze().generate_actual_maze(size)
        self.size = size
        self.solvedMaze = []
        self.start_node = None
        self.goal_node = None
        self.w = None

    def generate_random_start_and_goal_nodes(self):
        while True:
            start_node_actual = self.actual_maze[random.randint(0, self.size-1)][random.randint(0, self.size-1)]
            goal_node_actual = self.actual_maze[random.randint(0, self.size-1)][random.randint(0, self.size-1)]
            if (start_node_actual.cost == 1) & (goal_node_actual.cost == 1) & (start_node_actual != goal_node_actual):
                break
        self.start_node = self.agent_maze[start_node_actual.x][start_node_actual.y]
        self.goal_node = self.agent_maze[goal_node_actual.x][goal_node_actual.y]
        return start_node_actual, goal_node_actual



    def initializeVisuals(self, distance):
        self.w = Visual(distance, self.start_node, self.goal_node, self.size)
        self.w.showMaze(self.actual_maze)
        self.w.showMaze(self.agent_maze)


    def repeated_adaptive(self, start_node_actual, goal_node_actual):
        start_node = self.start_node
        self.initializeVisuals(7)
        Metrics().blockage_status_of_children(start_node, start_node_actual, self.w)
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

    def main(self):
        start_node_actual, goal_node_actual = self.generate_random_start_and_goal_nodes()
        # print(start_node_actual.x, start_node_actual.y, goal_node_actual.x, goal_node_actual.y)
        self.repeated_adaptive(start_node_actual, goal_node_actual)


RepeatedAdaptive(101).main()