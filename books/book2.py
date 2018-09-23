import csv
import sys

links_dictionary = []

with open("books_authors.csv") as csvfile:
    spamreader = csv.reader(csvfile)
    id = 1
    for row in spamreader:
        link = {'book_id': row[0], 'author_id': row[1]}
        id = id+1
        links_dictionary.append(link)
print(links_dictionary)



