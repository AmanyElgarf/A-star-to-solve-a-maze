

class Main:

    def main(self):
        start_node_actual, goal_node_actual = self.generate_random_start_and_goal_nodes()
        self.repeated_backward(start_node_actual)