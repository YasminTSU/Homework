from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__ (self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        self.movies.append(Movie(name, genre, False))
        self.movies.append(movie)

    def delete_movie(self, name):
        return list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        # Calculate which movies have been watch and creates a list
        return list(filter(lambda movie: movie.watched, self.movies))

    def json(self):
        #displaying movie name in a json file
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies()
        ]
    }