def dag(graph):
    status = {
        v: 0 for v in graph
    }  # 0 - before processing,  1 - in-processing, 2 - processed
    order = []

    cycle = None
    cycle_collected = False

    def dfs_dag(v):
        nonlocal cycle
        nonlocal cycle_collected

        status[v] = 1
        for w in graph[v]:
            if status[w] == 0:
                dfs_dag(w)
                if cycle:
                    if v != cycle[0] and not cycle_collected:
                        cycle.append(v)
                    else:
                        cycle_collected = True
                    return
            elif status[w] == 1:
                cycle = [w, v]
                return
        order.append(v)
        status[v] = 2

    for v in graph:
        if status[v] == 0:
            dfs_dag(v)
            if cycle:
                break

    if cycle:
        return True, list(reversed(cycle))
    else:
        return False, list(reversed(order))
