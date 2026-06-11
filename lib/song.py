class Song:
    """Represents a song and tracks global library statistics."""

    # Class attributes for global insights
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update global stats
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        """Add the song's genre to the global genres list (unique)."""
        # Ensure uniqueness
        if cls._current_instance_genre() not in cls.genres:
            cls.genres.append(cls._current_instance_genre())

    @classmethod
    def add_to_artists(cls):
        """Add the song's artist to the global artists list (unique)."""
        if cls._current_instance_artist() not in cls.artists:
            cls.artists.append(cls._current_instance_artist())

    @classmethod
    def add_to_genre_count(cls):
        """Increment the counter for this song's genre."""
        genre = cls._current_instance_genre()
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls):
        """Increment the counter for this song's artist."""
        artist = cls._current_instance_artist()
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def _current_instance_genre(cls):
        """Helper to access the genre of the most recently created Song instance.

        Implementation note: class methods are called from __init__ on the
        freshly-created instance, so inspect the last-created instance via
        Python's call stack by retrieving the last global Song instance if
        available. However, to keep this simple and reliable, these helper
        methods will read the last arguments passed to __init__ by relying on
        the instance that invoked the method being available as `self`.
        """
        # This helper will be replaced dynamically by instance-bound calls.
        # As a fallback, return an empty string.
        return ""

    @classmethod
    def _current_instance_artist(cls):
        return ""

    # Monkey-patch-friendly wrappers: when called from an instance, Python
    # will bind the function and pass the instance as the first argument.
    # To allow the classmethod implementations above to access the instance
    # attributes, we provide instance-level wrappers below.

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

    def add_song_to_count(self):
        Song.count += 1
