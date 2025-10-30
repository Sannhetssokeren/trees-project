from collections import deque
from binary_tree import TreeNode, BinaryTree

def bfs(root):
    """
    Обход дерева в ширину (Breadth-First Search).

    :param root: Корень дерева (TreeNode).
    :return: Список значений узлов в порядке обхода.
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

def dfs_preorder(root):
    """
    Прямой обход дерева в глубину (Depth-First Search, Preorder).

    :param root: Корень дерева (TreeNode).
    :return: Список значений узлов в порядке обхода.
    """
    if not root:
        return []
    result = [root.val]
    result += dfs_preorder(root.left)
    result += dfs_preorder(root.right)
    return result

def dfs_inorder(root):
    """
    Симметричный обход дерева в глубину (Depth-First Search, Inorder).

    :param root: Корень дерева (TreeNode).
    :return: Список значений узлов в порядке обхода.
    """
    if not root:
        return []
    result = dfs_inorder(root.left)
    result.append(root.val)
    result += dfs_inorder(root.right)
    return result

def dfs_postorder(root):
    """
    Обратный обход дерева в глубину (Depth-First Search, Postorder).

    :param root: Корень дерева (TreeNode).
    :return: Список значений узлов в порядке обхода.
    """
    if not root:
        return []
    result = dfs_postorder(root.left)
    result += dfs_postorder(root.right)
    result.append(root.val)
    return result

# Пример использования (опционально)
if __name__ == "__main__":
    # Создадим простое дерево вручную для демонстрации
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    print("BFS:", bfs(root))
    print("Preorder:", dfs_preorder(root))
    print("Inorder:", dfs_inorder(root))
    print("Postorder:", dfs_postorder(root))