from binary_tree import BinaryTree
from avl_tree import AVLTree
from tree_traversals import bfs, dfs_preorder, dfs_inorder, dfs_postorder

def test_binary_tree():
    print("--- Тестирование BinaryTree ---")
    bt = BinaryTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bt.insert(v)
        print(f"Вставлено: {v}")

    print(f"Поиск 40: {bt.search(40)}") # True
    print(f"Поиск 25: {bt.search(25)}") # False
    print(f"Поиск 80: {bt.search(80)}") # True
    print(f"Поиск 100: {bt.search(100)}") # False
    print("--- Тестирование BinaryTree завершено ---\n")

def test_avl_tree():
    print("--- Тестирование AVLTree ---")
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    for v in values:
        avl.insert(v)
        print(f"Вставлено: {v} (AVL сбалансировано)")
    print(f"Поиск 40: {avl.search(40)}") # True
    print(f"Поиск 35: {avl.search(35)}") # False
    print("--- Тестирование AVLTree завершено ---\n")

def test_traversals():
    print("--- Тестирование обходов (на примере BinaryTree) ---")
    bt = BinaryTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bt.insert(v)

    print("BFS:", bfs(bt.root))
    print("Preorder:", dfs_preorder(bt.root))
    print("Inorder:", dfs_inorder(bt.root)) # Должно быть отсортировано для BST
    print("Postorder:", dfs_postorder(bt.root))
    print("--- Тестирование обходов завершено ---\n")

if __name__ == "__main__":
    test_binary_tree()
    test_avl_tree()
    test_traversals()