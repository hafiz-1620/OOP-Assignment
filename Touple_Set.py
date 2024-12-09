# Initial data
books = (("To Kill a Mockingbird", "Harper Lee", 1960), 
         ("1984", "George Orwell", 1949), 
         ("The Great Gatsby", "F. Scott Fitzgerald", 1925))

tags = {"classic", "dystopian", "novel", "literature"}
print("Author of the second book:",books[1][1])

#add new book
new_book = ("Brave New World", "Aldous Huxley", 1932)
books = books + (new_book,)
print("Updated books tuple:", books)

# Unpack the details of the third book
third_book = books[2]  
third_title = third_book[0]
third_author = third_book[1]
third_year = third_book[2]
print("Third book details:")
print("Title:", third_title)
print("Author:", third_author)
print("Year:", third_year)

#loop in tags
print("Book titles:")
for book in books:
    print(book[0])
    
#add tags
tags.add("sci-fi")
print("Updated tags set:", tags)
#remove tags
tags.remove("novel") 
print("Tags set after removing 'novel':", tags)
