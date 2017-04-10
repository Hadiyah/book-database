from tkinter import *
from pymongo import MongoClient
from pprint import pprint


class Books:

    def __init__(self, master):
        frame = Frame(master,width=500,height=500)
        frame.pack()

        self.LABEL_book_title = Label(frame, text = "Book Title: ")
        self.LABEL_author = Label(frame, text = "Author: ")
        self.ENTRY_book_title = Entry(frame)
        self.ENTRY_author = Entry(frame)


        self.LABEL_book_title.grid(row=0, column=0, sticky=E)
        self.LABEL_author.grid(row=1, column=0,sticky=E)
        self.ENTRY_book_title.grid(row=0,column=1)        
        self.ENTRY_author.grid(row=1,column=1)

        self.addButton = Button(frame, text = "Add", command=self.add)
        self.addButton.grid(columnspan = 2)

        self.viewButton = Button(frame, text = "View", command=self.view)
        self.viewButton.grid(columnspan = 2)
        


    def add(self):
        title = self.ENTRY_book_title.get()
        author = self.ENTRY_author.get()
        added_books = [{"Title":title, "Author":author}]
        result = coll.insert_many(added_books)
        print([{title}])

    def view(self):
        for book in data:
            print (book['Title'])



root = Tk()

client = MongoClient()
db=client.myBooks
coll = db.books
data = coll.find({})


print (coll.count())

b = Books(root)
root.mainloop()






