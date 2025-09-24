from prime import get_count_of_primes


def test_example_1_from_task():
    assert get_count_of_primes(10) == 4


def test_example_2_from_task():
    assert get_count_of_primes(1) == 0


def test_boundary_conditions_around_two():
    assert get_count_of_primes(0) == 0
    assert get_count_of_primes(2) == 0


def test_negative_input():
    assert get_count_of_primes(-10) == 0


def test_first_prime_number_case():
    assert get_count_of_primes(3) == 1


def test_when_limit_is_prime():
    assert get_count_of_primes(13) == 5


def test_when_limit_is_square_of_prime():
    assert get_count_of_primes(25) == 9


def test_larger_number():
    assert get_count_of_primes(100) == 25
