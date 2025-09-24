def is_palindrome(n: int) -> bool:
    reverse_n = 0
    copy_n = n

    while n != 0:
        reverse_n *= 10
        reverse_n += n % 10
        n //= 10

    return copy_n == reverse_n


if __name__ == "__main__":
    n = int(input())
    print(is_palindrome(n))
