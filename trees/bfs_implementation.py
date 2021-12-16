from collections import deque


class SomeTree:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        print(f"Adding node: {child.value}")
        self.children.append(child)

    def remove_child(self, child):
        print(f"Removing child: {child.value}")
        self.children = [n for n in self.children if n != child]

    def traverse(self):
        print("Traversing")
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


root = SomeTree(12)
fc = SomeTree(21)
sc = SomeTree(11)
fc_a = SomeTree(1)
sc_b = SomeTree(3)
root.add_child(fc)
root.add_child(sc)
fc.add_child(fc_a)
sc.add_child(sc_b)
root.traverse()


def bfs(rn, gv):
    pq = deque()
    initial_path = [rn]
    pq.appendleft(initial_path)

    while pq:
        current_path = pq.pop()
        current_node = current_path[-1]

        if current_node.value == gv:
            return current_path

        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            pq.appendleft(new_path)
    return None

goal = bfs(root, 1)

if goal is None:
    print("Path not found")
else:
    print("Path found")
    for node in goal:
        print(node.value)
        print("---")