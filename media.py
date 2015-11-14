# Import for class function

import webbrowser

# Class with initializer


class Movie:
    def __init__(self, title, description, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.description = description
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def open_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
