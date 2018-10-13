# Books Phase 3 Homework
#     @author Yuting Su(suy@carelton.edu)
#     @author Starr Wang(wangy3@carleton.edu)
#      2018-09-20

import csv
import sys

class BooksDataSource:
    '''
    A BooksDataSource object provides access to data about books and authors.
    The particular form in which the books and authors are stored will
    depend on the context (i.e. on the particular assignment you're
    working on at the time).

    Most of this class's methods return Python lists, dictionaries, or
    strings representing books, authors, and related information.

    An author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    For example, Jane Austen would be represented like this
    (assuming her database-internal ID number is 72):

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}

    For a living author, the death_year is represented in the author's
    Python dictionary as None.

        {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.

    A book is represented as a dictionary with the keys 'id', 'title',
    and 'publication_year'. For example, "Pride and Prejudice"
    (assuming an ID of 132) would look like this:

        {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

    '''

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        self.books_dictionary = self.create_books_dictionary(books_filename)
        self.authors_dictionary = self.create_authors_dictionary(authors_filename)
        self.links_dictionary = self.create_links_dictionary(books_authors_link_filename)
        ''' Initializes this data source from the three specified  CSV files, whose
            CSV fields are:

                books: ID,title,publication-year
                  e.g. 6,Good Omens,1990
                       41,Middlemarch,1871
                    

                authors: ID,last-name,first-name,birth-year,death-year
                  e.g. 5,Gaiman,Neil,1960,NULL
                       6,Pratchett,Terry,1948,2015
                       22,Eliot,George,1819,1880

                link between books and authors: book_id,author_id
                  e.g. 41,22
                       6,5
                       6,6
                  
                  [that is, book 41 was written by author 22, while book 6
                    was written by both author 5 and author 6]

            Note that NULL is used to represent a non-existent (or rather, future and
            unknown) year in the cases of living authors.

            NOTE TO STUDENTS: I have not specified how you will store the books/authors
            data in a BooksDataSource object. That will be up to you, in Phase 3.
        '''
        pass

    def create_books_dictionary(self, books_filename):
        books_dictionary = []

        with open(books_filename) as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                book_information = {'id': int(row[0]), 'title': row[1] , 'publication_year': row[2]}
                books_dictionary.append(book_information)
        return books_dictionary

    def create_authors_dictionary(self, authors_filename):
        authors_dictionary = []

        with open(authors_filename) as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                author_information = {'id': int(row[0]), 'last_name': row[1], 'first_name': row[2],'birth_year': row[3], 'death_year': row[4]}
                authors_dictionary.append(author_information)
        return authors_dictionary

    def create_links_dictionary(self, books_authors_link_filename):
        links_dictionary = []

        with open(books_authors_link_filename) as csvfile:
            spamreader = csv.reader(csvfile)
            id = 1
            for row in spamreader:
                link = {'book_id': int(row[0]), 'author_id': int(row[1])}
                id = id+1
                links_dictionary.append(link)
        return links_dictionary

    def book(self, book_id):
        for book in self.books_dictionary:
            if book["id"] == book_id:
                return (book)
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.) '''
        raise ValueError('could not find the book with this id')

    def find_book_id_from_author_id(self, author_id):
        book_id_list = []
        for link in self.links_dictionary:
            if int(link["author_id"]) == author_id:
                book_id_list.append(int(link["book_id"]))
        return book_id_list

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):

        if (author_id!=None and int(author_id)<0 or start_year!=None and int(start_year)<0 or end_year!=None and int(end_year)<0):
            raise ValueError('the input should not be a negative number')

        return_books_list = []
        if (author_id!=None):
            book_id_list = self.find_book_id_from_author_id(author_id)
            for book_id in book_id_list:
                book = self.book(book_id)
                return_books_list.append(book)

        if (start_year!=None):

            #if the return_books_list is not empty, remove the books item in the list whose 
            #public year is before start year. 
            if return_books_list:
                for book in return_books_list:
                    if book["publication_year"] and int(book["publication_year"]) < int(start_year):
                        return_books_list.remove(book)

            #otherwise, add books whose publish year is after the start yeat
            #to the return_book_list
            else:
                for book in self.books_dictionary:
                    if book["publication_year"] and int(book["publication_year"]) >= int(start_year):
                        return_books_list.append(book)

        if (end_year!=None):

            if return_books_list:
                for book in return_books_list:
                    if book["publication_year"] and int(book["publication_year"]) > int(end_year):
                        return_books_list.remove(book)


            else:
                for book in self.books_dictionary:
                    if book["publication_year"] and int(book["publication_year"]) <= int(end_year):
                        return_books_list.append(book)

        if (search_text!=None):

            if return_books_list:
                for book in return_books_list:
                    if book["title"].lower().find(search_text.lower()) == -1:
                        return_books_list.remove(book)

            else:
                for book in self.books_dictionary:
                    if book["title"].lower().find(search_text.lower()) != -1:
                        return_books_list.append(book)

        return_books_list.sort(key=lambda item:item['title'])

        if (sort_by == "year"):
            return_books_list.sort(key=lambda item:item["publication_year"])

        return return_books_list
                
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year
                
            See the BooksDataSource comment for a description of how a book is represented.
        '''
        return []

    def author(self, author_id):
        for author in self.authors_dictionary:
            if int(author["id"]) == int(author_id):
                return (author)
        raise ValueError('could not find the author with this id')

    def find_author_id_from_book_id(self, book_id):
        for link in self.links_dictionary:
            if int(link["book_id"]) == int(book_id):
                return link["author_id"]
        raise ValueError('sorry could not find the author_id with this id')

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):

        if (book_id!=None and int(book_id)<0 or start_year!=None and int(start_year)<0 or end_year!=None and int(end_year)<0):
            raise ValueError('the input should not be a negative number')

        return_authors_list = []
        if (book_id!=None):
            author_id = self.find_author_id_from_book_id(book_id)
            author = self.author(author_id)
            return_authors_list.append(author)

        if (start_year!=None):
            #if the return_books_list is not empty, remove the books item in the list whose 
            #public year is before start year. 
            if return_authors_list:
                for author in return_authors_list:
                    if str(author["death_year"]) <= str(start_year):
                        return_authors_list.remove(author)

            #otherwise, add books whose publish year is after the start yeat
            #to the return_book_list
            else:
                for author in self.authors_dictionary:
                    if str(author["death_year"]) > str(start_year) or author["death_year"] == "NULL":
                        return_authors_list.append(author)

        if (end_year!=None):
            #if the return_books_list is not empty, remove the books item in the list whose 
            #public year is before start year. 
            if return_authors_list:
                for author in return_authors_list:
                    if str(author["death_year"]) > str(end_year) or author["death_year"] == "NULL":
                        return_authors_list.remove(author)

            #otherwise, add books whose publish year is after the start yeat
            #to the return_book_list
            else:
                for author in self.authors_dictionary:
                    if author["death_year"]!="NULL" and str(author["death_year"]) <= str(end_year):
                        return_authors_list.append(author)

        if (search_text!=None):

            if return_authors_list:
                for author in return_authors_list:
                    if author["first_name"].lower().find(search_text.lower()) == -1 and author["last_name"].lower().find(search_text.lower()) == -1:
                        return_authors_list.remove(author)

            else:
                for author in self.authors_dictionary:
                    if author["first_name"].lower().find(search_text.lower()) != -1 or author["last_name"].lower().find(search_text.lower()) != -1:
                        return_authors_list.append(author)

        return_authors_list.sort(key=lambda item:(item['last_name'], item['first_name'], item["birth_year"]))

        if (sort_by == "birth_year"):
            return_authors_list.sort(key=lambda item:(item["birth_year"],item["last_name"], item["first_name"]))

        return return_authors_list
        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.

                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year

            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.

            The list of authors is sorted in an order depending on the sort_by parameter:

                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year
        
            See the BooksDataSource comment for a description of how an author is represented.
        '''


    # Note for my students: The following two methods provide no new functionality beyond
    # what the books(...) and authors(...) methods already provide. But they do represent a
    # category of methods known as "convenience methods". That is, they provide very simple
    # interfaces for a couple very common operations.
    #
    # A question for you: do you think it's worth creating and then maintaining these
    # particular convenience methods? Is books_for_author(17) better than books(author_id=17)?

    def books_for_author(self, author_id):
        ''' Returns a list of all the books written by the author with the specified author ID.
            See the BooksDataSource comment for a description of how an book is represented. '''
        return self.books(author_id=author_id)

    def authors_for_book(self, book_id):
        ''' Returns a list of all the authors of the book with the specified book ID.
            See the BooksDataSource comment for a description of how an author is represented. '''
        return self.authors(book_id=book_id)

newbooksdatasource = BooksDataSource(books_filename="books.csv", authors_filename="authors.csv", books_authors_link_filename="books_authors.csv")
output=newbooksdatasource.books(search_text="we", start_year="2000")
print(output)