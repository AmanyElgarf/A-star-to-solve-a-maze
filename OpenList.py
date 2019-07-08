from Node import Node

class openList:
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
                if self.heap[self.parent_pos(child_pos)].g == self.heap[child_pos].g:
                    self.swap(self.parent_pos(child_pos), child_pos)
                    break
            self.swap(self.parent_pos(child_pos), child_pos)
            child_pos = self.parent_pos(child_pos)

    def sink(self, parent_pos):
        while (self.heap[parent_pos].f > self.heap[self.left_child_pos(parent_pos)].f or
               self.heap[self.right_child_pos(parent_pos)].f) \
                and self.is_leaf(parent_pos) is False:
            if self.heap[parent_pos].f > self.heap[self.left_child_pos(parent_pos)].f:
                self.swap(parent_pos, self.left_child_pos(parent_pos))
                parent_pos = self.left_child_pos(parent_pos)
            elif self.heap[parent_pos].f > self.heap[self.right_child_pos(parent_pos)].f:
                self.swap(parent_pos, self.right_child_pos(parent_pos))
                parent_pos = self.right_child_pos(parent_pos)

    def insert(self, element):
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

k = openList()
cell = Node(1, 1)
cell.update_g(6)
cell.update_h(6)

cell1 = Node(1, 2)
cell1.update_g(4)
cell1.update_h(3)


cell2 = Node(1, 3)
cell3 = Node(4, 5)
cell3.update_g(3)
cell3.update_h(4)



k.insert(cell)
k.insert(cell1)
k.insert(cell2)
k.insert(cell3)

k.del_min()
k.print()

