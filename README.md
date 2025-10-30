Проект: Деревья (BinaryTree, AVLTree, Обходы)

01. Описание
Этот проект реализует и анализирует следующие концепции:
- Класс `BinaryTree` с методами `insert` и `search`.
- Класс `AVLTree`, наследующий `BinaryTree`, с методами балансировки (`left_rotate`, `right_rotate`, `rebalance`) и переопределенной `insert`.
- Функции обхода дерева: BFS (в ширину), DFS Preorder, Inorder, Postorder (в глубину).

02. Структура файлов
- `binary_tree.py`: Реализация класса `BinaryTree`.
- `avl_tree.py`: Реализация класса `AVLTree`.
- `tree_traversals.py`: Функции обхода дерева (`bfs`, `dfs_preorder`, `dfs_inorder`, `dfs_postorder`).
- `test_trees.py`: Скрипт для демонстрации работы деревьев и обходов.
- `README.md`: Описание проекта.

03. Запуск
Для запуска скриптов необходим Python 3.x. Дополнительные зависимости не требуются.

04. Запуск тестов:
1.  **Демонстрация работы BinaryTree, AVLTree и обходов**:
    ```bash
    python test_trees.py
    ```
    Этот скрипт создаст деревья, выполнит вставки, поиски и обходы, выводя результаты.
