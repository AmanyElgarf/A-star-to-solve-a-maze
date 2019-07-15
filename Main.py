from Maze import Maze
from RepeatedAlgo import RepeatedAlgo
from Metrics import Metrics


class Main:
    def main(self):
        actual_mazes = Maze().readfiftymazes()
        size = 101
        for i in range(50):
            actual_maze = actual_mazes[i]
            start_node_actual, goal_node_actual = Metrics().generate_random_start_and_goal_nodes(
            actual_maze, size)

            agent_maze = Maze().generate_blank_maze(size)
            start_node = agent_maze[start_node_actual.x][start_node_actual.y]
            goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
            RepeatedAlgo(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                             goal_node_actual, 0).repeated_algorithm()

            agent_maze = Maze().generate_blank_maze(size)
            start_node = agent_maze[start_node_actual.x][start_node_actual.y]
            goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
            RepeatedAlgo(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                            goal_node_actual, 1).repeated_algorithm()

            agent_maze = Maze().generate_blank_maze(size)
            start_node = agent_maze[start_node_actual.x][start_node_actual.y]
            goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
            RepeatedAlgo(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                             goal_node_actual, 2).repeated_algorithm()

            agent_maze = Maze().generate_blank_maze(size)
            start_node = agent_maze[start_node_actual.x][start_node_actual.y]
            goal_node = agent_maze[goal_node_actual.x][goal_node_actual.y]
            RepeatedAlgo(size, actual_maze, agent_maze, start_node, goal_node, start_node_actual,
                             goal_node_actual, 3).repeated_algorithm()

Main().main()

