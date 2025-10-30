class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Вставляет узел с заданным ключом в дерево.

        :param key: Ключ для вставки.
        """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """
        Вспомогательная рекурсивная функция для вставки.
        """
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else: # key >= node.val
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """
        Ищет узел с заданным ключом в дереве.

        :param key: Ключ для поиска.
        :return: True, если узел найден, иначе False.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """
        Вспомогательная рекурсивная функция для поиска.
        """
        if node is None or node.val == key:
            return node is not None

        if key < node.val:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)