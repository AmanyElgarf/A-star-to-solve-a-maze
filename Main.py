from Maze import Maze
from RepeatedBackward import RepeatedBackward
from Metrics import Metrics
from RepeatedForward import RepeatedForward
from RepeatedAdaptive import RepeatedAdaptive
from RepeatedForwardInFavorOfSmallerG import RepeatedForwardInFavorOfSmallerG


class Main:
    def main(self):
        actual_mazes = Maze().readfiftymazes()
        size = 101
        blankMazes = Maze().fifty_blank_mazes()
        for i in range(50):
            actual_maze = actual_mazes[i]
            start_node_actual, goal_node_actual = Metrics().generate_random_start_and_goal_nodes(
                actual_maze, size)
            for k in range(4):
                if k == 0:
                    agent_maze = blankMazes[k][i]
                    start_node = agent_maze[start_node_actual.x][start_node_actual.y]
                    goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
                    RepeatedForward(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                                     goal_node_actual).repeated_forward()
                if k == 1:
                    agent_maze = blankMazes[k][i]
                    start_node = agent_maze[start_node_actual.x][start_node_actual.y]
                    goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
                    RepeatedForwardInFavorOfSmallerG(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                                    goal_node_actual).repeated_forward_in_favor_of_smaller_g()
                if k == 2:
                    agent_maze = blankMazes[k][i]
                    start_node = agent_maze[start_node_actual.x][start_node_actual.y]
                    goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
                    RepeatedBackward(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                                     goal_node_actual).repeated_backward()
                if k == 3:
                    agent_maze = blankMazes[k][i]
                    start_node = agent_maze[start_node_actual.x][start_node_actual.y]
                    goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
                    RepeatedAdaptive(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                                     goal_node_actual).repeated_adaptive()


Main().main()

