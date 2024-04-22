import csv

class Movie:
    # constructor
    def __init__(self):
        self.title = ''
        self.rating = ''
        self.genre = ''
        self.year = ''
        self.reviews = ''
        self.director = ''
        self.lead_star = ''
        self.country = ''
        self.runtime = ''
        self.rank = 0.0
        self.similar_movies = []

    # mutator methods
    def set_title(self, title):
        self.title = title

    def set_rating(self, rating):
        self.rating = rating

    def set_genre(self, genre):
        self.genre = genre

    def set_year(self, year):
        self.year = year

    def set_reviews(self, reviews):
        self.reviews = reviews

    def set_director(self, director):
        self.director = director

    def set_lead_star(self, lead_star):
        self.lead_star = lead_star

    def set_country(self, country):
        self.country = country

    def set_runtime(self, runtime):
        self.runtime = runtime

    def set_rank(self, rank):
        self.rank = rank

    def set_similar_movies(self, similar_movies):
        self.similar_movies = similar_movies

    # accessor methods
    def get_title(self):
        return self.title

    def get_rank(self):
        return self.rank

    def find_similar_movies(self, c1, c2, c3, c4, c5, c6, c7, c8):
        normalizer = 0.0
        if c1 != 'None':
            normalizer += float(int(c1))
        if c2 != 'None':
            normalizer += float(int(c2))
        if c3 != 'None':
            normalizer += float(int(c3))
        if c4 != 'None':
            normalizer += float(int(c4))
        if c5 != 'None':
            normalizer += float(int(c5))
        if c6 != 'None':
            normalizer += float(int(c6))
        if c7 != 'None':
            normalizer += float(int(c7))
        if c8 != 'None':
            normalizer += float(int(c8))

        if c1 != 'None':
            c1 = float(int(c1))/normalizer
        if c2 != 'None':
            c2 = float(int(c2))/normalizer
        if c3 != 'None':
            c3 = float(int(c3))/normalizer
        if c4 != 'None':
            c4 = float(int(c4))/normalizer
        if c5 != 'None':
            c5 = float(int(c5))/normalizer
        if c6 != 'None':
            c6 = float(int(c6))/normalizer
        if c7 != 'None':
            c7 = float(int(c7))/normalizer
        if c8 != 'None':
            c8 = float(int(c8))/normalizer

        movie_list = []

        with open('movies.csv', newline='', encoding='utf-8') as db:

            read = csv.reader(db)

            for movie_info in read:
                if movie_info[0] == self.title:
                    continue
                title = movie_info[0]
                rating = movie_info[1]
                genre = movie_info[2]
                year = movie_info[3]
                reviews = movie_info[5]
                director = movie_info[7]
                lead_star = movie_info[9]
                country = movie_info[10]
                runtime = movie_info[14]
                rank = 0.0

                if c1 != 'None' and self.rating == rating:
                    rank += c1
                if c2 != 'None' and self.genre == genre:
                    rank += c2
                if c3 != 'None' and self.year == year:
                    rank += c3
                if c4 != 'None' and reviews != '':
                    norm_reviews = float(reviews) / 10.0
                    rank += c4 * norm_reviews
                if c5 != 'None' and self.director == director:
                    rank += c5
                if c6 != 'None' and self.lead_star == lead_star:
                    rank += c6
                if c7 != 'None' and self.country == country:
                    rank += c7
                if c8 != 'None' and runtime != '' and self.runtime != '':
                    if int(float(self.runtime)) <= int(float(runtime)) + 15:
                        if int(float(self.runtime)) >= int(float(runtime)) - 15:
                            rank += c8

                movie = Movie()
                movie.set_title(title)
                movie.set_rating(rating)
                movie.set_genre(genre)
                movie.set_year(year)
                movie.set_reviews(reviews)
                movie.set_director(director)
                movie.set_lead_star(lead_star)
                movie.set_country(country)
                movie.set_runtime(runtime)
                movie.set_rank(rank)

                movie_list.append(movie)

            return movie_list
