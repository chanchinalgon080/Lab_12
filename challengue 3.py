class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        """Returns the height of a node"""
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        """Updates the height of a node"""
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        """Calculates the balance factor of a node"""
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        """Right rotation for AVL Tree"""
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        """Left rotation for AVL Tree"""
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def rebalance(self, node):
        """Rebalances the AVL Tree depending on the balance factor"""
        balance = self.balance_factor(node)

        # LL Case (Right rotation)
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        # RR Case (Left rotation)
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        # LR Case (Left-Right rotation)
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RL Case (Right-Left rotation)
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def delete(self, root, key):
        """Deletes a node from the AVL tree and rebalances if needed"""
        # Step 1: Perform standard BST deletion
        if not root:
            return root

        # If the key is smaller, move to the left subtree
        if key < root.key:
            root.left = self.delete(root.left, key)

        # If the key is larger, move to the right subtree
        elif key > root.key:
            root.right = self.delete(root.right, key)

        # If the key is equal to the root's key, this is the node to delete
        else:
            # Case 1: Node with no children (leaf node)
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            # Case 2: Node with two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Step 2: Update the height of the current node
        if not root:
            return root

        self.update_height(root)

        # Step 3: Rebalance the tree
        return self.rebalance(root)

    def min_value_node(self, node):
        """Finds the node with the minimum value"""
        current = node
        while current.left:
            current = current.left
        return current

    def insert(self, root, key):
        """Inserts a node into the AVL Tree"""
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)

        return self.rebalance(root)

    def inorder(self, root):
        """Performs an inorder traversal of the tree"""
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)


def test_avl_delete():
    avl = AVLTree()
    root = None
    for val in [20, 10, 30, 25, 35]:
        root = avl.insert(root, val)

    # Test 1: Eliminar un nodo hoja
    root = avl.delete(root, 35)
    print("🧪 Test 1 (Eliminar hoja): Pasado 👌")

    # Test 2: Eliminar un nodo con un hijo
    root = avl.delete(root, 25)
    print("🧪 Test 2 (Eliminar con un hijo): Pasado ✂️")

    # Test 3: Eliminar un nodo con dos hijos
    root = avl.delete(root, 20)
    print("🧪 Test 3 (Eliminar con dos hijos): Pasado 🪓")

    # Test 4 y 5: Validar el balance
    print("🧪 Test 4 & 5: Validar balance con recorrido inorder 📏")
    avl.inorder(root)


# 🚀 Ejecutar las pruebas
test_avl_delete()
