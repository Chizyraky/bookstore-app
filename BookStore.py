from tkinter import *
import sqlite3
from tkinter import ttk
from datetime import datetime

root = Tk()
root.title("XYZ Book Store Management")
root.geometry("1000x600+0+0")
space = Text(root)

# Creating a connection to the database
conn = sqlite3.connect('library.db')
# Create cursor
cur = conn.cursor()

# Calling the execute() method to create table and perform SQL commands
# Create table
cur.execute("""create table if not exists books (
            id integer PRIMARY KEY,
            title text,
            author text,
            year integer,
            isbn integer
)
""")


# Create Submit Function for database
def addEntry():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    # if():

    # Insert into database
    cur.execute("INSERT INTO books VALUES (NULL, :title, :author, :yr, :isbn)",
                {
                    'title': book_title.get(),
                    'author': author.get(),
                    'yr': yr.get(),
                    'isbn': isbn.get(),
                }
                )
    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()
    # Clear inputs from form
    book_title.delete(0, END)
    author.delete(0, END)
    yr.delete(0, END)
    isbn.delete(0, END)


def view_all():
    treev.delete(*treev.get_children())
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    # Query the database
    cur.execute("select * from books")
    records = cur.fetchall()

    for record in records:
        treev.insert('', 'end', values=record)

    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    selected_item = treev.item(treev.focus())
    delete_id = selected_item.get('values')[0]

    # Delete from database
    cur.execute("delete from books where id=?", (delete_id,))
    conn.commit()
    conn.close()
    view_all()


def search():
    treev.delete(*treev.get_children())

    select = callback()

    if select is 'id':
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        cur.execute("select * from books where id=?", (search_entry.get(),))
        results = cur.fetchall()
        for result in results:
            treev.insert('', 'end', values=result)
        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        sql = str('select * from books where ' + select + ' like (?)')
        cur.execute(sql, ("%" + search_entry.get() + "%",))
        results = cur.fetchall()
        for result in results:
            treev.insert('', 'end', values=result)
        conn.commit()
        conn.close()


def callback(*args):
    return variable.get()


# Create text boxes for the user entry
book_title = Entry(root, width=20)
book_title.grid(row=0, column=1, pady=10)
author = Entry(root, width=20)
author.grid(row=0, column=3, pady=10)
yr = Entry(root, width=20)
yr.grid(row=1, column=1, pady=10)
isbn = Entry(root, width=20)
isbn.grid(row=1, column=3, pady=10)
search_entry = Entry(root, width=70)
search_entry.grid(row=2, column=0, columnspan=1)

# Create text box labels
book_title_label = Label(root, text="Title")
book_title_label.grid(row=0, column=0, padx=30)
author_label = Label(root, text="Author")
author_label.grid(row=0, column=2, padx=30)
yr_label = Label(root, text="Year")
yr_label.grid(row=1, column=0, padx=30)
isbn_label = Label(root, text="ISBN")
isbn_label.grid(row=1, column=2, padx=30)
search_label = Label(root, text="Search by:")
search_label.grid(row=2, column=1, padx=30)

OptionList = [
    "id",
    "id",
    "title",
    "author",
    "year",
    "isbn"
]
option_frame = Frame(root, bd=1, bg='cyan')
option_frame.grid(row=2, column=2)
variable = StringVar(root)
variable.set('???')
opt = ttk.OptionMenu(option_frame, variable, *OptionList)
opt.config(width=10)
opt.pack(side="top")
option_select = 'id'
variable.trace("w", callback)

# Creating the execution buttons
view_all_btn = Button(root, text="View all", font=('arial', 10, 'bold'), width=15, command=view_all)
view_all_btn.grid(row=3, column=3)
search_entry_btn = Button(root, text="Search entry", font=('arial', 10, 'bold'), width=15, command=search)
search_entry_btn.grid(row=2, column=3)
add_entry_btn = Button(root, text="Add entry", font=('arial', 10, 'bold'), width=15, command=addEntry)
add_entry_btn.grid(row=5, column=3)
update_selected_btn = Button(root, text="Update Selected", font=('arial', 10, 'bold'), width=15)
update_selected_btn.grid(row=6, column=3)
delete_selected_btn = Button(root, text="Delete selected", font=('arial', 10, 'bold'), width=15, command=delete)
delete_selected_btn.grid(row=7, column=3)
close_btn = Button(root, text="Close", font=('arial', 10, 'bold'), width=15)
close_btn.grid(row=8, column=3)

# Adding the display label
data_entry_frame = Frame(root, bd=1, width=400, height=250, bg="cyan")
data_entry_frame.grid(row=3, rowspan=6, columnspan=3)

# frm = Frame(root)
treev = ttk.Treeview(data_entry_frame, selectmode='browse')
treev.pack(side='left', fill='x')
verscrlbar = ttk.Scrollbar(data_entry_frame,
                           orient="vertical",
                           command=treev.yview)
verscrlbar.pack(side='right', fill='y')
treev.configure(xscrollcommand=verscrlbar.set)
# Defining number of columns
treev["columns"] = ("0", "1", "2", "3", "4")
# Defining heading
treev['show'] = 'headings'
treev.column("0", width=10)

treev.heading(0, text="Id")
treev.heading(1, text="Title")
treev.heading(2, text="Author")
treev.heading(3, text="Year")
treev.heading(4, text="Isbn")

# Commit Changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
