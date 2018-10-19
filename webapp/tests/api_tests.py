# Books Phase 4 Homework
#     @author Yuting Su(suy@carelton.edu)
#     @author Starr Wang(wangy3@carleton.edu)
#      2018-10-14

import musicdatasource
import unittest

class MusicDataSourceTest(unittest.TestCase):
  def setUp(self):
    self.music_data_source=musicdatasource.MusicDataSource("music.csv")

  def tearDown(self):
    pass

  # test the method "def singer(self, singer_id)"
  def test_find_singer_by_singer_id(self):
    self.assertEqual(self.music_data_source.singer(3), 
      {'id':'3', 'name':'Adam_Ant', 'location':'London, England', 'hotness':0.45})

  def test_find_singer_with_bad_singer_id(self):
    self.assertRaises(ValueError, self.music_data_source.singer, singer_id = -1)

  # test the method "def singers(self, *, name=None, sort_by='id')"
  def test_find_singers_by_name(self):
    self.assertEqual(self.music_data_source.singers(name='ada')
      [{'id':'23', 'name':'Ada Jane'},
       {'id':'67', 'name':'Adalberto Santiago'},
       {'id':'98', 'name':'Adam Ant'},
       {'id':'102', 'name':'Adam Richman'}])

  # test the method "def song(self, song_id)"
  def test_find_song_by_song_id(self):
    self.assertEqual(self.music_data_source.song(6404), 
      {'id':'6404', 'song_name':'Standing On My Own', 'singer_name':'Agnostic Front', 
      'album_name':'Dead Yuppies', 'genre':'hardcore punk', 'duration':105, 'hotness':0.61, 'year':2001})

  def test_find_song_bad_song_id(self): 
    self.assertRaises(ValueError, self.music_data_source.song, song_id = -1)

  # test the method "def songs (self, *, song_name=None, singer_id=None, album_name=None, 
  # hotness=None, genre=None, year=None, sort_by='id')"
  def test_find_songs_by_singer_id(self):
    self.assertEqual(self.music_data_source.songs(singer_id = 3), 
      [{'id':'3', 'song_name':'Something Girls'},
      {'id':'2861', 'song_name':'Friend Or Foe'},
      {'id':'5584', 'song_name':'Goody Two Shoes'},
      {'id':'7767', 'song_name':'Manzenera'},
      {'id':'9296', 'song_name':'Mahair Locker Room Pin-Up Boys'}])

  def test_find_songs_by_genre_and_hotness(self):
      self.assertEqual(self.music_data_source.songs(genre='alternative rock', hotness=0.6), 
        [{'id':'1036', 'song_name':'The Dynamo Of Volition [From An All Night Session]'},
         {'id':'3489', 'song_name':'No Stopping Us [Eagles Ballroom Live Version]'},
         {'id':'4642', 'song_name':'Song For A Friend (Live From Montalvo)'},
         {'id':'5520', 'song_name':'Real Love'},
         {'id':'8530', 'song_name':'Rocket'}])

  def test_find_songs_by_year_and_hotness(self):
    self.assertEqual(self.music_data_source.songs(year=2010, hotness=0.78), 
      [{'id':'239', 'song_name':"Hey Daddy (Daddy's Home)"},
       {'id':'554', 'song_name':'State of Emergency'},
       {'id':'1427', 'song_name':'You And Your Heart'},
       {'id':'9895', 'song_name':'I Know A Place'}])

  def test_find_songs_by_year_genre_and_hotness(self):
    self.assertEqual(self.music_data_source.songs(year=2010, genre='blue rock', hotness=0.6), 
      [{'id':'554', 'song_name':'State of Emergency'},
       {'id':'8650', 'song_name': 'Lullaby For The Summer'},
       {'id':'9895', 'song_name':'I Know A Place'}])

  def test_find_songs_with_bad_year(self):
    self.assertRaises(ValueError, self.music_data_source.songs, year = -1)

if __name__ == '__main__':
    unittest.main()
