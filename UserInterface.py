from Maze import Maze
from RepeatedAlgo import RepeatedAlgo
from Metrics import Metrics
from Visual import Visual
import random


class UserInterface:

    def __init__(self):
        self.actual_maze = Maze().readfiftymazes()[random.randint(0, 50)]
        self.blank_maze = None
        self.size = 101
        self.start_node_actual, self.goal_node_actual = Metrics().generate_random_start_and_goal_nodes(
                    self.actual_maze, self.size)
        self.actual_mazes = Maze().readfiftymazes()

    def user(self):
        user_input = None
        print("0: generate actual maze\n"
              "1: generate blank maze\n"
              "2: generate random maze from the saved mazes\n"
              "3: Perform Repeated forward A* in favor of larger g value\n"
              "4: Perform Repeated forward A* in favor of smaller g value\n"
              "5: Perform Repeated backward A*\n"
              "6: Perform Repeated Adaptive A\n"
              "q: Quit\n")

        while user_input != "q":

            user_input = input("Choose one of the numbers above : ")

            if user_input == "0":
                size = int(input("Enter the size of the maze : "))
                actual_maze = Maze().generate_actual_maze(size)
                start_node_actual, goal_node_actual = Metrics().generate_random_start_and_goal_nodes(
                    actual_maze, size)
                Visual(7, start_node_actual, goal_node_actual, size).showMaze(actual_maze)

            elif user_input == "1":
                size = int(input("Enter the size of the maze : "))
                blank_maze = Maze().generate_blank_maze(size)
                start_node_actual, goal_node_actual = Metrics().generate_random_start_and_goal_nodes(
                    blank_maze, size)
                Visual(7, start_node_actual, goal_node_actual, size).showMaze(blank_maze)

            elif user_input == "2":
                self.actual_maze = self.actual_mazes[random.randint(0, 50)]
                self.start_node_actual, self.goal_node_actual = Metrics().generate_random_start_and_goal_nodes(
                    self.actual_maze, self.size)
                Visual(7, self.start_node_actual, self.goal_node_actual, self.size).showMaze(self.actual_maze)

            elif user_input == "3":
                agent_maze = Maze().generate_blank_maze(self.size)
                start_node = agent_maze[self.start_node_actual.x][self.start_node_actual.y]
                goal_node = agent_maze[self.goal_node_actual.x][self.goal_node_actual.y]
                RepeatedAlgo(self.size, self.actual_maze, agent_maze, start_node, goal_node, self.start_node_actual,
                             self.goal_node_actual, 0).repeated_algorithm()

            elif user_input == "4":
                agent_maze = Maze().generate_blank_maze(self.size)
                start_node = agent_maze[self.start_node_actual.x][self.start_node_actual.y]
                goal_node = agent_maze[self.goal_node_actual.x][self.goal_node_actual.y]
                RepeatedAlgo(self.size, self.actual_maze, agent_maze, start_node, goal_node, self.start_node_actual,
                             self.goal_node_actual, 1).repeated_algorithm()

            elif user_input == "5":
                agent_maze = Maze().generate_blank_maze(self.size)
                start_node = agent_maze[self.start_node_actual.x][self.start_node_actual.y]
                goal_node = agent_maze[self.goal_node_actual.x][self.goal_node_actual.y]
                RepeatedAlgo(self.size, self.actual_maze, agent_maze, start_node, goal_node, self.start_node_actual,
                             self.goal_node_actual, 2).repeated_algorithm()

            elif user_input == "6":
                agent_maze = Maze().generate_blank_maze(self.size)
                start_node = agent_maze[self.start_node_actual.x][self.start_node_actual.y]
                goal_node = agent_maze[self.goal_node_actual.x][self.goal_node_actual.y]
                RepeatedAlgo(self.size, self.actual_maze, agent_maze, start_node, goal_node, self.start_node_actual,
                             self.goal_node_actual, 3).repeated_algorithm()


UserInterface().user()
