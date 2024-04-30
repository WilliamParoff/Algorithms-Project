import time
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


def evaluate_graph(graph):
    weight_sum = 0
    for (u, v) in graph.edges():
        weight_sum += graph[u][v]['weight']
    return weight_sum


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

    # ========================
    # prim_mst tests
    # ========================
    prim_sparse = prim_mst(sparse)
    prim_dense = prim_mst(dense)
    prim_weighted = prim_mst(weighted)

    # ========================
    # kruskal_mst tests
    # ========================
    kruskal_sparse = kruskal_mst(sparse)
    kruskal_dense = kruskal_mst(dense)
    kruskal_weighted = kruskal_mst(weighted)

    # ========================
    # draw mst graphs
    # ========================
    plt.subplot(4, 3, 1)
    plt.title("Sparse Graph")
    plt.text(0.01, 0.99, f"Weight: {evaluate_graph(sparse)}", fontsize=12, ha='left', va='top',
             transform=plt.gca().transAxes)
    draw_graph(sparse)

    plt.subplot(4, 3, 2)
    plt.title("Dense Graph")
    plt.text(0.01, 0.99, f"Weight: {evaluate_graph(dense)}", fontsize=12, ha='left', va='top',
             transform=plt.gca().transAxes)
    draw_graph(dense)

    plt.subplot(4, 3, 3)
    plt.title("Weighted Graph")
    plt.text(0.01, 0.99, f"Weight: {evaluate_graph(weighted)}", fontsize=12, ha='left', va='top',
             transform=plt.gca().transAxes)
    draw_graph(weighted, weighted=True)

    plt.subplot(4, 3, 4)
    plt.title("Prim MST Sparse")
    plt.text(0.01, 0.99, f"Weight: {evaluate_graph(prim_sparse)}", fontsize=12, ha='left', va='top',
             transform=plt.gca().transAxes)
    draw_graph(prim_sparse)

    plt.subplot(4, 3, 5)
    plt.title("Prim MST Dense")
    plt.text(0.01, 0.99, f"Weight: {evaluate_graph(prim_dense)}", fontsize=12, ha='left', va='top',
             transform=plt.gca().transAxes)
    draw_graph(prim_dense)

    plt.subplot(4, 3, 6)
    plt.title("Prim MST Weighted")
    plt.text(0.01, 0.99, f"Weight: {evaluate_graph(prim_weighted)}", fontsize=12, ha='left', va='top',
             transform=plt.gca().transAxes)
    draw_graph(prim_weighted)

    plt.subplot(4, 3, 7)
    plt.title("Kruskal MST Sparse")
    plt.text(0.01, 0.99, f"Weight: {evaluate_graph(kruskal_sparse)}", fontsize=12, ha='left', va='top',
             transform=plt.gca().transAxes)
    draw_graph(prim_sparse)

    plt.subplot(4, 3, 8)
    plt.title("Kruskal MST Dense")
    plt.text(0.01, 0.99, f"Weight: {evaluate_graph(kruskal_dense)}", fontsize=12, ha='left', va='top',
             transform=plt.gca().transAxes)
    draw_graph(prim_dense)

    plt.subplot(4, 3, 9)
    plt.title("Kruskal MST Weighted")
    plt.text(0.01, 0.99, f"Weight: {evaluate_graph(kruskal_weighted)}", fontsize=12, ha='left', va='top',
             transform=plt.gca().transAxes)
    draw_graph(prim_weighted)

    # ========================
    # test time complexity
    # ========================
    start_time = time.time()
    for _ in range(1000):
        prim_mst(sparse)
    prim_sparse_time = time.time() - start_time

    start_time = time.time()
    for _ in range(1000):
        prim_mst(dense)
    prim_dense_time = time.time() - start_time

    start_time = time.time()
    for _ in range(1000):
        prim_mst(weighted)
    prim_weighted_time = time.time() - start_time

    start_time = time.time()
    for _ in range(1000):
        kruskal_mst(sparse)
    kruskal_sparse_time = time.time() - start_time

    start_time = time.time()
    for _ in range(1000):
        kruskal_mst(dense)
    kruskal_dense_time = time.time() - start_time

    start_time = time.time()
    for _ in range(1000):
        kruskal_mst(weighted)
    kruskal_weighted_time = time.time() - start_time

    # ========================
    # write time complexity
    # ========================
    plt.subplot(4, 3, 10)
    plt.title("Sparse MST Time")
    plt.text(0.5, 0.5, f"Prim: {prim_sparse_time:.4f}\nKruskal: {kruskal_sparse_time:.4f}", fontsize=12, ha='center',
             va='center')

    plt.subplot(4, 3, 11)
    plt.title("Dense MST Time")
    plt.text(0.5, 0.5, f"Prim: {prim_dense_time:.4f}\nKruskal: {kruskal_dense_time:.4f}", fontsize=12, ha='center',
             va='center')

    plt.subplot(4, 3, 12)
    plt.title("Weighted MST Time")
    plt.text(0.5, 0.5, f"Prim: {prim_weighted_time:.4f}\nKruskal: {kruskal_weighted_time:.4f}", fontsize=12, ha='center',
             va='center')

    # ========================
    # show plots
    # ========================
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
