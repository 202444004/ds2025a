# BST
class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


def pre_order(node):
    if node is None:
        return
    print(node.data, end="->")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end="->")
    in_order(node.right)


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end="->")


def search(find_number):
    current = root
    while True:
        if find_number == current.data:
            return True
        elif find_number < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
                return False
            current = current.right


def insert(root, value):
    node = TreeNode()
    node.data = value

    if root is None:
        return node

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left  # 이동
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right  # 이동
    return root

def delete(node, value):
    if node is None:
        return None

    if value < node.data:
        node.left = delete(node.left, value)

    elif value > node.data:
        node.right = delete(node.right, value)

    else:
        #자식이 한 개인 노드 삭제
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        #자식이 두 개인 노드 삭제
        #min_larger_node = node.right
        max_smaller_node = node.left
        while max_smaller_node.rigth:
            max_smaller_node = max_smaller_node.rigth
        node.data = max_smaller_node.data
        node.left = delete(node.left, max_smaller_node.data)
    return node


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 100, 7, 13]
    root = None

    for number in numbers:
        root = insert(root, number)

    print('BST 구성 완료')
    pre_order(root)
    print()
    in_order(root)
    print()
    post_order(root)
    print()
    find_number = int(input("찾는 수는? "))
    if search(find_number):
        print(f"{find_number}을(를) 찾았습니다")
    else:
        print(f"{find_number}이(가) 존재하지 않습니다")

    delete_number = int(input("제거할 수는? "))
    root = delete(root, delete_number)