import booksdatasource
# import books
# import authors
# import books_authors
import unittest


class BooksDataSourceTest(unittest.TestCase):
	def setUp(self):
		self.book_data_source=booksdatasource.BooksDataSource("books.csv", "authors.csv", "books_authors.csv")

	def tearDown(self):
		pass

	def test_find_book_by_id(self):
		self.assertEqual(self.book(6), {'id': 6, 'title': 'Good Omens', 'publication_year': 1990})

	def test_find_books_by_author(self):
		self.assertEqual(self.books(author_id = 5), [{'id': 6, 'title': 'Good Omens', 'publication_year': 1990}])

	def test_find_books_by_text(self):
		self.assertEqual(self.books(search_text="good"), [{'id': 6, 'title': 'Good Omens', 'publication_year': 1990}])

	def test_find_books_by_start_year(self):
		self.assertEqual(self.books(start_year=2010), [{'id': 3, 'title': 'All Clear', 'publication_year': 2010}, {'id': 9, 'title': 'Blackout', 'publication_year': 2010}])

	def test_find_books_by_end_year(self):
		self.assertEqual(self.books(end_year=1813), [{'id': 19, 'title': 'Pride and Prejudice', 'publication_year': 1813}, {'id': 21, 'title': 'Sense and Sensibility', 'publication_year': 1813}, {'id': 31, 'title': 'The Life and Opinions of Tristram', 'publication_year': 1759}])

	def test_find_books_sorted_by_year(self):
		self.assertEqual(self.books(end_year=1813, sort_by="year"), [{'id': 31, 'title': 'The Life and Opinions of Tristram', 'publication_year': 1759}, {'id': 19, 'title': 'Pride and Prejudice', 'publication_year': 1813}, {'id': 21, 'title': 'Sense and Sensibility', 'publication_year': 1813}])


	def test_find_author_by_id(self):
		self.assertEqual(self.author(4), {'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817})

	def test_find_authors_by_book_id(self):
		self.assertEqual(self.authors(book_id = 5), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])

	def test_find_authors_by_text(self):
		self.assertEqual(self.authors(search_text="Jane"), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])

	def test_find_authors_by_start_year(self):
		self.assertEqual(self.authors(start_year=1972), [{'id': 2, 'last_name': 'Jemisen', 'first_name': 'N.K.','birth_year': 1972, 'death_year': NULL}, 
			{'id': 3, 'last_name': 'Alderman', 'first_name': 'Naomi','birth_year': 1974, 'death_year': NULL}])

	def test_find_authors_by_end_year(self):
		self.assertEqual(self.authors(end_year=1812), [{'id': 7, 'last_name': 'Dickens', 'first_name': 'Charles','birth_year': 1812, 'death_year': 1870}, 
			{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])

	def test_find_authors_sort_by_last_name(self):
		self.assertEqual(self.authors(end_year=1812, sort_by="last_name"), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}, {'id': 7, 'last_name': 'Dickens', 'first_name': 'Charles','birth_year': 1812, 'death_year': 1870}])


	def test_books_for_author_method(self):
		self.assertEqual(self.books_for_author(author_id = 5), [{'id': 6, 'title': 'Good Omens', 'publication_year': 1990}])


	def test_authors_for_book_method(self):
		self.assertEqual(self.authors_for_book(book_id = 5), [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])


if __name__ == '__main__':
    unittest.main()
