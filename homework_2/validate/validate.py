from typing import List
from stack_vs_queue.stack import Stack


def validate(pushed: List[int], popped: List[int]) -> bool:
    stack = Stack()
    id_in_popped = 0
    for pushed_el in pushed:
        stack.push(pushed_el)
        while (
            id_in_popped < len(popped) and stack.top() == popped[id_in_popped]
        ):
            stack.pop()
            id_in_popped += 1
    return len(stack) == 0


if __name__ == "__main__":
    pushed = [int(x) for x in input().split()]
    popped = [int(x) for x in input().split()]
    print(validate(pushed=pushed, popped=popped))
