# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Archive(object):
    """Provide a way to store common information for both movies and vynils"""

    def __init__(self, title, poster_image, release_date_year):
        """Link each argument with appropriate method"""
        self.title = title
        self.poster_image_url = poster_image
        self.release_date = release_date_year

class Movie(Archive):
    """Provides a way to store movie related informations"""

    def __init__(self, title, poster_image, release_date_year, movie_director, trailer_youtube):
        """Link each argument with appropriate method"""
        Archive.__init__(self, title, poster_image, release_date_year)
        """Initialize Archive instance"""
        self.director = movie_director
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Vynil(Archive):
    """Provide a way to store info related to music Vynils"""

    def __init__(self, title, poster_image, release_date_year, author, trailer_youtube):
        """Link each argument with appropriate method"""
        Archive.__init__(self, title, poster_image, release_date_year)
        """Initialize Archive instance"""
        self.author = author
        self.music_youtube_url = trailer_youtube
