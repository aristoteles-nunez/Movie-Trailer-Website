import media
import fresh_tomatoes
import json

def read_data_from_json_file(file_name):
	"""Method that reads a file with JSON content.

	Args:
		file_name: Exactly path of the file, if the file is in the same 
				   directory of the program just pass the name.
	Returns:
		A python Dict Object from a valid Json Document.
	Raises:
		An Exception if the data being deserialized is not a valid JSON
		document or the file isn't found.
	"""

	try:
		data = json.load(open(file_name))
	except Exception as e1 :
		print("Error  failed to open file: {}".format(file_name))
		print ( e1 )
		sys.exit(0)
	return data


def main():
	"""Program that reads a JSON data to build a movie trailer website 
	"""
	favorites_movies = read_data_from_json_file("data.json")
	movies = []

	# For each JSON Object we create an instance of class Movie 
	# setting every corresponding value 
	for element in favorites_movies:
		title = element["title"]
		storyline = element["storyline"]
		poster_image_url = element["poster_image_url"]
		trailer_youtube_url = element["trailer_youtube_url"]
		release_year = element["release_year"]
		imdb_data_title = element["imdb_data_title"]
		imdb_alt_msg = title + " (" + str(release_year) + ") on IMDb"
		movie = media.Movie(title, storyline, poster_image_url, 
							trailer_youtube_url, release_year,
							imdb_data_title, imdb_alt_msg)
		movies.append(movie)
	
	fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()



