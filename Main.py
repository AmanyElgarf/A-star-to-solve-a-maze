from Maze import Maze
from RepeatedBackward import RepeatedBackward
from Metrics import Metrics
from RepeatedForward import RepeatedForward
from RepeatedAdaptive import RepeatedAdaptive


class Main:
    def __init__(self):
        pass

    def main(self):
        actual_mazes, blankMazes = Maze().readfiftymazes()
        size = 101

        for i in range(50):
            actual_maze = actual_mazes[i]
            start_node_actual, goal_node_actual = Metrics().generate_random_start_and_goal_nodes(
                actual_maze, size)
            for k in range(3):
                if k ==0:
                    agent_maze = blankMazes[i][k]
                    start_node = agent_maze[start_node_actual.x][start_node_actual.y]
                    goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
                    RepeatedForward(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                                     goal_node_actual).repeated_forward()
                if k ==1:
                    agent_maze = blankMazes[i][k]
                    start_node = agent_maze[start_node_actual.x][start_node_actual.y]
                    goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
                    RepeatedBackward(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                                     goal_node_actual).repeated_backward()
                if k ==2:
                    agent_maze = blankMazes[i][k]
                    start_node = agent_maze[start_node_actual.x][start_node_actual.y]
                    goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
                    RepeatedAdaptive(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                                     goal_node_actual).repeated_adaptive()





Main().main()

