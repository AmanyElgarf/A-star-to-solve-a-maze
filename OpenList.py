from Node import Node
import random

class OpenList:
    def __init__(self):
        self.heap = [Node(-9,-9)]
        self.current_size = 0

    def is_empty(self):
        if self.current_size == 0:
            return True
        return False

    def parent_pos(self, child_pos):
        return (int(child_pos/2))

    def left_child_pos(self, parent_pos):
        return int(parent_pos*2)

    def right_child_pos(self, parent_pos):
        return int((parent_pos * 2) + 1)

    def is_leaf(self, pos):
        if pos <= int(self.current_size/2):
            return False
        return True

    def swap(self, parent_pos, child_pos):
        self.heap[parent_pos], self.heap[child_pos] = self.heap[child_pos], self.heap[parent_pos]

    def swim(self, child_pos):
        while self.heap[self.parent_pos(child_pos)].f >= self.heap[child_pos].f and child_pos > 1:
            if self.heap[self.parent_pos(child_pos)].f == self.heap[child_pos].f:
                if self.heap[self.parent_pos(child_pos)].g < self.heap[child_pos].g:
                    self.swap(self.parent_pos(child_pos), child_pos)
                    break
                elif self.heap[self.parent_pos(child_pos)].g > self.heap[child_pos].g:
                    break
                elif self.heap[self.parent_pos(child_pos)].g == self.heap[child_pos].g:
                    intt = random.randint(0, 1)
                    if intt == 0:
                        self.swap(self.parent_pos(child_pos), child_pos)
                    break
            self.swap(self.parent_pos(child_pos), child_pos)
            child_pos = self.parent_pos(child_pos)

    def sink(self, parent_pos):

        while ((self.heap[parent_pos].f > self.heap[self.left_child_pos(parent_pos)].f or
                self.heap[parent_pos].f > self.heap[self.right_child_pos(parent_pos)].f) and self.is_leaf(
            parent_pos) is False):
            k = self.heap[self.left_child_pos(parent_pos)].f > self.heap[self.right_child_pos(parent_pos)].f
            if k is True:
                if self.heap[parent_pos].f > self.heap[self.right_child_pos(parent_pos)].f:
                    self.swap(parent_pos, self.right_child_pos(parent_pos))
                    parent_pos = self.right_child_pos(parent_pos)
                    if self.is_leaf(parent_pos) is True:
                        break
            elif k is False:
                if self.heap[parent_pos].f > self.heap[self.left_child_pos(parent_pos)].f:
                    self.swap(parent_pos, self.left_child_pos(parent_pos))
                    parent_pos = self.left_child_pos(parent_pos)
                if self.is_leaf(parent_pos) is True:
                    break

    def insert(self, element):
        if element  in self.heap:
            for i in self.heap:
                if i.x == element.x and i.y == element.y:
                    self.swim(self.heap.index(i))

        else:
            self.heap.append(element)
            self.current_size += 1
            self.swim(self.current_size)

    def get_min(self):
        return self.heap[1]

    def del_min(self):
        min = self.heap[1]
        self.swap(1, self.current_size)
        self.current_size -= 1
        self.sink(1)
        return min


    def print(self):
        for i in range(1, self.current_size+1):
            print(self.heap[i].f)




k = OpenList()
cell = Node(1, 1)
cell.update_g(6)
cell.update_h(6)

cell1 = Node(1, 2)
cell1.update_g(4)
cell1.update_h(8)


cell2 = Node(1, 3)


cell3 = Node(4, 5)
cell3.update_g(4)
cell3.update_h(5)



k.insert(cell)
k.insert(cell1)
k.insert(cell2)
k.insert(cell3)

cell4 = Node(9, 3)
cell4.update_g(19)


k.insert(cell4)

k.print()


print("amany")
cell4.update_g(2)
k.insert(cell4)




# k.print()

k.print()
#
# print(k.del_min().f)
#
# k.print()
#
# print(k.del_min().f)
#
# print(k.del_min().f)


