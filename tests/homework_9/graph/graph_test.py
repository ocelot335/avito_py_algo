from homework_9.graph.graph import get_components


def normalize_components(components: list[list[int]]) -> list[list[int]]:
    sorted_inner = [sorted(comp) for comp in components]
    sorted_inner.sort()
    return sorted_inner


def test_empty_graph():
    graph = {}
    result = get_components(graph)
    assert result == []


def test_single_node():
    graph = {1: []}
    expected = [[1]]
    assert normalize_components(get_components(graph)) == normalize_components(
        expected
    )


def test_two_isolated_nodes():
    graph = {1: [], 2: []}
    expected = [[1], [2]]
    assert normalize_components(get_components(graph)) == normalize_components(
        expected
    )


def test_single_connected_component():
    graph = {1: [2], 2: [1, 3], 3: [2]}
    expected = [[1, 2, 3]]
    assert normalize_components(get_components(graph)) == normalize_components(
        expected
    )


def test_multiple_components():
    graph = {1: [2], 2: [1], 3: [4, 5], 4: [3], 5: [3], 6: []}
    expected = [[1, 2], [3, 4, 5], [6]]
    assert normalize_components(get_components(graph)) == normalize_components(
        expected
    )


def test_cycle_graph():
    graph = {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: []}
    expected = [[1, 2, 3], [4]]
    assert normalize_components(get_components(graph)) == normalize_components(
        expected
    )


def test_self_loop():
    graph = {1: [1]}
    expected = [[1]]
    assert normalize_components(get_components(graph)) == normalize_components(
        expected
    )


def test_complex_tree_structure():
    graph = {0: [1, 2, 3, 4], 1: [0], 2: [0], 3: [0], 4: [0]}
    expected = [[0, 1, 2, 3, 4]]
    assert normalize_components(get_components(graph)) == normalize_components(
        expected
    )


def test_duplicate_edges():
    graph = {1: [2, 2, 2], 2: [1]}
    expected = [[1, 2]]
    assert normalize_components(get_components(graph)) == normalize_components(
        expected
    )


def test_disconnected_complex():
    graph = {
        "a": ["b"],
        "b": ["a"],
        "c": [],
        "d": ["e"],
        "e": ["d"],
    }
    expected = [["a", "b"], ["c"], ["d", "e"]]
    assert normalize_components(get_components(graph)) == normalize_components(
        expected
    )
