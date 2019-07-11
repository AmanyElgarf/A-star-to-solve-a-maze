import math


class SolveMaze:
    def forward_A_star(self, open_list, closed_list, goal_node, counter):
        #counter = 0
        while (open_list.is_empty() is False):
            #counter += 1
            #print()
            #print("Forward A* #", counter)


            current = open_list.del_min()
            if current == goal_node:
                closed_list.add(current)
                return
            if current in closed_list: continue
            closed_list.add(current)


            for i in range(0, 4):
                child = current.traverse_children(i)
                if child is None: continue
                if child.cost != 1: continue
                if child in closed_list: continue

                #print("Current child: ")
                #child.print()

                if open_list.contains(child) == False:
                    #print("editing child features")
                    child.update_h(goal_node)
                    child.update_g(float("inf"))
                    #child.search = counter

                    #print("Inserting child to open: ")
                    #child.print()

                if child.g > current.g + child.cost:
                    newG = current.g + child.cost
                    child.update_g(newG)
                    child.parent = [current.x, current.y]
                    #child.print()
                    open_list.insert(child)


    def adaptive_A_star(self, open_list, closed_list, goal_node, lastClosedList, lastGoalCost):
        #counter = 0
        while (open_list.is_empty() is False):
            #counter += 1
            #print()
            #print("Forward A* #", counter)

            current = open_list.del_min()
            if current == goal_node:
                closed_list.add(current)
                return
            if current in closed_list: continue
            closed_list.add(current)


            for i in range(0, 4):
                child = current.traverse_children(i)
                if child is None: continue
                if child.cost != 1: continue
                if child in closed_list: continue
                #print("Current child: ")
                #child.print()

                #initialize children if not yet visited
                if open_list.contains(child) == False:
                    #if first Adaptive Search, no hnew to update
                    if lastClosedList == None and lastGoalCost == float("inf"):
                        child.update_h(goal_node)
                    #otherwise its a successive adaptive search, so you might update child.h if it was previously expanded
                    elif child in lastClosedList:
                        if (child.f < lastGoalCost):
                            child.update_hnew(lastGoalCost)
                    child.update_g(float("inf"))

                    #print("Inserting child to open: ")
                    #child.print()
                if child.g > current.g + child.cost:
                    newG = current.g + child.cost
                    child.update_g(newG)
                    child.parent = [current.x, current.y]
                    #child.print()
                    open_list.insert(child)

