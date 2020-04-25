from tkinter import *
import sqlite3
import random
import tkinter.messagebox
from tkinter import ttk
from datetime import datetime

root = Tk()
root.title("Library Management")
root.geometry("1000x600+0+0")
space = Text(root)

# Creating a connection to the database
conn = sqlite3.connect('library.db')
# Create cursor
cur = conn.cursor()

# Calling the execute() method to create table and perform SQL commands
# Create table
# cur.execute("""create table books (
#             title text,
#             author text,
#             year integer,
#             isbn integer
# )
# """)

# Create text boxes for the user entry
book_title = Entry(root, width=20)
book_title.grid(row=0, column=1, pady=10)
author = Entry(root, width=20)
author.grid(row=0, column=3, pady=10)
yr = Entry(root, width=20)
yr.grid(row=1, column=1, pady=10)
isbn = Entry(root, width=20)
isbn.grid(row=1, column=3, pady=10)

# Create text box labels
book_title_label = Label(root, text="Title")
book_title_label.grid(row=0, column=0, padx=30)
author_label = Label(root, text="Author")
author_label.grid(row=0, column=2, padx=30)
yr_label = Label(root, text="Year")
yr_label.grid(row=1, column=0, padx=30)
isbn_label = Label(root, text="ISBN")
isbn_label.grid(row=1, column=2, padx=30)

# Creating the execution buttons
view_all_btn = Button(root, text="View all", font=('arial', 10, 'bold'), width=15)
view_all_btn.grid(row=2, column=6)
search_entry_btn = Button(root, text="Search entry", font=('arial', 10, 'bold'), width=15)
search_entry_btn.grid(row=3, column=6)
add_entry_btn = Button(root, text="Add entry", font=('arial', 10, 'bold'), width=15)
add_entry_btn.grid(row=4, column=6)
update_selected_btn = Button(root, text="Update Selected", font=('arial', 10, 'bold'), width=15)
update_selected_btn.grid(row=5, column=6)
delete_selected_btn = Button(root, text="Delete selected", font=('arial', 10, 'bold'), width=15)
delete_selected_btn.grid(row=6, column=6)

# Adding the display label
data_entry_frame = Frame(root, bd=1, width=400, height=200, bg="cyan")
data_entry_frame.grid(row=2, column=0)

close_btn = Button(root, text="Close", font=('arial', 10, 'bold'), width=15)
close_btn.grid(row=7, column=6)
# Commit Changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
