from tkinter import *
from tkinter import messagebox
import pymysql
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# Function to open the main library page
def main():
    try:
        # Connect to the MySQL database
        con = pymysql.connect(host="localhost", user="root", password="admin", database="db")
        cur = con.cursor()
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"Error connecting to the database:\n{e}")
        return

    # Initialize Tkinter window for the main library page
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Heading Frame
    headingFrame1 = Frame(root, bg="#cf5e13", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to\nDigital Library", bg='white', fg='black', font=('Rockwell Extra Bold', 25))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Buttons for features
    btn1 = Button(root, text="Add Book Details", bg='blue', fg='white', command=addBook)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)
    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
    btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
    btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

    # Start Tkinter loop
    root.mainloop()
