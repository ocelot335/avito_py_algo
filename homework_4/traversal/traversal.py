from .bst import BST, BSTNode
from homework_2.stack_vs_queue.stack import Stack


def pre_order(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer

    def incapsulated_node_traverse(node: BSTNode):
        if node is None:
            return
        answer.append(node.value)
        incapsulated_node_traverse(node.left)
        incapsulated_node_traverse(node.right)

    incapsulated_node_traverse(tree.root)
    return answer


def pre_order_wo_recursion(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer
    stack = Stack()
    stack.push((0, tree.root))
    while len(stack) != 0:
        mode, node = stack.pop()
        if node is None:
            continue
        if mode == 1:
            answer.append(node.value)
        else:
            stack.push((0, node.right))
            stack.push((0, node.left))
            stack.push((1, node))
    return answer


def post_order(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer

    def incapsulated_node_traverse(node: BSTNode):
        if node is None:
            return
        incapsulated_node_traverse(node.left)
        incapsulated_node_traverse(node.right)
        answer.append(node.value)

    incapsulated_node_traverse(tree.root)
    return answer


def post_order_wo_recursion(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer
    stack = Stack()
    stack.push((0, tree.root))
    while len(stack) != 0:
        mode, node = stack.pop()
        if node is None:
            continue
        if mode == 1:
            answer.append(node.value)
        else:
            stack.push((1, node))
            stack.push((0, node.right))
            stack.push((0, node.left))
    return answer


def in_order(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer

    def incapsulated_node_traverse(node: BSTNode):
        if node is None:
            return
        incapsulated_node_traverse(node.left)
        answer.append(node.value)
        incapsulated_node_traverse(node.right)

    incapsulated_node_traverse(tree.root)
    return answer


def in_order_wo_recursion(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer
    stack = Stack()
    stack.push((0, tree.root))
    while len(stack) != 0:
        mode, node = stack.pop()
        if node is None:
            continue
        if mode == 1:
            answer.append(node.value)
        else:
            stack.push((0, node.right))
            stack.push((1, node))
            stack.push((0, node.left))
    return answer


def reverse_pre_order(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer

    def incapsulated_node_traverse(node: BSTNode):
        if node is None:
            return
        answer.append(node.value)
        incapsulated_node_traverse(node.right)
        incapsulated_node_traverse(node.left)

    incapsulated_node_traverse(tree.root)
    return answer


def reverse_pre_order_wo_recursion(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer
    stack = Stack()
    stack.push((0, tree.root))
    while len(stack) != 0:
        mode, node = stack.pop()
        if node is None:
            continue
        if mode == 1:
            answer.append(node.value)
        else:
            stack.push((0, node.left))
            stack.push((0, node.right))
            stack.push((1, node))
    return answer


def reverse_post_order(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer

    def incapsulated_node_traverse(node: BSTNode):
        if node is None:
            return
        incapsulated_node_traverse(node.right)
        incapsulated_node_traverse(node.left)
        answer.append(node.value)

    incapsulated_node_traverse(tree.root)
    return answer


def reverse_post_order_wo_recursion(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer
    stack = Stack()
    stack.push((0, tree.root))
    while len(stack) != 0:
        mode, node = stack.pop()
        if node is None:
            continue
        if mode == 1:
            answer.append(node.value)
        else:
            stack.push((1, node))
            stack.push((0, node.left))
            stack.push((0, node.right))
    return answer


def reverse_in_order(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer

    def incapsulated_node_traverse(node: BSTNode):
        if node is None:
            return
        incapsulated_node_traverse(node.right)
        answer.append(node.value)
        incapsulated_node_traverse(node.left)

    incapsulated_node_traverse(tree.root)
    return answer


def reverse_in_order_wo_recursion(tree: BST) -> list:
    answer = []
    if tree is None:
        return answer
    stack = Stack()
    stack.push((0, tree.root))
    while len(stack) != 0:
        mode, node = stack.pop()
        if node is None:
            continue
        if mode == 1:
            answer.append(node.value)
        else:
            stack.push((0, node.left))
            stack.push((1, node))
            stack.push((0, node.right))
    return answer
