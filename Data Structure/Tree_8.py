class TreeNode:
    # __init__(self, data):
    # We initialize the TreeNode with a data value, which represents the content of the node.
    # We create an empty list, self.children, to hold the child nodes of this TreeNode.
    # We set self.parent to None initially, indicating that this node has no parent.

    def __init__(self, data):  # self is just like this in constructor of JavaScript's class
        self.data = data
        self.children = []  # It will be a list
        self.parent = None

    # get_level(self):
    # This method calculates the level or depth of the current node within the tree.
    # It iterates through the parent nodes, incrementing the level until it reaches the root.

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    # print_tree(self):
    # This method prints the tree structure starting from the current node.
    # It uses indentation to represent the level of each node, with "|" and "__" to
    # create a visual hierarchy.

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    # add_child(self, child):
    # This method is used to add a child node to the current node.
    # It assigns the current node (self) as the parent of the child node and
    # appends the child to the list of children of the current node.

    def add_child(self, child):  # child node addition in our tree
        child.parent = self
        self.children.append(child)


# build_product_tree():

# This function creates a sample tree structure for product categories.
# It initializes a root node and then adds child nodes for electronics categories
# such as laptops, cell phones, and TVs.
# Finally, it calls root.print_tree() to display the entire tree structure.


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()


# if __name__ == '__main__'::
# This conditional statement checks whether the script is being run as the main program.
# It is used to ensure that the build_product_tree() function is executed when the script is run directly
# and not when it is imported as a module.

if __name__ == "__main__":  # Main method mainly use for call the method or function
    build_product_tree()
