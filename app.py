from movie import Movie
from user import User
import json

user = User("Jose")
user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The Hangover", "Comedy")


with open('my_file.txt', 'w') as f:
    json.dump(user.json(), f)