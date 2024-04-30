import networkx as nx


def kruskal_mst(graph):
    # initialize minimum spanning tree
    mst = nx.Graph()

    # add all nodes to the minimum spanning tree
    mst.add_nodes_from(graph.nodes)

    # sort edges in non-descending order by weight
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])

    # loop over all edges
    for (n, c, d) in edges:
        # if the nodes are not in the minimum spanning tree or the edge creates a cycle, skip
        if not mst.has_node(n) or not mst.has_node(c) or nx.has_path(mst, n, c):
            continue
        # add the edge to the minimum spanning tree
        mst.add_edge(n, c, **d)
    # return the minimum spanning tree
    return mst
