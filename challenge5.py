from collections import deque  # Importamos deque para realizar un recorrido por niveles (BFS)

# Definimos la clase Node para representar cada nodo del árbol AVL
class Node:
    def __init__(self, key):
        self.key = key          # Valor del nodo
        self.left = None        # Hijo izquierdo
        self.right = None       # Hijo derecho
        self.height = 1         # Altura del nodo (las hojas empiezan con altura 1)

# Definimos la clase AVLTree que contiene todos los métodos del árbol AVL
class AVLTree:

    # Método para insertar un nodo en el árbol y balancearlo
    def insert(self, root, key):
        if not root:
            return Node(key)  # Si el árbol está vacío, creamos un nuevo nodo

        if key < root.key:
            root.left = self.insert(root.left, key)  # Insertamos en el subárbol izquierdo
        else:
            root.right = self.insert(root.right, key)  # Insertamos en el subárbol derecho

        # Actualizamos la altura del nodo actual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Calculamos el factor de balance
        balance = self.get_balance(root)

        # Casos de rotación para mantener el árbol balanceado
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)  # Rotación derecha (Izquierda-Izquierda)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)  # Rotación izquierda (Derecha-Derecha)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)  # Rotación doble izquierda-derecha
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)  # Rotación doble derecha-izquierda
            return self.left_rotate(root)

        return root  # Devolvemos la raíz actualizada

    # Rotación hacia la izquierda
    def left_rotate(self, z):
        y = z.right             # y es el nuevo nodo raíz del subárbol
        T2 = y.left             # T2 será el nuevo hijo derecho de z

        y.left = z              # Rotamos: y pasa a ser raíz y z su hijo izquierdo
        z.right = T2            # T2 se convierte en hijo derecho de z

        # Actualizamos alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # Devolvemos nueva raíz

    # Rotación hacia la derecha
    def right_rotate(self, z):
        y = z.left              # y es el nuevo nodo raíz del subárbol
        T3 = y.right            # T3 será el nuevo hijo izquierdo de z

        y.right = z             # Rotamos: y pasa a ser raíz y z su hijo derecho
        z.left = T3             # T3 se convierte en hijo izquierdo de z

        # Actualizamos alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # Devolvemos nueva raíz

    # Obtiene la altura de un nodo (0 si es None)
    def get_height(self, node):
        return node.height if node else 0

    # Calcula el balance de un nodo
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    # Imprime el recorrido por niveles mostrando clave y altura de cada nodo
    def print_level_order(self, root):
        if not root:
            return  # Si el árbol está vacío, no imprimimos nada

        queue = deque([root])  # Cola para recorrido por niveles

        while queue:
            level_size = len(queue)  # Número de nodos en el nivel actual
            level_nodes = []         # Lista para almacenar los nodos de este nivel

            for _ in range(level_size):
                node = queue.popleft()  # Extraemos el siguiente nodo en la cola
                level_nodes.append(f"{node.key}(h{node.height})")  # Guardamos valor y altura

                # Añadimos hijos a la cola si existen
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            print(", ".join(level_nodes))  # Imprimimos todos los nodos del nivel actual

# Función de prueba para construir un árbol e imprimirlo por niveles
def test_level_order_heights():
    avl = AVLTree()
    root = None

    # Insertamos los valores en el árbol
    for val in [10, 5, 15, 2, 7]:
        root = avl.insert(root, val)

    print("🧪 Test 1–5: Expected output:")
    # Esperado:
    # 10(h3)
    # 5(h2), 15(h1)
    # 2(h1), 7(h1)
    avl.print_level_order(root)

# Ejecutamos la prueba
test_level_order_heights()
