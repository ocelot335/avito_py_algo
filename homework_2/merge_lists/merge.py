class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_lists(
    first_list: LinkedListNode, second_list: LinkedListNode
) -> LinkedListNode:
    if not first_list:
        return second_list
    if not second_list:
        return first_list

    new_head = None
    if first_list.value > second_list.value:
        first_list, second_list = second_list, first_list

    new_head = first_list
    current_node = new_head
    first_list = first_list.next
    while first_list is not None and second_list is not None:
        if first_list.value <= second_list.value:
            current_node.next = first_list
            current_node = first_list
            first_list = first_list.next
        else:
            current_node.next = second_list
            current_node = second_list
            second_list = second_list.next
    if first_list is not None:
        current_node.next = first_list
    if second_list is not None:
        current_node.next = second_list
    return new_head


def merge_lists_dummy(
    first_list: LinkedListNode, second_list: LinkedListNode
) -> LinkedListNode:
    new_head = LinkedListNode(0)  # dummy

    current_node = new_head
    while first_list is not None and second_list is not None:
        if first_list.value <= second_list.value:
            current_node.next = first_list
            current_node = first_list
            first_list = first_list.next
        else:
            current_node.next = second_list
            current_node = second_list
            second_list = second_list.next
    if first_list is not None:
        current_node.next = first_list
    if second_list is not None:
        current_node.next = second_list
    return new_head.next
