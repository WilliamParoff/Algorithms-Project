import random
from queue import PriorityQueue
import networkx as nx


def prim_mst(graph: nx.Graph):
    # initialize priority queue
    pq = PriorityQueue()
    # initialize minimum spanning tree
    mst = nx.Graph()
    # initialize visited set
    visited = set()

    # choose a random node to start
    node = random.choice(list(graph.nodes))
    # add all edges from the starting node to the priority queue
    for (n, c, d) in graph.edges(node, data=True):
        pq.put((d['weight'], (n, c, d)))

    # while the priority queue is not empty
    while not pq.empty():
        # get the edge with the minimum weight
        weight, (n, c, d) = pq.get()
        # if the node is already visited, skip
        if c in visited:
            continue

        # add the edge to the minimum spanning tree
        mst.add_edge(n, c, **d)
        visited.add(c)

        # loop over all edges from the current node
        for (nn, cc, dd) in graph.edges(c, data=True):
            # if the node is not visited, add the edge to the priority queue
            if cc not in visited:
                pq.put((dd['weight'], (nn, cc, dd)))

    # return the minimum spanning tree
    return mst




