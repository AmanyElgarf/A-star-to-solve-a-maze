import random
from SolveMaze import SolveMaze
from Maze import Maze
from Visual import Visual
from tkinter import *

class Main:
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

    def traverse_path(self, goal_node, start_node):
        path = [goal_node]
        currentNode = goal_node
        while currentNode is not start_node:
            currentNode = currentNode.parent
            path.append(currentNode)
        return path

    def blockage_status_of_children(self, start_node, start_node_actual):
        if start_node_actual.right_child is not None:
            start_node.right_child.cost = start_node_actual.right_child.cost
            self.w.blocked(start_node.right_child)
        if start_node_actual.left_child is not None:
            start_node.left_child.cost = start_node_actual.left_child.cost
            self.w.blocked(start_node.left_child)
        if start_node_actual.top_child is not None:
            start_node.top_child.cost = start_node_actual.top_child.cost
            self.w.blocked(start_node.top_child)
        if start_node_actual.down_child is not None:
            start_node.down_child.cost = start_node_actual.down_child.cost
            self.w.blocked(start_node.down_child)

    def initializeVisuals(self, distance):
        master = Tk()
        canvas_width = self.size * distance + distance * 2
        canvas_height = self.size * distance + distance * 2
        canvas = Canvas(master, width=canvas_width, height=canvas_height)
        canvas.pack()
        self.w = Visual(canvas, master, distance)
        self.w.showMaze(self.actual_maze)
        self.w.start(self.start_node)
        self.w.goal(self.goal_node)
        self.w.showMaze(self.agent_maze)
        self.w.start(self.start_node)
        self.w.goal(self.goal_node)

    def repeated_forward(self, start_node_actual):
        start_node = self.start_node

        self.initializeVisuals(6)

        self.blockage_status_of_children(start_node, start_node_actual)


        while start_node is not self.goal_node:
            start_node.update_g(0)
            start_node.update_h(self.goal_node)
            self.goal_node.update_g(float("inf"))
            if SolveMaze().forward_A_star(start_node, self.goal_node, self.agent_maze, self.w) == "I can't reach the target":
                print("I can't reach the target")
                self.w.noPath()
                break
            path = self.traverse_path(self.goal_node, start_node)
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
                    self.blockage_status_of_children(start_node, start_node_actual)
                    break
            if self.solvedMaze[len(self.solvedMaze)-1] == self.goal_node:
                print("I reached the goal")
                self.w.finalPath(self.actual_maze, self.solvedMaze)
                break
        mainloop()

    def main(self):
        start_node_actual, goal_node_actual = self.generate_random_start_and_goal_nodes()
        # print(start_node_actual.x, start_node_actual.y, goal_node_actual.x, goal_node_actual.y)
        self.repeated_forward(start_node_actual)


# Main(101).main()