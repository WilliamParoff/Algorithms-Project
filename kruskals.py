import networkx as nx


def kruskal_mst(graph: nx.Graph):
    # initialize minimum spanning tree
    mst = nx.Graph()

    # sort edges in non-descending order by weight
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])

    # loop over all edges
    for (n, c, d) in edges:
        # if the edge creates a cycle, skip
        if mst.has_node(n) and mst.has_node(c):
            if nx.has_path(mst, n, c):
                continue

        # add the edge to the minimum spanning tree
        mst.add_edge(n, c, weight=d['weight'])
    # return the minimum spanning tree
    return mst
