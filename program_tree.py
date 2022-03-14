class Program_Tree:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.function = None

    def add_child(self, name):
        self.children.append(Program_Tree(name))
        return self

    def get_depth(self):
        if len(self.children) == 0:
            return 0
        else:
            return 1 + max([child.get_depth() for child in self.children])

    def get_level(self, level):
        if level == 0:
            return [self]
        else:
            return [child.get_level(level - 1) for child in self.children]

    def print_tree(self):
        print(self.name)
        for child in self.children:
            child.print_tree()

    def do_function(self):
        if self.function is None:
            return 1 
        else:
            self.function([child.do_function() for child in self.children])

        