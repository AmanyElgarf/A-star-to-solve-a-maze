import random
from Visual import Visual


class Metrics:
    def traverse_path(self, goal_node, start_node):
        path = [goal_node]
        currentNode = goal_node
        while currentNode is not start_node:
            currentNode = currentNode.parent
            path.append(currentNode)
        return path

    def generate_random_start_and_goal_nodes(self, actual_maze, size):
        while True:
            start_node_actual = actual_maze[random.randint(0, size-1)][random.randint(0, size-1)]
            goal_node_actual = actual_maze[random.randint(0, size-1)][random.randint(0, size-1)]
            if (start_node_actual.cost == 1) & (goal_node_actual.cost == 1) & (start_node_actual != goal_node_actual):
                break
        return start_node_actual, goal_node_actual

    def blockage_status_of_children(self, start_node, start_node_actual, w):
        if start_node_actual.right_child is not None:
            start_node.right_child.cost = start_node_actual.right_child.cost
            w.blocked(start_node.right_child)
        if start_node_actual.left_child is not None:
            start_node.left_child.cost = start_node_actual.left_child.cost
            w.blocked(start_node.left_child)
        if start_node_actual.top_child is not None:
            start_node.top_child.cost = start_node_actual.top_child.cost
            w.blocked(start_node.top_child)
        if start_node_actual.down_child is not None:
            start_node.down_child.cost = start_node_actual.down_child.cost
            w.blocked(start_node.down_child)
        w.master.update()

    def initializeVisuals(self, distance, start_node, goal_node, size, actual_maze, agent_maze):
        w = Visual(distance, start_node, goal_node, size)
        w.showMaze(actual_maze)
        w.showMaze(agent_maze)
        return w
