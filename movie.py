class Movie:
    # constructor
    def __init__(self):
        self.title = ''
        self.genre = ''
        self.year = ''
        self.runtime = ''
        self.main_stars = ''
        self.director = ''
        self.reviews = ''
        self.rating = ''
        self.rank = -1
        self.similar_movies = []

    # mutator methods
    def set_title(self, title):
        self.title = title

    def set_genre(self, genre):
        self.genre = genre

    def set_year(self, year):
        self.year = year

    def set_runtime(self, runtime):
        self.runtime = runtime

    def set_main_stars(self, main_stars):
        self.main_stars = main_stars

    def set_director(self, director):
        self.director = director

    def set_reviews(self, reviews):
        self.reviews = reviews

    def set_rating(self, rating):
        self.rating = rating

    def set_rank(self, rank):
        self.rank = rank

    def set_similar_movies(self, similar_movies):
        self.similar_movies = similar_movies

    # accessor methods
    def get_title(self):
        return self.title

    def get_rank(self):
        return self.rank

    def find_similar_movies(self, c1, c2, c3, c4, c5, c6, c7):
        movie_list = []

        file = open('movies.txt', 'r', errors='ignore')

        while True:
            movie_info = file.readline()

            if not movie_info:
                break
            else:
                movie_info = movie_info.split('\t')

                title = movie_info[0]
                year = movie_info[1]
                rating = movie_info[2]
                runtime = movie_info[3]
                genre = movie_info[4]
                reviews = movie_info[5]
                director = movie_info[6]
                main_stars = movie_info[7]
                rank = 0

                # determines ranking for most similar movies
                if self.genre == genre:
                    if c1 == '1':
                        rank += 7
                    elif c1 == '2':
                        rank += 6
                    elif c1 == '3':
                        rank += 5
                    elif c1 == '4':
                        rank += 4
                    elif c1 == '5':
                        rank += 3
                    elif c1 == '6':
                        rank += 2
                    elif c1 == '7':
                        rank += 1
                if self.year == year:
                    if c2 == '1':
                        rank += 7
                    elif c2 == '2':
                        rank += 6
                    elif c2 == '3':
                        rank += 5
                    elif c2 == '4':
                        rank += 4
                    elif c2 == '5':
                        rank += 3
                    elif c2 == '6':
                        rank += 2
                    elif c2 == '7':
                        rank += 1
                if self.runtime == runtime:
                    if c3 == '1':
                        rank += 7
                    elif c3 == '2':
                        rank += 6
                    elif c3 == '3':
                        rank += 5
                    elif c3 == '4':
                        rank += 4
                    elif c3 == '5':
                        rank += 3
                    elif c3 == '6':
                        rank += 2
                    elif c3 == '7':
                        rank += 1
                if self.main_stars == main_stars:
                    if c4 == '1':
                        rank += 7
                    elif c4 == '2':
                        rank += 6
                    elif c4 == '3':
                        rank += 5
                    elif c4 == '4':
                        rank += 4
                    elif c4 == '5':
                        rank += 3
                    elif c4 == '6':
                        rank += 2
                    elif c4 == '7':
                        rank += 1
                if self.director == director:
                    if c5 == '1':
                        rank += 7
                    elif c5 == '2':
                        rank += 6
                    elif c5 == '3':
                        rank += 5
                    elif c5 == '4':
                        rank += 4
                    elif c5 == '5':
                        rank += 3
                    elif c5 == '6':
                        rank += 2
                    elif c5 == '7':
                        rank += 1
                if self.reviews == reviews:
                    if c6 == '1':
                        rank += 7
                    elif c6 == '2':
                        rank += 6
                    elif c6 == '3':
                        rank += 5
                    elif c6 == '4':
                        rank += 4
                    elif c6 == '5':
                        rank += 3
                    elif c6 == '6':
                        rank += 2
                    elif c6 == '7':
                        rank += 1
                if self.rating == rating:
                    if c7 == '1':
                        rank += 7
                    elif c7 == '2':
                        rank += 6
                    elif c7 == '3':
                        rank += 5
                    elif c7 == '4':
                        rank += 4
                    elif c7 == '5':
                        rank += 3
                    elif c7 == '6':
                        rank += 2
                    elif c7 == '7':
                        rank += 1

            movie = Movie()
            movie.set_title(title)
            movie.set_year(year)
            movie.set_rating(rating)
            movie.set_runtime(runtime)
            movie.set_genre(genre)
            movie.set_rating(rating)
            movie.set_director(director)
            movie.set_main_stars(main_stars)
            movie.set_rank(rank)

            movie_list.append(movie)

        file.close()

        return movie_list
