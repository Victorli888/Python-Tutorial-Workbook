import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Create the tree nodes


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
# Build the tree structure
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node8
node3.left = node6
node3.right = node7
node6.left = node9
node6.right = node10


def inOrderTraversal(root):
    ans = []

    def inorder(root):
        if not root:
            return None
        inorder(root.left)
        ans.append(root.val)
        inorder(root.right)

    inorder(root)
    return ans


def preOrderTraversal(root):
    ans = []

    def preOrder(root):
        # Base Case
        if not root:
            return None
        # Recursive Logic
        ans.append(root.val)
        preOrder(root.left)
        preOrder(root.right)

    preOrder(root)
    return ans


def postOrderTraversal(root):
    ans = []

    def postOrder(root):
        # Base case
        if not root:
            return None

        # Recursion
        postOrder(root.left)
        postOrder(root.right)
        ans.append(root.val)

    postOrder(root)
    return ans


def inOrderIterative(root):
    """
    Using a call stack we will store nodes in a stack so we don't lose them while traversing and call them when we need
    :param root:
    :return:
    """
    ans = []
    node_stack = []
    curr_node = root

    while curr_node or len(node_stack) > 0:
        while curr_node:
            node_stack.append(curr_node)
            curr_node = curr_node.left
        curr_node = node_stack.pop()
        ans.append(curr_node.val)
        curr_node = curr_node.right
    return ans

def levelOrderTraversal(root):
    ans = []
    myQueue = collections.deque()
    myQueue.append(root)

    while len(myQueue) > 0:
        currNode = myQueue.popleft()
        ans.append(currNode.val)
        if currNode.left:
            myQueue.append(currNode.left)
        if currNode.right:
            myQueue.append(currNode.right)
    return ans




# DFS in a nutshell
print(inOrderTraversal(node1))
print(preOrderTraversal(node1))
print(postOrderTraversal(node1))
print(inOrderIterative(node1))
print(levelOrderTraversal(node1))