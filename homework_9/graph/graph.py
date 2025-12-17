from collections import deque


def get_components(graph) -> list[list[int]]:
    visited = set()
    components = []
    for v in graph:
        if v in visited:
            continue
        new_component = []
        bfs_queue = deque()
        bfs_queue.append(v)
        visited.add(v)
        while bfs_queue:
            current_v = bfs_queue.popleft()
            new_component.append(current_v)
            for w in graph[current_v]:
                if w in visited:
                    continue
                visited.add(w)
                bfs_queue.append(w)
        components.append(new_component)

    return components
