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

    def balance_factor(self, node):
        """Calculates the balance factor of a node"""
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        """Updates the height of a node"""
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def is_avl_balanced(self, root):
        """Checks if the tree is balanced according to AVL rules"""
        # Base case: If the node is None, it's balanced
        if not root:
            return True

        # Check the balance factor of the current node
        balance = self.balance_factor(root)

        # If the balance factor is outside the range [-1, 1], it's not AVL-balanced
        if abs(balance) > 1:
            return False

        # Recursively check the left and right subtrees
        left_balanced = self.is_avl_balanced(root.left)
        right_balanced = self.is_avl_balanced(root.right)

        # Ensure both left and right subtrees are balanced
        if not left_balanced or not right_balanced:
            return False

        # If everything is fine, update the current node's height and return True
        self.update_height(root)
        return True

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

    def rebalance(self, node):
        """Rebalances the tree if necessary"""
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

# 🧪 Test cases


def test_is_avl_balanced():
    avl = AVLTree()
    root = None
    for val in [20, 10, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1:", avl.is_avl_balanced(root) == True)  # ✅

    # Simulate imbalance manually
    unbalanced = Node(10)
    unbalanced.right = Node(20)
    unbalanced.right.right = Node(30)
    print("🧪 Test 2:", avl.is_avl_balanced(unbalanced) == False)  # ⚠️

    print("🧪 Test 3:", avl.is_avl_balanced(None) == True)  # 🌱
    # More cases in complex structures...


# 🚀 Run tests
test_is_avl_balanced()
