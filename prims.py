import random
from queue import PriorityQueue
import networkx as nx


def prim_mst(graph: nx.Graph):
    pq = PriorityQueue()
    mst = nx.Graph()
    visited = set()

    node = random.choice(list(graph.nodes))
    for (n, c, d) in graph.edges(node, data=True):
        pq.put((d['weight'], (n, c, d)))

    while not pq.empty():
        weight, (n, c, d) = pq.get()
        if c in visited:
            continue

        mst.add_edge(n, c, **d)
        visited.add(n)
        visited.add(c)

        for (nn, cc, dd) in graph.edges(c, data=True):
            if cc not in visited:
                pq.put((dd['weight'], (nn, cc, dd)))

    return mst




