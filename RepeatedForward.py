from SolveMaze import SolveMaze
from Maze import Maze
from Visual import Visual
from tkinter import *
from Metrics import Metrics


class RepeatedForward:
    def __init__(self, size):
        self.agent_maze = Maze().generate_blank_maze(size)
        self.actual_maze = Maze().generate_actual_maze(size)
        self.size = size
        self.solvedMaze = []
        self.start_node = None
        self.goal_node = None
        self.w = None

    def initializeVisuals(self, distance):
        self.w = Visual(distance, self.start_node, self.goal_node, self.size)
        self.w.showMaze(self.actual_maze)
        self.w.showMaze(self.agent_maze)

    def repeated_forward(self, start_node_actual, goal_node_actual, start_nodee, goal_node):
        start_node = start_nodee
        self.initializeVisuals(7)

        Metrics().blockage_status_of_children(start_node, start_node_actual, self.w)

        while start_node is not goal_node:
            if SolveMaze().forward_A_star(start_node, goal_node, self.agent_maze, self.w) == 0:
                print("I can't reach the target")
                self.w.noPath()
                break
            path = Metrics().traverse_path(goal_node, start_node)
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
            if self.solvedMaze[len(self.solvedMaze)-1] == goal_node:
                print("I reached the goal")
                self.w.finalPath(self.actual_maze, self.solvedMaze)
                break
        mainloop()

    def main(self):
        start_node_actual, goal_node_actual, start_node, goal_node = Metrics().generate_random_start_and_goal_nodes(self.actual_maze, self.agent_maze,  self.size)
        self.start_node = start_node
        self.goal_node = goal_node
        self.repeated_forward(start_node_actual, goal_node_actual, start_node, goal_node)


RepeatedForward(20).main()