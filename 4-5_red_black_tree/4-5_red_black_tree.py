class Node:
    def __init__(self, key, value, color, parent=None):
        self.key = key
        self.value = value
        self.color = color  # True - red, False - black
        self.left = None
        self.right = None
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, None, False) 
        self.root = self.NIL

    def insert(self, key, value):
        new_node = Node(key, value, True, None)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:  # tree is empty
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = True
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color is True:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color is True:  # Case 1
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:  # Case 2
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = False  # Case 3
                    node.parent.parent.color = True
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color is True:  # Case 1
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:  # Case 2
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = False  # Case 3
                    node.parent.parent.color = True
                    self.left_rotate(node.parent.parent)
        self.root.color = False

    def left_rotate(self, node):
        right = node.right
        node.right = right.left
        if right.left != self.NIL:
            right.left.parent = node
        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    def right_rotate(self, node):
        left = node.left
        node.left = left.right
        if left.right != self.NIL:
            left.right.parent = node
        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left

    def search(self, key):
        current = self.root
        while current != self.NIL:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node != self.NIL:
            self.inorder(node.left, result)
            result.append((node.key, node.value))
            self.inorder(node.right, result)
        return result

    def display(self, node=None, indent="", last=True):
        if node is None:
            node = self.root

        if node != self.NIL:
            print(indent, "`- " if last else "|- ", f"{node.key} ({'R' if node.color else 'B'})", sep="")
            indent += "   " if last else "|  "
            self.display(node.left, indent, False)
            self.display(node.right, indent, True)


# Пример использования
if __name__ == "__main__":
    tree = RedBlackTree()
    tree.insert(10, "val 10")
    tree.insert(20, "val 20")
    tree.insert(15, "val 15")
    tree.insert(5, "val 5")
    tree.insert(1, "val 1")
    tree.insert(100, "val 100")

    print("Inorder traversal:", tree.inorder(tree.root))
    print("\nTree structure:")
    tree.display()
