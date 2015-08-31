
[TOC]
# Movie Trailer Website
Program that list a serie of your favorite movies, with title, release year, youtube trailer and IMDb rating.

# What's included
Within the download you'll find the following directories and files:
```
movies/
├── entertainment_center.py
├── fresh_tomatoes.py
├── media.py
└── data.json
```


# Prerequisites

This program is compatible with `Python 2.7.x` and `Python 3.x`.


# Program Execution

* Download the compressed file `Movie-Trailer-Website-master.zip`.
* Descompress the file. It will create `Movie-Trailer-Website-master` directory
* Open a terminal and go to the `Movie-Trailer-Website-master` directory just created.

```
cd path_to_downloads_folder/Movie-Trailer-Website-master/
```

* Executes the program with:

```
python entertainment_center.py
```

* It will open your default browser, now enjoy the movie trailers.

# How to add more movies
To add or replace the movies listed, edit the file `data.json`. This file contains JSON documents with the following strcuture:

```
{
	"title": "Peaceful Warrior",
	"storyline": "A chance encounter with a stranger changes the life of a college gymnast.",
	"poster_image_url": "https://upload.wikimedia.org/wikipedia/en/9/9c/Peaceful_warrior.jpg",
	"trailer_youtube_url": "https://www.youtube.com/watch?v=gegNMYvY_yg",
	"release_year": 2006,
	"imdb_data_title":"tt0438315"
}
```

So you must replace, add or modify that information to match with your own favorites movies.

In the section [About IMDb Plugin](#markdown-header-about-imdb-plugin) you can find information about how to get `imdb_data_title`.

Remember that all the data within `data.json` must be well formed JSON documents.

# About IMDb Plugin

IMDb has a service [IMDb Plugins](http://www.imdb.com/plugins) that will display the IMDb rating for all titles that have a rating. If a movie/TV series has yet to be released, or if the title hasn't received enough votes, the plugin will only display the IMDb logo without any rating. Once the title has enough votes, the rating will automatically appear. If this occurs please verify the title you are trying to add, actually has a rating.


In the "Frequently Asked Questions" says:
> Anyone can use the rating plugin. For example, if you have a personal blog or a commercial website, you can use the provided HTML snippet to display on your site.

So you can use it with confidence.

To obtain `imdb_data_title` required followg the next steps:

* Enter to: [IMDb Plugins](http://www.imdb.com/plugins).
* Write the movie name into texbox "Choose a title." and press `Search`.
* Choose the desirable movie from the list.
* Choose the Style for the plugin.
* Press the `Create HTML` button.
* It will display a chunk of html code, that looks like:

```
<span class="imdbRatingPlugin" data-user="ur623559777" data-title="tt0438315" data-style="p1"><a href="http://www.imdb.com/title/tt0438315/?ref_=plg_rt_1"><img src="http://g-ecx.images-amazon.com/images/G/01/imdb/plugins/rating/images/imdb_46x22.png" alt=" Peaceful Warrior
(2006) on IMDb" />
</a></span><script>(function(d,s,id){var js,stags=d.getElementsByTagName(s)[0];if(d.getElementById(id)){return;}js=d.createElement(s);js.id=id;js.src="http://g-ec2.images-amazon.com/images/G/01/imdb/plugins/rating/js/rating.min.js";stags.parentNode.insertBefore(js,stags);})(document,'script','imdb-rating-api');</script>
```

* Find the number into the `data_title` tag, in this example it is `tt0438315`, and that's it, now you can use it in your program.


# Improvements to original code
`Movie Trailer Website` program was based in the code showed in Udacity's course `Python Fundamentals` with the following improvements:

* IMDb Rating was added.
* The input data was separated from python code and read it from a JSON Document file.
* The `css` was changed to fill all the screen (noticed in big screens), using the `container-fluid` class provided by bootstrap.
* The `css` was changed to show four columns on large screens, three columns in medium screens, two columns in small screens, and one colummn in really small screens, with the following classes: `col-sm-6`, `col-md-4`, and  `col-lg-3` provided by bootstrap.
* The `css` was changed to show gradient background when cursor was over. To obtain the gradient code the following site was used: [Colozilla](http://colorzilla.com/gradient-editor/#000000+0,000000+100&amp;0+0,0.65+100).

# Contributors list
* Teachers at Udacity. (Original code)
* Aristóteles Federico Núñez Juárez (Improvements)

