from homework_9.dag.dag import dag


def is_valid_toposort(graph, order):
    order_list = list(order)
    if len(order_list) != len(graph):
        return False

    position = {node: i for i, node in enumerate(order_list)}

    for u in graph:
        for v in graph[u]:
            if position[u] > position[v]:
                return False
    return True


def is_valid_cycle(graph, cycle):
    cycle_list = list(cycle)
    if not cycle_list:
        return False

    for i in range(len(cycle_list)):
        u = cycle_list[i]
        v = cycle_list[(i + 1) % len(cycle_list)]

        if v not in graph[u]:
            return False

    return True


def test_empty_graph():
    graph = {}
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert list(result) == []


def test_single_node_no_edges():
    graph = {1: []}
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert list(result) == [1]


def test_simple_path_dag():
    graph = {1: [2], 2: [3], 3: []}
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert is_valid_toposort(graph, result)


def test_diamond_dag():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert is_valid_toposort(graph, result)


def test_disconnected_components_dag():
    graph = {1: [2], 2: [], 3: [4], 4: []}
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert is_valid_toposort(graph, result)


def test_simple_cycle():
    graph = {1: [2], 2: [1]}
    has_cycle, result = dag(graph)
    assert has_cycle is True
    assert is_valid_cycle(graph, result)


def test_triangle_cycle():
    graph = {1: [2], 2: [3], 3: [1]}
    has_cycle, result = dag(graph)
    assert has_cycle is True
    assert is_valid_cycle(graph, result)


def test_self_loop():
    graph = {1: [1]}
    has_cycle, result = dag(graph)
    assert has_cycle is True
    assert is_valid_cycle(graph, result)


def test_cycle_with_tail():
    graph = {1: [2], 2: [3], 3: [2]}
    has_cycle, result = dag(graph)
    assert has_cycle is True

    cycle_list = list(result)
    assert 1 not in cycle_list
    assert is_valid_cycle(graph, cycle_list)


def test_cycle_in_second_component():
    graph = {1: [2], 2: [], 3: [4], 4: [3]}
    has_cycle, result = dag(graph)
    assert has_cycle is True
    assert is_valid_cycle(graph, result)
    assert 3 in list(result) or 4 in list(result)


def test_figure_eight_cycle():
    graph = {1: [2, 3], 2: [1], 3: [1]}
    has_cycle, result = dag(graph)
    assert has_cycle is True
    assert is_valid_cycle(graph, result)


def test_complex_structure_no_cycle():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert is_valid_toposort(graph, result)


def test_cycle_large_recursion():
    size = 100
    # 0->1->2...->99->0
    graph = {i: [(i + 1) % size] for i in range(size)}

    has_cycle, result = dag(graph)
    assert has_cycle is True
    assert len(list(result)) == size
    assert is_valid_cycle(graph, result)
