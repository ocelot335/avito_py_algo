from typing import List


def max_sum(numbers: List[int]) -> int:
    total = sum(numbers)

    if total % 2 == 0:
        return total
    else:
        odds = [x for x in numbers if x % 2 == 1]  # всегда как миниимум одно
        return total - min(odds)


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    print(max_sum(numbers))
