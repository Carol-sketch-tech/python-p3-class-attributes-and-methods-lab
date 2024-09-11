'''
define a class Song class such that na individual song is initialized with a name, artist and genre.
create a class sttribute count - > used to keept track of the number of songd that are created from the Song class. set this attribute to equal to 0.
whenever a new song is created, yout __init__ method should call a class method add_song_to_count() that inceaments the value of count by one.

define the follwing methods.
1. add_to_genres() -> adds new genres to a class attributes genres, a list.
this list should contain a unique genres - no duplicates!
control for duplicated when you code your add_to_genres class method, not when you add genres to the original genres list.

2.add_to_artist()-> add any new artists to a class attribute artists, a list. This list should only contain unique artsit, just like the genres class attribute.
you'll need a clas attribute, artist that is equal to an empty list.
when a new song in initialized, your __init__ method should add artist to the artist list.
allartist should be added to the list.
control for duplicated when you code your add_to_articles() class method, not when you add artist to the original artists list.
will have to know how many songs each have been assigned to each artist.

3. add_to_genre_count()-> adds to a class attribute genre_count, a dictionary in which the keys are the names of each genre.
each genre key name key should point to a value that in the number of songs tat have that genre
this manner of displaying numerical data is called a histogram.

how will one create a histogram?
    1. you can need to iterate over the genres list and populate a adictionary with the key/value pairs.
    you will need to check to see if the hask already contains a key of a partibular genre.
    if so increament the value of that key by one, otherwise, create a new key/value pair.
'''

class Song:
    genres = []
    artists = []
    genre_count = []


    def __init__(self,name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.genres(genre)
        Song.artists(artist)
        Song.genre_count(genre)

        @classmethod
        def add_to_genres(cls):
            cls.genres.append(genre)

        @classmethod
        def add_to_artsits(cls):
            return cls.artists.append(artist)

        @classmethod
        def add_to_genre_count(cls, increment = 1):# still to re-do
            for _ in range(increment):
                cls.genres.append(genre)


