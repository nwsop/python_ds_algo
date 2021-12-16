class SomeTree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        print(f"adding child: {child.value}")
    
    def remove_child(self, child):
        self.children = [n for n in self.children if n != child]
        print(f"removing child: {child.value}")

    def traverse(self):
        nodes_to_visit = [self]

        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

root = SomeTree(13)
first_child = SomeTree(21)
second_child = SomeTree(11)
first_child_a = SomeTree(33)
second_child_a = SomeTree(31)

root.add_child(first_child)
root.add_child(second_child)
root.traverse()
first_child.add_child(first_child_a)
second_child.add_child(second_child_a)
root.traverse()
root.remove_child(first_child)
root.traverse()
