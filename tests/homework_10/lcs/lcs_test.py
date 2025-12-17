from homework_10.lcs.lcs import lcs


def test_basic():
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    assert lcs(s1, s2) == "GTAB"


def test_different_lengths():
    s1 = "A"
    s2 = "ABC"
    assert lcs(s1, s2) == "A"

    s1 = "ABC"
    s2 = "A"
    assert lcs(s1, s2) == "A"


def test_empty():
    assert lcs("", "abc") == ""
    assert lcs("abc", "") == ""


def test_no_common():
    assert lcs("abc", "xyz") == ""


def test_full_match():
    assert lcs("test", "test") == "test"


def test_complex_gaps():
    # A...B...C...D
    s1 = "AxBxCxD"
    s2 = "ABCD"
    assert lcs(s1, s2) == "ABCD"


def test_order_matters():
    res = lcs("ab", "ba")
    assert res in ["a", "b"]
    assert len(res) == 1
