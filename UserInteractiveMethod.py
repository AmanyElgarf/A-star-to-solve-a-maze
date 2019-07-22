from Maze import Maze
from RepeatedAlgo import RepeatedAlgo
from Metrics import Metrics
from Visual import Visual


class USerInteractiveMethod:

    def __init__(self):
        self.actual_maze = None
        self.blank_maze = None
        self.size = 0
        self.start_node_actual = None
        self.goal_node_actual = None

    def user(self):
        user_input = None
        while user_input != "stop":
            user_input = input("Enter your the function you you want to perform : ")
            if user_input == "generate actual maze":
                size = input("Enter the size of the maze : ")
                self.size = int(size)
                self.actual_maze = Maze().generate_actual_maze(self.size)
                self.start_node_actual, self.goal_node_actual = Metrics().generate_random_start_and_goal_nodes(
                    self.actual_maze, self.size)
                Visual(7, self.start_node_actual, self.goal_node_actual, self.size).showMaze(self.actual_maze)

            elif user_input == "generate blank maze":
                size = input("Enter the size of the maze : ")
                blank_maze = Maze().generate_blank_maze(self.size)
                start_node_actual, goal_node_actual = Metrics().generate_random_start_and_goal_nodes(
                    blank_maze, int(size))
                Visual(7, start_node_actual, goal_node_actual, int(size)).showMaze(blank_maze)

            elif user_input == "generate corresponding blank maze":
                self.blank_maze = Maze().generate_blank_maze(self.size)
                Visual(7, self.start_node_actual, self.goal_node_actual, self.size).showMaze(self.blank_maze)

            elif user_input == "Perform Repeated forward A* in favor of larger g value":
                agent_maze = Maze().generate_blank_maze(self.size)
                start_node = agent_maze[self.start_node_actual.x][self.start_node_actual.y]
                goal_node = agent_maze[self.goal_node_actual.x][self.goal_node_actual.y]
                RepeatedAlgo(self.size, self.actual_maze, agent_maze, start_node, goal_node, self.start_node_actual,
                             self.goal_node_actual, 0).repeated_algorithm()

            elif user_input == "Perform Repeated forward A* in favor of smaller g value":
                agent_maze = Maze().generate_blank_maze(self.size)
                start_node = agent_maze[self.start_node_actual.x][self.start_node_actual.y]
                goal_node = agent_maze[self.goal_node_actual.x][self.goal_node_actual.y]
                RepeatedAlgo(self.size, self.actual_maze, agent_maze, start_node, goal_node, self.start_node_actual,
                             self.goal_node_actual, 1).repeated_algorithm()

            elif user_input == "Perform Repeated backward A*":
                agent_maze = Maze().generate_blank_maze(self.size)
                start_node = agent_maze[self.start_node_actual.x][self.start_node_actual.y]
                goal_node = agent_maze[self.goal_node_actual.x][self.goal_node_actual.y]
                RepeatedAlgo(self.size, self.actual_maze, agent_maze, start_node, goal_node, self.start_node_actual,
                             self.goal_node_actual, 2).repeated_algorithm()

            elif user_input == "Perform Repeated Adaptive A*":
                agent_maze = Maze().generate_blank_maze(self.size)
                start_node = agent_maze[self.start_node_actual.x][self.start_node_actual.y]
                goal_node = agent_maze[self.goal_node_actual.x][self.goal_node_actual.y]
                RepeatedAlgo(self.size, self.actual_maze, agent_maze, start_node, goal_node, self.start_node_actual,
                             self.goal_node_actual, 3).repeated_algorithm()


USerInteractiveMethod().user()