from sum import max_sum


def test_example_1_odd_sum():
    assert max_sum([5, 7, 13, 2, 14]) == 36


def test_example_2_single_odd_number():
    assert max_sum([3]) == 0


def test_all_numbers_sum_is_even():
    assert max_sum([2, 4, 6, 8]) == 20


def test_all_numbers_are_odd():
    assert max_sum([1, 3, 5]) == 8
    assert max_sum([3, 5]) == 8


def test_no_odd_numbers():
    assert max_sum([10, 20, 30]) == 60


def test_single_even_number():
    assert max_sum([10]) == 10


def test_empty_list():
    assert max_sum([]) == 0
