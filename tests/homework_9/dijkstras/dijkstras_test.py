from homework_9.dijkstras.dijkstras import dijkstras


def test_diamond_graph():
    graph = {
        "A": [("B", 1), ("C", 10)],
        "B": [("C", 2)],
        "C": [],
    }
    result = dijkstras(graph, "A")
    assert result["C"] == 3
    assert result["B"] == 1


def test_complex_graph_priority():
    graph = {
        "Start": [("A", 5), ("B", 2)],
        "A": [("End", 1)],
        "B": [("A", 4), ("D", 2)],
        "D": [("End", 100)],
        "End": [],
    }

    result = dijkstras(graph, "Start")
    assert result["End"] == 6


def test_disconnected_components():
    graph = {1: [(2, 10)], 2: [], 3: [(4, 5)], 4: []}
    result = dijkstras(graph, 1)
    assert result[1] == 0
    assert result[2] == 10
    assert result[3] == float("inf")
    assert result[4] == float("inf")


def test_cycle_graph():
    # 1 -> 2 -> 3 -> 1
    graph = {
        1: [(2, 1)],
        2: [(3, 1)],
        3: [(1, 10)],
    }
    result = dijkstras(graph, 1)
    assert result[1] == 0
    assert result[2] == 1
    assert result[3] == 2


def test_single_node():
    graph = {"A": []}
    result = dijkstras(graph, "A")
    assert result == {"A": 0}


def test_zero_weights():
    graph = {"A": [("B", 0)], "B": [("C", 0)], "C": [("D", 5)], "D": []}
    result = dijkstras(graph, "A")
    assert result["C"] == 0
    assert result["D"] == 5


def test_multiple_paths_update():
    graph = {
        "S": [("A", 10), ("B", 1)],
        "B": [("A", 2)],
        "A": [],
    }
    result = dijkstras(graph, "S")
    assert result["A"] == 3


def test_string_and_int_nodes():
    graph = {0: [("end", 5)], "end": []}
    result = dijkstras(graph, 0)
    assert result["end"] == 5


def test_start_node_has_no_edges():
    graph = {"Start": [], "Other": []}
    result = dijkstras(graph, "Start")
    assert result["Start"] == 0
    assert result["Other"] == float("inf")


def test_large_chain_performance():
    # 0 -> 1 -> 2 -> ... -> 999
    size = 1000
    graph = {i: [(i + 1, 1)] for i in range(size - 1)}
    graph[size - 1] = []

    result = dijkstras(graph, 0)
    assert result[size - 1] == size - 1
