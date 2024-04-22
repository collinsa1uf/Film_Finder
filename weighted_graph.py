from networkx import *
import matplotlib.pyplot as plt
plt.matplotlib.use('TkAgg')


class WeightedGraph:
    def __init__(self):
        self.weighted_graph = []

    def output_graph(self, clicked_option):
        graph = Graph()
        num_nodes = 0

        # number of vertices extending off of inputted movie vertex
        if clicked_option == 'Top 5':
            num_nodes = 5
        elif clicked_option == 'Top 10':
            num_nodes = 10
        elif clicked_option == 'Top 25':
            num_nodes = 25

        # find top #_ of most similar vertices
        top_similar_vertices = []
        num = 0

        while num < num_nodes:
            least_weight = 50.0
            for edge in self.weighted_graph:
                print('here')
                if edge[2] < least_weight:
                    least_weight = edge[2]
            for edge in self.weighted_graph:
                if edge[2] == least_weight:
                    print('here')
                    top_similar_vertices.append(edge)
                    self.weighted_graph.pop(self.weighted_graph.index(edge))
                    break
            num += 1

        #for v in top_similar_vertices:
            #print(v)
        # outputs graph with top #_ of similar movies extending from inputted movie vertex
        for v in top_similar_vertices:
            graph.add_edge(v[0].get_title(), v[1].get_title(), weight=v[2])

        pos = spring_layout(graph)
        edge_labels = get_edge_attributes(graph, 'weight')
        node_list = list(graph.nodes)
        node_list.pop(0)

        draw_networkx_nodes(graph, pos, node_size=500, nodelist=[self.weighted_graph[0][0].get_title()], node_color='red')
        draw_networkx_nodes(graph, pos, node_size=500, nodelist=node_list)
        draw_networkx_edges(graph, pos, alpha=0.5)
        draw_networkx_labels(graph, pos=pos, font_size=10)
        draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels, label_pos=0.5)

        axis = plt.gca()
        axis.margins(0.25)
        plt.tight_layout()
        plt.axis('off')
        plt.show()

    def create_graph(self, movie, similar_movies):
        vertices = []

        # removes all movies that are not at all similar to the inputted movie
        for m in similar_movies:
            if m.get_rank() == 0.0:
                continue
            elif m.get_title() == movie.get_title():
                continue
            else:
                vertices.append(m)

        for v in vertices:
            edge = [movie, v, round((1.0 / v.get_rank()) * 10, 2)]

            self.weighted_graph.append(edge)