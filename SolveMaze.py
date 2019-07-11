
class SolveMaze:
    def forward_A_star(self, open_list, closed_list, goal_node, counter):
        counter = 0

        while open_list.is_empty() is False:
            counter += 1
            print()
            print("Forward A* #", counter)


            current = open_list.del_min()
            if current == goal_node: return
            if current in closed_list: continue
            closed_list.add(current)


            for i in range(0, 4):
                child = current.traverse_children(i)
                if child is None: continue

                print("Current child: ")
                child.print()

                if (open_list.contains(child) == False) or (child not in closed_list):
                    print("editing child features")

                    child.update_g(float("inf"))
                    child.update_h(goal_node)
                #    child.search = counter


                if child not in closed_list:
                    if (child.cost != 1):
                        print("CHILD COST NOT 1")
                        closed_list.add(child)
                        continue

                    print("Inserting child to open: ")
                    child.print()

                    if child.g > current.g + child.cost:
                        newG = current.g + child.cost
                        child.update_g(newG)
                        child.parent = [current.x, current.y]
                        child.print()
                        open_list.insert(child)

