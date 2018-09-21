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
		self.assertEqual(self.book_data_source.book(6), {'id': 6, 'title': 'Good Omens', 'publication_year': 1990})

	def test_books_bad_book_id(self):
		self.assertRaises(ValueError, self.book_data_source.book, book_id = -1)


	# test the method "def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title')"
	def test_find_books_by_author(self):
		self.assertEqual(self.book_data_source.books(author_id = 5), [{'id': 6, 'title': 'Good Omens', 'publication_year': 1990}])

	def test_find_books_by_text(self):
		self.assertEqual(self.book_data_source.books(search_text="good"), [{'id': 6, 'title': 'Good Omens', 'publication_year': 1990}])

	def test_find_books_by_start_year(self):
		self.assertEqual(self.book_data_source.books(start_year=2010), [{'id': 3, 'title': 'All Clear', 'publication_year': 2010}, {'id': 9, 'title': 'Blackout', 'publication_year': 2010}])

	def test_find_books_by_end_year(self):
		self.assertEqual(self.book_data_source.books(end_year=1813), [{'id': 19, 'title': 'Pride and Prejudice', 'publication_year': 1813}, {'id': 21, 'title': 'Sense and Sensibility', 'publication_year': 1813}, {'id': 31, 'title': 'The Life and Opinions of Tristram', 'publication_year': 1759}])

	def test_find_books_sorted_by_year(self):
		self.assertEqual(self.book_data_source.books(end_year=1813, sort_by="year"), [{'id': 31, 'title': 'The Life and Opinions of Tristram', 'publication_year': 1759}, {'id': 19, 'title': 'Pride and Prejudice', 'publication_year': 1813}, {'id': 21, 'title': 'Sense and Sensibility', 'publication_year': 1813}])

	def test_find_books_by_author_id_and_start_year(self):
		self.assertEqual(self.book_data_source.books(author_id=3, start_year=2010), [{'id': 3, 'title': 'All Clear', 'publication_year': 2010}])


	# test the method "def author(self, author_id)"
	def test_find_author_by_id(self):
		self.assertEqual(self.book_data_source.author(4), {'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817})

	def test_books_bad_author_id(self): 
		self.assertRaises(ValueError, self.book_data_source.author, author_id = -1)


	# test the method "def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year')"
	def test_find_authors_by_book_id(self):
		self.assertEqual(self.book_data_source.authors(book_id = 5), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])

	def test_find_authors_by_text(self):
		self.assertEqual(self.book_data_source.authors(search_text="Jane"), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])

	def test_find_authors_by_start_year(self):
		self.assertEqual(self.book_data_source.authors(start_year=1972), [{'id': 2, 'last_name': 'Jemisen', 'first_name': 'N.K.','birth_year': 1972, 'death_year': NULL}, 
			{'id': 3, 'last_name': 'Alderman', 'first_name': 'Naomi','birth_year': 1974, 'death_year': NULL}])

	def test_find_authors_by_end_year(self):
		self.assertEqual(self.book_data_source.authors(end_year=1812), [{'id': 7, 'last_name': 'Dickens', 'first_name': 'Charles','birth_year': 1812, 'death_year': 1870}, 
			{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])

	def test_find_authors_by_text_and_end_year(self):
		self.assertEqual(self.book_data_source.authors(search_text='Dickens', end_year=1812), [{'id': 7, 'last_name': 'Dickens', 'first_name': 'Charles','birth_year': 1812, 'death_year': 1870}])

	def test_find_authors_sort_by_last_name(self):
		self.assertEqual(self.book_data_source.authors(end_year=1812, sort_by="last_name"), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}, {'id': 7, 'last_name': 'Dickens', 'first_name': 'Charles','birth_year': 1812, 'death_year': 1870}])


	# test the method "def books_for_author(self, author_id)"
	def test_books_for_author_method(self):
		self.assertEqual(self.book_data_source.books_for_author(author_id = 5), [{'id': 6, 'title': 'Good Omens', 'publication_year': 1990}])


	# test the method "def authors_for_book(self, book_id)"
	def test_authors_for_book_method(self):
		self.assertEqual(self.book_data_source.authors_for_book(book_id = 5), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])


if __name__ == '__main__':
    unittest.main()
