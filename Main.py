import random
from SolveMaze import SolveMaze
from Maze import Maze
from OpenList import OpenList
import math


class Main:
    def __init__(self):
        self.counter = 0
        # type maze where every thing is unblocked
        self.agent_maze = Maze().generate_blank_maze(3)
        self.actual_maze = Maze().generate_actual_maze(3)

    def traverse_path(self, goal_node):
        array = []
        current = goal_node
        while current.x != -1 or current.y != -1:
            array.append([current.x, current.y])
            current = self.agent_maze[current.parent[0], current.parent[1]]
        return array


    def main(self):
        # generating start and goal positions
        array = []
        for x in range(4):
            random.randint(0, 5)
            array.append(random)
        start_x = array[0]
        start_y = array[1]
        goal_x = array[2]
        goal_y = array[3]
        start_node = self.agent_maze[start_x][start_y]
        goal_node = self.agent_maze[goal_x][goal_y]

        while start_x != goal_x or start_y != goal_y:
            self.counter += 1
            start_node.update_g (0)
            start_node.update_search(self.counter)
            start_node.update_parent([-1, -1])
            goal_node.update_g(math.inf)
            goal_node.update_search(self.counter)
            open_list = OpenList()
            open_list.insert(start_node)
            closed_list = set()
            SolveMaze().forward_A_star(open_list, closed_list, start_node, goal_node, self.counter)

            if open_list.is_empty is True:
                print("I can't reach the target")
                return

            path = self.traverse_path(goal_node)




            # AMANY WILL EDIT ON WEDNESDAY
            parent = array[len(array)-1]
            current = parent
            for i in range(len(path) - 2):
                current = path[i]
                # if actual_maze[parent[0], parent[1]].left_child == actual_maze[current[0], current[1]]:
                if self.actual_maze[current[0], current[1]].cost != 1:
                    start_node = self.agent_maze[parent[0], parent[1]]
                    self.agent_maze[current[0], current[1]].cost = math.inf
                    break
                else:
                    parent = current

            if self.agent_maze[parent[0], parent[1]] == goal_node:
                break

        print("I reached the goal")
        return





