import json
import jgrapht
from jgrapht.algorithms.tour import metric_tsp_christofides
import jgrapht.drawing.draw_matplotlib as drawing
import matplotlib.pyplot as plt
import jgrapht.algorithms.shortestpaths as sp
import jgrapht


def print_hi(name):

    # read file
    with open('graph.json', 'r',  encoding='utf-8') as myfile:
        data = myfile.read()

    g = jgrapht.create_graph(directed=False, weighted=True)

    # parse file
    graph = json.loads(data)['graph']
    for node in enumerate(graph["node"]):
        node_id = node[1]["id"]
        g.add_vertex(node_id)

    for edge in enumerate(graph["edge"]):
        g.add_edge(edge[1]["source"], edge[1]["target"], weight=edge[1]["weight"])

    print(g)

    tree = sp.dijkstra(g, source_vertex=6)
    path = tree.get_path(8)

    print('path start: {}'.format(path.start_vertex))
    print('path end: {}'.format(path.end_vertex))
    print('path edges: {}'.format(path.edges))
    print('path vertices: {}'.format(path.vertices))
    print('path weight: {}'.format(path.weight))

    positions = drawing.layout(g, seed=10, name="random")

    drawing.draw_jgrapht(
        g,
        positions=positions,
        node_label=True,
        node_color=range(len(g.vertices)),
        node_cmap=plt.cm.Blues,
        edge_linewidth=4,
        arrow=True,
        arrow_color="orange",
        arrow_line="dotted",
        connection_style="arc3,rad=-0.3",
        axis=False,
    )
    plt.show()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
