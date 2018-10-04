# Books Phase 2 Homework
#     @author Yuting Su(suy@carelton.edu)
#     @author Starr Wang(wangy3@carleton.edu)
#      2018-09-20

import booksdatasource
import unittest


class BooksDataSourceTest(unittest.TestCase):
	def setUp(self):
		self.book_data_source=booksdatasource.BooksDataSource("books.csv", "authors.csv", "books_authors.csv")

	def tearDown(self):
		pass

	# test the method "def book(self, book_id)"
	def test_find_book_by_id(self):
		self.assertEqual(self.book_data_source.book(6), {'id': 6, 'title': 'Good Omens', 'publication_year': '1990'})

	def test_books_bad_book_id(self):
		self.assertRaises(ValueError, self.book_data_source.book, book_id = -1)

	# test the method "def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title')"
	def test_find_books_by_author(self):
		self.assertEqual(self.book_data_source.books(author_id = 5), [{'id': 6, 'title': 'Good Omens', 'publication_year': '1990'}, {'id': 15, 'title': 'Neverwhere', 'publication_year': '1996'}])

	def test_find_books_by_text(self):
		self.assertEqual(self.book_data_source.books(search_text="good"), [{'id': 6, 'title': 'Good Omens', 'publication_year': '1990'}])

	def test_find_books_by_start_year(self):
		self.assertEqual(self.book_data_source.books(start_year=2010), [{'id': 0, 'title': 'All Clear', 'publication_year': '2010'}, {'id': 3, 'title': 'Blackout', 'publication_year': '2010'}, {'id': 37, 'title': 'The Fifth Season', 'publication_year': '2015'}, {'id': 38, 'title': 'The Obelisk Gate', 'publication_year': '2015'}, {'id': 35, 'title': 'The Power', 'publication_year': '2016'}, {'id': 39, 'title': 'The Stone Sky', 'publication_year': '2015'}])

	def test_find_books_by_end_year(self):
		self.assertEqual(self.book_data_source.books(end_year=1813), [{'id': 18, 'title': 'Pride and Prejudice', 'publication_year': '1813'}, {'id': 20, 'title': 'Sense and Sensibility', 'publication_year': '1813'}])

	def test_find_books_sorted_by_year(self):
		self.assertEqual(self.book_data_source.books(end_year=1813, sort_by="year"), [{'id': 18, 'title': 'Pride and Prejudice', 'publication_year': '1813'}, {'id': 20, 'title': 'Sense and Sensibility', 'publication_year': '1813'}])

	def test_find_books_by_author_id_and_start_year(self):
		self.assertEqual(self.book_data_source.books(author_id=3, end_year=2010), [{'id': 4, 'title': 'Elmer Gantry', 'publication_year': '1927'}])

	# test the method "def author(self, author_id)"
	def test_find_author_by_id(self):
		self.assertEqual(self.book_data_source.author(4), {'id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': '1775', 'death_year': '1817'})

	def test_books_bad_author_id(self): 
		self.assertRaises(ValueError, self.book_data_source.author, author_id = -1)


	# test the method "def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year')"
	def test_find_authors_by_book_id(self):
		self.assertEqual(self.book_data_source.authors(book_id = 5), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': '1775', 'death_year': '1817'}])

	def test_find_authors_by_text(self):
		self.assertEqual(self.book_data_source.authors(search_text="Jane"), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': '1775', 'death_year': '1817'}])

	def test_find_authors_by_start_year(self):
		self.assertEqual(self.book_data_source.authors(start_year=2010), [{'id': 3, 'last_name': 'Lewis', 'first_name': 'Sinclair', 'birth_year': '1885', 'death_year': 'NULL'}, {'id': 9, 'last_name': 'Márquez', 'first_name': 'Gabriel García', 'birth_year': '1927', 'death_year': '2014'}, {'id': 24, 'last_name': 'Carré', 'first_name': 'John Le', 'birth_year': '1931', 'death_year': 'NULL'}, {'id': 2, 'last_name': 'Morrison', 'first_name': 'Toni', 'birth_year': '1931', 'death_year': 'NULL'}, {'id': 0, 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year': '1945', 'death_year': 'NULL'}, {'id': 11, 'last_name': 'Rushdie', 'first_name': 'Salman', 'birth_year': '1947', 'death_year': 'NULL'}, {'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry', 'birth_year': '1948', 'death_year': '2015'}, {'id': 12, 'last_name': 'Bujold', 'first_name': 'Lois McMaster', 'birth_year': '1949', 'death_year': 'NULL'}, {'id': 16, 'last_name': 'Murakami', 'first_name': 'Haruki', 'birth_year': '1949', 'death_year': 'NULL'}, {'id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil', 'birth_year': '1960', 'death_year': 'NULL'}, {'id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.', 'birth_year': '1972', 'death_year': 'NULL'}, {'id': 18, 'last_name': 'Alderman', 'first_name': 'Naomi', 'birth_year': '1974', 'death_year': 'NULL'}])
	
	def test_find_authors_by_end_year(self):
		self.assertEqual(self.book_data_source.authors(end_year=1850), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': '1775', 'death_year': '1817'}, {'id': 15, 'last_name': 'Brontë', 'first_name': 'Emily', 'birth_year': '1818', 'death_year': '1848'}, {'id': 14, 'last_name': 'Brontë', 'first_name': 'Ann', 'birth_year': '1820', 'death_year': '1849'}])

	def test_find_authors_by_text_and_end_year(self):
		self.assertEqual(self.book_data_source.authors(search_text='Dickens', end_year=1812), [{'id': 23, 'last_name': 'Dickens', 'first_name': 'Charles', 'birth_year': '1812', 'death_year': '1870'}])

	def test_find_authors_sort_by_birth_year(self):
		self.assertEqual(self.book_data_source.authors(end_year=1850, sort_by="birth_year"), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': '1775', 'death_year': '1817'}, {'id': 15, 'last_name': 'Brontë', 'first_name': 'Emily', 'birth_year': '1818', 'death_year': '1848'}, {'id': 14, 'last_name': 'Brontë', 'first_name': 'Ann', 'birth_year': '1820', 'death_year': '1849'}])

	#test the method "def books_for_author(self, author_id)"
	def test_books_for_author_method(self):
		self.assertEqual(self.book_data_source.books_for_author(author_id = 5), [{'id': 6, 'title': 'Good Omens', 'publication_year': '1990'}, {'id': 15, 'title': 'Neverwhere', 'publication_year': '1996'}])

	# test the method "def authors_for_book(self, book_id)"
	def test_authors_for_book_method(self):
		self.assertEqual(self.book_data_source.authors_for_book(book_id = 5), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': '1775', 'death_year': '1817'}])


if __name__ == '__main__':
    unittest.main()
