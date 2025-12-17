import heapq


def dijkstras(graph, v):
    dists = {vertex: float("inf") for vertex in graph}
    priority_queue = [(0, v)]
    dists[v] = 0
    while priority_queue:
        dist, vertex = heapq.heappop(priority_queue)
        if dist > dists[vertex]:
            continue

        for w, weight in graph[vertex]:
            if dists[w] > weight + dist:
                heapq.heappush(priority_queue, (weight + dist, w))
                dists[w] = weight + dist

    return dists
