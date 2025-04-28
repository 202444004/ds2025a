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
        print(node.data, end="")

def insert(root, value):


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 100, 7, 13]
    root = None

    node = TreeNode()
    node.data = numbers[0] #10
    root = node

    for number in numbers:
        root = insert(root, number)
    print('BST 구성완료')
    pre_order(root)

    find_number = int(input())
    current = root
    while True:
        if find_number == current.data:
            print(f"{find_number}을(를) 찾았습니다")
            break
        elif find_number < current.data:
            if current.left is None:
                print(f"{find_number}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_number}이(가) 존재하지 않습니다")
                break
            current = current.right