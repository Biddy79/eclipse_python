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
        self.name = name
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
        albums (list[Album]: A list of the albums by this artist
            The list only includes those albums in this collection, it is
            not an exhaustive list of the artist's published albums.
            
    Methods:
        add_album: Used to add a new album to the artist's album list
    """
    def __init__(self, name):
        self.name = name
        self.album = [] 
        
    def add_album(self, album):
        """ Add new album to the list.
        
        Args: 
            album (Album): Album object to add to the list
                If the album is already present, it will not added again
                (although this is yet to be implemented)
        """
        self.album.append(album)
        
    def add_song(self, name, year, title):
        """Add a new song to collection of albums
        
        This method will add songs to album collection
        A new album will be created in the collection if one dose't already exist
        
        Args:
            name (str) the name of the album
            year (int) the year of the album
            title (str) title of song
         """
        album_found = find_object(name, self.album)
        if album_found is None:
            print(name + "not found")
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print("Found album " + name)
        
        album_found.add_song(title)
            
            
            
def find_object(field, object_list):
    """Check object_list for object with name attribute equeal to field is so return"""
    for item in object_list:
        if item.name == field:
            return item 
    return None
      
            
#function to import ablums artist, album, year, song from a .txt file          
def load_data():
    artist_list = [] 

    with open("albums.txt", "r") as albums:
        for line in albums:
            #data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(f"{artist_field} {album_field} {year_field} {song_field}")
        
        new_artist = find_object(artist_field, artist_list)
        if new_artist is None:
            new_artist = Artist(artist_field)
            artist_list.append(new_artist)
        
        new_artist.add_song(album_field, year_field, song_field)
        
            
            
    return artist_list

def create_checkfile(artist_list):                
    """Create a check file from object data for comparison with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.album:
                for new_song in new_album.track:
                    print(f"{new_artist.name}\t{new_album.name}\t{new_album.year}\t{new_song.titel}", file=checkfile)
    
    
if __name__ == "__main__":
    artists = load_data()
    
    create_checkfile(artists)