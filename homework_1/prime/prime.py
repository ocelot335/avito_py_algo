def get_count_of_primes(n: int) -> int:
    sieve = [True] * n  # решето Эратосфена
    if n <= 2:
        return 0
    sieve[0] = False
    sieve[1] = False

    for num in range(2, int(n**0.5) + 1):
        if sieve[num]:
            for not_prime in range(
                num * num, n, num
            ):  # с num*num потому что остальные уже вычеркнули
                sieve[not_prime] = False

    return sum(sieve)


if __name__ == "__main__":
    n = int(input())
    print(get_count_of_primes(n))
