# Books Phase 1 Homework
#     @author Yuting Su(suy@carelton.edu)
#     @author Starr Wang(wangy3@carleton.edu)
#      2018-09-18

import csv
import sys

if(len(sys.argv) < 3):
	print("Please use the correct format: python3 books1.py input-file action [sort-direction]")

title=[]
year=[]
authors=[]
author_without_year=[]


with open(sys.argv[1]) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        title.append(row[0])
        year.append(row[1])
        authors.append(row[2])

    title.sort()
    year.sort()

    #remove the year from the author list
    for author in authors:
        if ("and" in author):
            author1, author2 = author.split("and ")
            # print(author1)
            # print(author2)
            authors.append(author1)
            authors.append(author2)
        else:
            new_author = ""
            for letter in author:
                if (letter != '('):
                    new_author = new_author + letter
                else:
                    break
            new_author = new_author[:-1]
            if not (new_author in author_without_year):
                author_without_year.append(new_author)

    #sort the author list by last name
    author_without_year.sort(key=lambda s: s.split()[1])

    if (len(sys.argv) == 3):
        content = sys.argv[2]
        if (content == "authors"):
            for i in author_without_year:
                print(i)
        elif (content == "books"):
            for i in title:
                print(i)
        else:
            print("Please use the correct format: python3 books1.py input-file action [sort-direction]")

    elif (len(sys.argv) == 4):
        content = sys.argv[2]
        direction = sys.argv[3]
        if (content == "authors" and direction == "forward"):
            for i in author_without_year:
                print(i)
        elif (content == "authors" and direction == "reverse"):
            for i in reversed(author_without_year):
                print(i)
        elif (content == "books" and direction == "forward"):
            for i in title:
                print(i)
        elif (content == "books" and direction == "reverse"):
            for i in reversed(title):
                print(i)        
        else:
            print("Please use the correct format: python3 books1.py input-file action [sort-direction]")

    elif (len(sys.argv) > 4):
        print("Please use the correct format: python3 books1.py input-file action [sort-direction]")
  
