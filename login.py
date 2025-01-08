from tkinter import *
from tkinter import messagebox
import pymysql

# Function to validate login credentials
def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Connect to the MySQL database
    try:
        con = pymysql.connect(host="localhost", user="root", password="admin", database="db")
        cur = con.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cur.execute(query, (username, password))
        user = cur.fetchone()
        
        if user:
            # If user is found, login is successful
            messagebox.showinfo("Login Successful", "Welcome to the Digital Library!")
            root_login.destroy()  # Close login window
            open_main_page()  # Open the main page of the library
        else:
            # If user not found, show error message
            messagebox.showerror("Login Failed", "Incorrect username or password.")
        
        con.close()
    
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")

# Function to open the main library page
def open_main_page():
    try:
        import main  # Import the main library page here
        main.main()  # Call the main function of your library (assumes you have a `main()` function in `main.py`)
    except ImportError as e:
        messagebox.showerror("Import Error", "Error opening main page: {0}".format(str(e)))

# Initialize Tkinter window for login
root_login = Tk()
root_login.title("Login Page")
root_login.geometry("400x300")  # Set window size

# Heading
heading_label = Label(root_login, text="Login to Digital Library", font=("Arial", 16))
heading_label.pack(pady=20)

# Username Entry
label_username = Label(root_login, text="Username:")
label_username.pack(pady=5)
entry_username = Entry(root_login, width=30)
entry_username.pack(pady=5)

# Password Entry
label_password = Label(root_login, text="Password:")
label_password.pack(pady=5)
entry_password = Entry(root_login, width=30, show="*")  # Mask the password with asterisks
entry_password.pack(pady=5)

# Login Button
btn_login = Button(root_login, text="Login", bg="blue", fg="white", command=validate_login)
btn_login.pack(pady=20)

# Run the login window
root_login.mainloop()
