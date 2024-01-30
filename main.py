class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_max_value(root):
    if root is None:
        return float('-inf')

    while root.right:
        root = root.right

    return root.value


def find_min_value(root):
    if root is None:
        return float('inf')

    while root.left:
        root = root.left

    return root.value


def find_sum_of_values(root):
    if root is None:
        return 0

    return root.value + find_sum_of_values(root.left) + find_sum_of_values(root.right)

# Створення тестового дерева:
#       10
#      /  \
#     5   15
#    / \    \
#   3   7   20


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

# Перевірка результатів:
max_value = find_max_value(root)
min_value = find_min_value(root)
sum_of_values = find_sum_of_values(root)

print(f"Nайбільше значення: {max_value}")
print(f"Nайменше значення: {min_value}")
print(f"Сума всіх значень: {sum_of_values}")
