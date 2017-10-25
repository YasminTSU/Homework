class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

        # Did User watch movie boolean
        self.watched = True

    def __repr__(self):
        return "<Movie {}>".format(self.name)

    def json(self):
        #displaying movie info in JSON file
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }