# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Archive():

    def __init__(self, title, poster_image, release_date_year):
        self.title = title
        self.poster_image_url = poster_image
        self.release_date = release_date_year

class Movie(Archive):
    # This class provides a way to store movie related information

    def __init__(self, title, poster_image, release_date_year, movie_storyline, trailer_youtube):
        # initialize instance of class Movie
        Archive.__init__(self, title, poster_image, release_date_year)
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Vynil(Archive):
    # This class provides a way to store info related to music Vynils

    def __init__(self, title, poster_image, release_date_year, author, trailer_youtube):
        # initialize instance of class Vynil
        Archive.__init__(self, title, poster_image, release_date_year)
        self.author = author
        self.music_youtube_url = trailer_youtube
