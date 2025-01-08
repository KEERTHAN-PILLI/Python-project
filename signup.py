from tkinter import *
from tkinter import messagebox
import pymysql

# Function to validate the sign-up form
def validate_signup():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    
    if not username or not password or not confirm_password:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    if password != confirm_password:
        messagebox.showerror("Password Error", "Passwords do not match!")
        return
    
    # Connect to the MySQL database
    try:
        con = pymysql.connect(host="localhost", user="root", password="admin", database="db")
        cur = con.cursor()
        
        # Check if the username already exists
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cur.fetchone()
        
        if existing_user:
            messagebox.showwarning("Username Error", "Username already exists!")
        else:
            # Insert new user into the database
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            con.commit()
            messagebox.showinfo("Sign Up Successful", "You have successfully signed up!")
            signup_window.destroy()  # Close the sign-up window
            root.deiconify()  # Reopen the login page

        con.close()

    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")

# Function to open the sign-up page
def open_signup_page():
    global signup_window
    root.withdraw()  # Hide the login window
    signup_window = Toplevel(root)
    signup_window.title("Sign Up Page")
    signup_window.geometry("400x400")  # Set window size

    # Heading
    heading_label = Label(signup_window, text="Create a New Account", font=("Arial", 16))
    heading_label.pack(pady=20)

    # Username Entry
    label_username = Label(signup_window, text="Username:")
    label_username.pack(pady=5)
    global entry_username
    entry_username = Entry(signup_window, width=30)
    entry_username.pack(pady=5)

    # Password Entry
    label_password = Label(signup_window, text="Password:")
    label_password.pack(pady=5)
    global entry_password
    entry_password = Entry(signup_window, width=30, show="*")  # Mask the password with asterisks
    entry_password.pack(pady=5)

    # Confirm Password Entry
    label_confirm_password = Label(signup_window, text="Confirm Password:")
    label_confirm_password.pack(pady=5)
    global entry_confirm_password
    entry_confirm_password = Entry(signup_window, width=30, show="*")  # Mask the confirm password with asterisks
    entry_confirm_password.pack(pady=5)

    # Sign Up Button
    btn_signup = Button(signup_window, text="Sign Up", bg="green", fg="white", command=validate_signup)
    btn_signup.pack(pady=20)

    # Back Button
    def go_back_to_login():
        signup_window.destroy()
        root.deiconify()  # Show the login window again

    btn_back = Button(signup_window, text="Back to Login", bg="gray", fg="white", command=go_back_to_login)
    btn_back.pack()

# Function to validate login credentials (already in `login.py`)
def validate_login():
    username = entry_username_login.get()
    password = entry_password_login.get()
    
    try:
        con = pymysql.connect(host="localhost", user="root", password="admin", database="db")
        cur = con.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cur.execute(query, (username, password))
        user = cur.fetchone()
        
        if user:
            messagebox.showinfo("Login Successful", "Welcome to the Digital Library!")
            root.destroy()  # Close login window
            open_main_page()  # Open the main page
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")
        
        con.close()
    
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")

# Function to open the main library page (already in `login.py`)
def open_main_page():
    try:
        import main  # Import the main library page here
        main.main()  # Call the main function of your library
    except ImportError as e:
        messagebox.showerror("Import Error", "Error opening main page: {0}".format(str(e)))

# Initialize Tkinter login window
root = Tk()
root.title("Login Page")
root.geometry("400x300")  # Set window size

# Heading
heading_label = Label(root, text="Login to Digital Library", font=("Arial", 16))
heading_label.pack(pady=20)

# Username Entry
label_username_login = Label(root, text="Username:")
label_username_login.pack(pady=5)
entry_username_login = Entry(root, width=30)
entry_username_login.pack(pady=5)

# Password Entry
label_password_login = Label(root, text="Password:")
label_password_login.pack(pady=5)
entry_password_login = Entry(root, width=30, show="*")  # Mask the password with asterisks
entry_password_login.pack(pady=5)

# Login Button
btn_login = Button(root, text="Login", bg="blue", fg="white", command=validate_login)
btn_login.pack(pady=10)

# Sign Up Button
btn_signup = Button(root, text="Sign Up", bg="green", fg="white", command=open_signup_page)
btn_signup.pack()

# Run the login window
root.mainloop()
