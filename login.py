import tkinter as tk
from tkinter import messagebox
import mysql.connector
import webbrowser
import app


app()
# Function to insert user data into the database
def insert_user(first_name, last_name, username, email, password):
    try:
        cn = mysql.connector.connect(host="localhost",user="root",password="atharva",database="space")
        cr = cn.cursor()
        sql_query = "INSERT INTO customers(first_name, last_name, username, email, password) VALUES (%s, %s, %s, %s, %s)"
        cr.execute(sql_query, (first_name, last_name, username, email, password))
        cn.commit()
        print("User  registered successfully")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

# Registration function
def register():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # Validate inputs
    if not all([first_name, last_name, username, email, password, confirm_password]):
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    # Insert user data into the database
    insert_user(first_name, last_name, username, email, password)
    messagebox.showinfo("Success", "Registration successful! Please log in.")

    # Open login window
    open_login_window()


# Function to open the login window
def open_login_window():
    global entry_login_username, entry_login_password
    login_window = tk.Toplevel(r)
    login_window.title("Login")

    label_login_username = tk.Label(login_window, text="Username:")
    label_login_username.pack()
    entry_login_username = tk.Entry(login_window)
    entry_login_username.pack()

    label_login_password = tk.Label(login_window, text="Password:")
    label_login_password.pack()
    entry_login_password = tk.Entry(login_window, show='*')
    entry_login_password.pack()

    button_login = tk.Button(login_window, text="Login", command=login)
    button_login.pack()


# Login function
def login():
    username = entry_login_username.get()
    password = entry_login_password.get()

    # Connect to MySQL database to validate login
    try:
        cn = mysql.connector.connect(
            host='localhost',
            database='space',
            user='atharva',
            password='atharva'
        )
        cr = cn.cursor()
        cr.execute("SELECT * FROM customers WHERE username=%s AND password=%s", (username, password))
        result = cr.fetchone()

        if result:
            messagebox.showinfo("Login", "Login successful!")
            webbrowser.open('')  # Redirect to your HTML page
            r.quit()  # Close the main Tkinter window
        else:
            messagebox.showerror("Login", "Invalid username or password")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

# Create the main window
r = tk.Tk()
r.title("Registration Form")

# Create labels and entry fields for registration
label_first_name = tk.Label(r, text="First Name:")
label_first_name.pack()
entry_first_name = tk.Entry(r)
entry_first_name.pack()

label_last_name = tk.Label(r, text="Last Name:")
label_last_name.pack()
entry_last_name = tk.Entry(r)
entry_last_name.pack()

label_username = tk.Label(r, text="Username:")
label_username.pack()
entry_username = tk.Entry(r)
entry_username.pack()

label_email = tk.Label(r, text="Email:")
label_email.pack()
entry_email = tk.Entry(r)
entry_email.pack()

label_password = tk.Label(r, text="Password:")
label_password.pack()
entry_password = tk.Entry(r, show='*')
entry_password.pack()

label_confirm_password = tk.Label(r, text="Confirm Password:")
label_confirm_password.pack()
entry_confirm_password = tk.Entry(r, show='*')
entry_confirm_password.pack()

button_register = tk.Button(r, text="Register", command=register)
button_register.pack()

# Run the application
r.mainloop()