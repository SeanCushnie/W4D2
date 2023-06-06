import unittest
from models.artist import Artist
from models.album import Album

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        
        self.artist = Artist("Ravey Davey")
        
        self.album = Album("Doosh Doosh", "Dance", self.artist)
    
    
    def test_album_has_title(self):
        self.assertEqual("Doosh Doosh", self.album.title)
        
        
    def test_album_has_genre(self):
        self.assertEqual("Dance", self.album.genre)
    
        
    def test_album_has_artist(self):
        self.assertEqual(self.artist, self.album.artist)
    