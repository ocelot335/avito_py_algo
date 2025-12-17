from homework_10.rabin_karp.rabin_karp import rabin_karp


def test_basic_match():
    assert rabin_karp("hello world", "world") == [6]


def test_start_match():
    assert rabin_karp("hello world", "hello") == [0]


def test_multiple_matches():
    assert rabin_karp("banana", "ana") == [1, 3]


def test_overlap():
    # "aaaaa" ищем "aa" -> индексы 0, 1, 2, 3
    assert rabin_karp("aaaaa", "aa") == [0, 1, 2, 3]


def test_no_match():
    assert rabin_karp("abcdef", "xyz") == []


def test_pattern_longer_than_text():
    assert rabin_karp("short", "longer") == []


def test_empty_pattern():
    assert rabin_karp("abc", "") == []


def test_unicode():
    assert rabin_karp("привет мир", "мир") == [7]
