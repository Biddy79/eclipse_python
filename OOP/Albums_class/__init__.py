class Song:
    """Class to represent a song
    
    Attributes:
        titel (str): The titel of the song 
        artist (Artist): An artist object representing the song creator
        duration (int): duration of the song in seconds> May be zero
    """
    
    def __init__(self, titel, artist, duration=0):
        self.titel = titel
        self.artist = artist
        self.duration = duration

#prints out doc string for given class     
print(Song.__doc__)


class Album:
    """ Class to represent an Album, using it's track list
    
    Attribute:
        name (str): The name of the alubm
        year (int): The year the album was released 
        artist (Artist): The artist responsible for the album
           If not specified the artist will default to an artist with the 
           name "Various Artists"
        track (list[Song]): A list of hte song on the album
        
    Methods: 
        addSong: used to add a new song to the album's teack list.
    """
    
    def __init__(self, name, year, artist=None):
        self.album_name = name
        self.year = year 
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist
        
        self.track = []
        
    def add_song(self, song, position=None):
        """Adds a song to the track list
    
        Args:
            song (Song): A song to add
            position (optional[int]): If specified, the song will be added to that position
            in the track list - inserting it between other songs if necessary
            otherwise, the song will be added to the end of the list
        """
        if position is None:
            self.track.append(song)
        else:
            self.tracks.insert(position, song)
            
#prints out doc string for Album Class with attributes and methods 
help(Album)


class Artist:
    """ Basic class to store artist details
    
    Attributes: 
        name (str): The name of the artist
        albums (list[Album]: A list of hte albums by this artist
            The list only includes those albums in this collection, it is
            not an exhaustive list of the artist's published albums.
            
    Methods:
        add_album: Used to add a new album to the artist's album list
    """
    def __init__(self, name):
        self.name = name
        self.albuma = [] 
        
    def add_album(self, album):
        """ Add new album to the list.
        
        Args: 
            album (Album): Album object to add to the list
                If the album is already present, it will not added again
                (although this is yet to be implemented)
        """
        self.album.append(album)
            
            
#function to import ablums artist, album, year, song from a .txt file          
def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    
    with open("albums.txt", "r") as albums:
        for line in albums:
            #data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)
        
        
        
if __name__ == "__main__":
    load_data()
    
    
    
    
    
        
        
        
        
        
        
    
    
    
    
    
