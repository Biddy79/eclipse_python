from _operator import itemgetter
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
        
def find_object(field, object_list):
    """Check object_list for object with name attribute equeal to field is so return"""
    for item in object_list:
        if item.name == field:
            return item 
    return None
      
            
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
            print(f"{artist_field} {album_field} {year_field} {song_field}")
        
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            #chenking if artist name_field in .txt file as changed form object Artist.name
            elif new_artist.name != artist_field:
                #retrieve the artist object if there is one
                #otherwise create a new artist object and add it to artist list
                new_artist = find_object(artist_field,artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None
            
            if new_album is None:
                #create new Album object if None
                new_album = Album(album_field, year_field, new_artist)
                #add new Album to album list in Artist class
                new_artist.add_album(new_album)
            #check to see if album name as changed
            elif new_album.name != album_field:
                #retrieve the album object if there is one
                #otherwise create a new album object and add it to album list in Artist class
                new_album = find_object(album_field, new_artist.album)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    #add album object to album list in Artist class object
                    new_artist.add_album(new_album)
                
            #create instance of Song object populate with song and artist field args
            new_song = Song(song_field, new_artist)
            #add new_song object to trak list in new_album object class
            new_album.add_song(new_song)    
        
    #return a list of Artist and Album objects       
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
    
    print(f"There are {len(artists)} artists")
    
    create_checkfile(artists)

    
    #prints First artist name in .txt file
    print(artists[0].name)
    #prints forth artists third album name in .txt file
    print(artists[3].album[2].name)
    #prints third artists first album, second track name in .txt
    print(artists[2].album[0].track[1].titel)
    #prints third artist, first album second track artist(obj).name
    print(artists[2].album[0].track[1].artist.name)
    
