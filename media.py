import webbrowser

class Movie():
	"""This class provides a way to store movie related information """

	def __init__(self, movie_title, movie_storyline, 
				movie_poster_image_url, movie_trailer_youtube_url, 
				release_year, imdb_data_title, imdb_alt_msg):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_image_url
		self.trailer_youtube_url = movie_trailer_youtube_url
		self.release_year = release_year
		self.imdb_data_title = imdb_data_title
		self.imdb_alt_msg = imdb_alt_msg

	def show_trailer(self):
		"""Method that opens the movie trailer in the browser """
		webbrowser.open(self.trailer_youtube_url)

		
