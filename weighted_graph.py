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

        # inputted movie vertex
        graph.add_node(self.weighted_graph[0][0].get_title(), color='red')

        # find top #_ of most similar vertices
        top_similar_vertices = []
        num = 0
        while num < num_nodes:
            max_rank = 0
            for i in self.weighted_graph:
                if self.weighted_graph[i][2] > max_rank:
                    max_rank = self.weighted_graph[i][2]
            for i in self.weighted_graph:
                if self.weighted_graph[i][2] == max_rank:
                    top_similar_vertices.append(self.weighted_graph[i])
                    self.weighted_graph.pop(i)
                    continue
            num += 1

        # Debug: print(len(top_similar_vertices))

        # outputs graph with top #_ of similar movies extending from inputted movie vertex
        for i in top_similar_vertices:
            graph.add_edge(top_similar_vertices[0].get_title(), top_similar_vertices[1].get_title(), weight=top_similar_vertices[2])

        pos = spring_layout(graph)
        draw(graph, pos, node_color='red', node_size=600)
        edge_labels = get_edge_attributes(graph, 'weight')
        draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels, label_pos=0.5)
        plt.axis('off')
        plt.show()

    def create_graph(self, movie, similar_movies):
        vertices = []

        # removes all movies that are not at all similar to the inputted movie
        for m in similar_movies:
            if m.get_rank() == 0:
                continue
            else:
                vertices.append(m)

        edge = []

        for v in vertices:
            edge.append(movie)
            edge.append(v)
            edge.append(1 / v.get_rank())

            self.weighted_graph.append(edge)
