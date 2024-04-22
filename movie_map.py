import matplotlib.pyplot as plt

class MovieMap:
    def __init__(self):
        self.movie_map = {}

    def create_map(self, similar_movies):
        intial_map = {}

        for m in similar_movies:
            intial_map[m.get_title()] = m.get_rank()

        map_pairs = intial_map.items()

        sorted_map_pairs = sorted(map_pairs, key=lambda x: x[1], reverse=True)

        for t, r in sorted_map_pairs:
            self.movie_map[t] = r

    def output_map(self, clicked_option):
        num_movs = 0

        if clicked_option == 'Top 5':
            num_movs = 5
        elif clicked_option == 'Top 10':
            num_movs = 10
        elif clicked_option == 'Top 25':
            num_movs = 25

        similar_movies = list(self.movie_map.items())[:num_movs]

        titles = [mov[0] for mov in similar_movies]
        ranks = [mov[1] for mov in similar_movies]

        def title_size(title):
            if len(title) < 10:
                return 10
            elif len(title) < 20:
                return 8
            return 6

        figure, axis = plt.subplots()

        bars = axis.bar(titles, ranks)

        for title in axis.get_xticklabels():
            title.set_rotation(45)
            title.set_fontsize(title_size(title.get_text()))

        plt.tight_layout()
        plt.show()
        #plt.figure(figsize=(10, 6))
        #plt.bar(titles, ranks, color='skyblue')

        #plt.xlabel('Movie Title')
        #plt.ylabel('Rank')
        #plt.title(f'Top {num_movs} Similar Movies')

        #plt.xticks(rotation=45)
        plt.show()