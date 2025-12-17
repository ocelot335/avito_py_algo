from homework_10.kmp.kmp import prefix_f, kmp


def test_prefix_function_simple():
    assert prefix_f("ababa") == [0, 0, 1, 2, 3]


def test_prefix_function_no_matches():
    assert prefix_f("abcde") == [0, 0, 0, 0, 0]


def test_prefix_function_full_repeat():
    assert prefix_f("aaaa") == [0, 1, 2, 3]


def test_prefix_function_complex():
    assert prefix_f("aabaac") == [0, 1, 0, 1, 2, 0]


def test_kmp_basic_match():
    assert kmp("hello world", "world") == [6]


def test_kmp_start_match():
    assert kmp("hello world", "hello") == [0]


def test_kmp_multiple_matches():
    text = "test match test"
    pattern = "test"
    assert kmp(text, pattern) == [0, 11]


def test_kmp_overlapping_matches():
    assert kmp("ababa", "aba") == [0, 2]


def test_kmp_heavy_overlap():
    assert kmp("aaaaa", "aa") == [0, 1, 2, 3]


def test_kmp_no_match():
    assert kmp("abcdef", "xyz") == []


def test_kmp_pattern_longer_than_text():
    assert kmp("short", "longer_pattern") == []


def test_kmp_empty_pattern():
    assert kmp("anything", "") == []


def test_kmp_empty_text():
    assert kmp("", "abc") == []


def test_kmp_exact_match():
    assert kmp("abc", "abc") == [0]


def test_kmp_partial_match_rollback():
    assert kmp("abababc", "ababc") == [2]
