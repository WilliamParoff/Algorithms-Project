import random

import networkx as nx
import matplotlib.pyplot as plt

from prims import prim_mst
from kruskals import kruskal_mst


def generate_graph(degree, nodes, default_weight=1, wight_range=None):
    graph = nx.generators.random_regular_graph(degree, nodes)
    for (u, v) in graph.edges():
        graph[u][v]['weight'] = default_weight if wight_range is None else random.randint(*wight_range)
    return graph


def draw_graph(graph, weighted=False, draw=False):
    pos = nx.spring_layout(graph)
    if weighted:
        edge_labels = nx.get_edge_attributes(graph, "weight")
        nx.draw_networkx_nodes(graph, pos)
        nx.draw_networkx_edges(graph, pos)
        nx.draw_networkx_labels(graph, pos)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels)
    else:
        nx.draw_networkx(graph, pos)
    if draw:
        plt.show()


def main():
    # sparse graph is a regular graph with low degree
    sparse = generate_graph(4, 10)
    # dense graph is a regular graph with high degree
    dense = generate_graph(8, 10)
    # weighted graph is a regular graph with non-uniform weights
    weighted = generate_graph(6, 10, wight_range=(1, 10))

    # prim_mst tests
    prim_sparse = prim_mst(sparse)
    prim_dense = prim_mst(dense)
    prim_weighted = prim_mst(weighted)

    # kruskal_mst tests
    kruskal_sparse = kruskal_mst(sparse)
    kruskal_dense = kruskal_mst(dense)
    kruskal_weighted = kruskal_mst(weighted)

    # draw graphs
    plt.subplot(3, 3, 1)
    plt.title("Sparse Graph")
    draw_graph(sparse)
    plt.subplot(3, 3, 2)
    plt.title("Dense Graph")
    draw_graph(dense)
    plt.subplot(3, 3, 3)
    plt.title("Weighted Graph")
    draw_graph(weighted, weighted=True)
    plt.subplot(3, 3, 4)
    plt.title("Prim MST Sparse")
    draw_graph(prim_sparse)
    plt.subplot(3, 3, 5)
    plt.title("Prim MST Dense")
    draw_graph(prim_dense)
    plt.subplot(3, 3, 6)
    plt.title("Prim MST Weighted")
    draw_graph(prim_weighted)

    plt.show()


if __name__ == '__main__':
    main()
