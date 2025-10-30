from binary_tree import TreeNode, BinaryTree

class AVLNode(TreeNode):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1 # Высота узла

class AVLTree(BinaryTree):
    def __init__(self):
        # Переопределяем root как AVLNode (хотя в __init__ BinaryTree он будет None)
        # Это важно для корректной работы _insert_recursive и других методов
        super().__init__()
        self.root = None # Явно указываем, что root теперь AVLNode

    def _get_height(self, node):
        """Возвращает высоту узла. 0, если узел None."""
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        """Возвращает баланс узла (разница высот левого и правого поддеревьев)."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _update_height(self, node):
        """Обновляет высоту узла на основе высот его потомков."""
        if node:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _rotate_right(self, y):
        """
        Правый поворот вокруг узла y.
        """
        x = y.left
        T2 = x.right

        # Выполняем поворот
        x.right = y
        y.left = T2

        # Обновляем высоты
        self._update_height(y)
        self._update_height(x)

        # Возвращаем новый корень поддерева
        return x

    def _rotate_left(self, x):
        """
        Левый поворот вокруг узла x.
        """
        y = x.right
        T2 = y.left

        # Выполняем поворот
        y.left = x
        x.right = T2

        # Обновляем высоты
        self._update_height(x)
        self._update_height(y)

        # Возвращаем новый корень поддерева
        return y

    def _rebalance(self, node):
        """
        Балансирует поддерево с корнем в node.
        """
        # Обновляем высоту текущего узла
        self._update_height(node)

        # Получаем баланс
        balance = self._get_balance(node)

        # Если узел лево-тяжелый (баланс > 1)
        if balance > 1:
            # Левый-левый случай -> правый поворот
            if self._get_balance(node.left) >= 0:
                return self._rotate_right(node)
            # Левый-правый случай -> левый поворот на левом потомке, затем правый на текущем
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Если узел право-тяжелый (баланс < -1)
        if balance < -1:
            # Правый-правый случай -> левый поворот
            if self._get_balance(node.right) <= 0:
                return self._rotate_left(node)
            # Правый-левый случай -> правый поворот на правом потомке, затем левый на текущем
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        # Если дерево сбалансировано
        return node

    def _insert_recursive(self, node, key):
        """
        Переопределяем рекурсивную вставку для AVL-дерева.
        """
        # Выполняем стандартную вставку BST
        if not node:
            return AVLNode(key)

        if key < node.val:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.val:
            node.right = self._insert_recursive(node.right, key)
        else: # Ключи равны, игнорируем дубликаты
            return node

        # Балансируем поддерево
        return self._rebalance(node)

    # Переопределяем insert, чтобы root был AVLNode
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    # Метод search наследуется из BinaryTree, он не зависит от баланса