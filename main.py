import tkinter as tk
from tkinter import ttk, messagebox
import json
import hashlib
from ttkthemes import ThemedTk
import os

# --- Configuration and Styling ---
DATABASE_FILE = "users.json"
THEME = "arc"  # You can change the theme to suit your style ('plastik', 'equinox', etc.)
FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 14, "bold")
PADDING = (15, 10)
WIDTH = 500
HEIGHT = 700

# --- Advanced Helper Functions ---
def load_users():
    """Load users from the database file."""
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as f:
            json.dump([], f)
    with open(DATABASE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_users(users):
    """Save users to the database file."""
    with open(DATABASE_FILE, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# --- User Interaction Functions ---
def register_user():
    """Handle user registration."""
    username = entry_username_reg.get().strip()
    password = entry_password_reg.get().strip()

    # Validate input
    if not username or not password:
        lbl_message_reg.config(text="Please fill in all fields.", foreground="red")
        return

    users = load_users()

    # Check if username already exists
    if any(user["username"] == username for user in users):
        lbl_message_reg.config(text="Username already exists.", foreground="red")
        return

    hashed_password = hash_password(password)
    new_user = {"username": username, "password": hashed_password}
    users.append(new_user)
    save_users(users)

    messagebox.showinfo("Success", "Registration successful! You can now log in.")
    clear_registration_fields()
    show_login_frame()

def login_user():
    """Handle user login."""
    username = entry_username_login.get().strip()
    password = entry_password_login.get().strip()

    # Validate input
    if not username or not password:
        lbl_message_login.config(text="Please fill in all fields.", foreground="red")
        return

    users = load_users()
    hashed_password = hash_password(password)

    # Check if username and password match
    user = next((user for user in users if user["username"] == username and user["password"] == hashed_password), None)

    if user:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        clear_login_fields()
    else:
        lbl_message_login.config(text="Invalid username or password.", foreground="red")

# --- UI Setup ---
root = ThemedTk(theme=THEME)
root.title("Login & Registration System")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

# Set the background and frame styling
style = ttk.Style()
style.configure("TLabel", font=FONT)
style.configure("TButton", font=BUTTON_FONT, padding=PADDING)
style.configure("TEntry", font=FONT, padding=5)
style.configure("RoundedFrame.TFrame", relief="raised", borderwidth=3, background="#ffffff")
style.configure("Title.TLabel", font=("Helvetica", 24, "bold"), foreground="#2c3e50")
style.configure("Message.TLabel", foreground="red", font=("Helvetica", 10))
style.configure("Accent.TButton", foreground="white", background="#3498db", font=("Helvetica", 14, "bold"))
style.map("Accent.TButton", background=[("active", "#2980b9")])
style.configure("Success.TButton", foreground="white", background="#2ecc71", font=("Helvetica", 12, "bold"))
style.map("Success.TButton", background=[("active", "#27ae60")])

# --- Helper Functions ---
def create_styled_frame(parent, style_name="TFrame"):
    """Create a styled frame."""
    frame = ttk.Frame(parent, style=style_name)
    return frame

def create_styled_button(parent, text, command, style_name="TButton", **kwargs):
    """Create a styled button."""
    button = ttk.Button(parent, text=text, command=command, style=style_name, **kwargs)
    return button

# --- Frame Management ---
def show_frame(frame):
    """Show a specific frame."""
    frame.tkraise()

def show_register_frame():
    """Switch to the registration frame."""
    show_frame(frame_register)

def show_login_frame():
    """Switch to the login frame."""
    show_frame(frame_login)

# --- Frames and Layout ---
frame_login = create_styled_frame(root, "RoundedFrame.TFrame")
frame_register = create_styled_frame(root, style_name="RoundedFrame.TFrame")

# --- Login Frame Widgets ---
lbl_title_login = ttk.Label(frame_login, text="Login", style="Title.TLabel")
lbl_title_login.grid(row=0, column=0, columnspan=2, pady=(40, 10))

lbl_message_login = ttk.Label(frame_login, text="", style="Message.TLabel")
lbl_message_login.grid(row=1, column=0, columnspan=2, pady=(0, 10))

ttk.Label(frame_login, text="Username", font=("Helvetica", 12)).grid(row=2, column=0, sticky=tk.W, padx=30, pady=(20, 5))
entry_username_login = ttk.Entry(frame_login, width=30, font=("Helvetica", 12))
entry_username_login.grid(row=2, column=1, pady=(0, 10), padx=(5, 30), sticky=tk.E)

ttk.Label(frame_login, text="Password", font=("Helvetica", 12)).grid(row=3, column=0, sticky=tk.W, padx=30, pady=(0, 5))
entry_password_login = ttk.Entry(frame_login, show="*", font=("Helvetica", 12))  # Password entry
entry_password_login.grid(row=3, column=1, pady=(0, 10), padx=(5, 30), sticky=tk.E)

btn_login = create_styled_button(frame_login, text="Login", command=login_user, style_name="Accent.TButton")
btn_login.grid(row=4, column=0, columnspan=2, pady=(20, 20))

btn_to_register = create_styled_button(frame_login, text="Don't have an account? Register", command=show_register_frame, style_name="Success.TButton")
btn_to_register.grid(row=5, column=0, columnspan=2, pady=(10, 30))

# --- Registration Frame Widgets ---
lbl_title_reg = ttk.Label(frame_register, text="Register", style="Title.TLabel")
lbl_title_reg.grid(row=0, column=0, columnspan=2, pady=(40, 10))

lbl_message_reg = ttk.Label(frame_register, text="", style="Message.TLabel")
lbl_message_reg.grid(row=1, column=0, columnspan=2, pady=(0, 10))

ttk.Label(frame_register, text="Username", font=("Helvetica", 12)).grid(row=2, column=0, sticky=tk.W, padx=30, pady=(20, 5))
entry_username_reg = ttk.Entry(frame_register, font=("Helvetica", 12))
entry_username_reg.grid(row=2, column=1, pady=(0, 10), padx=(5, 30), sticky=tk.E)

ttk.Label(frame_register, text="Password", font=("Helvetica", 12)).grid(row=3, column=0, sticky=tk.W, padx=30, pady=(0, 5))
entry_password_reg = ttk.Entry(frame_register, show="*", font=("Helvetica", 12))
entry_password_reg.grid(row=3, column=1, pady=(0, 10), padx=(5, 30), sticky=tk.E)

btn_register = create_styled_button(frame_register, text="Register", command=register_user, style_name="Accent.TButton")
btn_register.grid(row=4, column=0, columnspan=2, pady=(20, 20))

btn_to_login = create_styled_button(frame_register, text="Already have an account? Login", command=show_login_frame, style_name="Success.TButton")
btn_to_login.grid(row=5, column=0, columnspan=2, pady=(10, 30))

# --- Clear Entry Functions ---
def clear_registration_fields():
    """Clear registration form fields."""
    entry_username_reg.delete(0, tk.END)
    entry_password_reg.delete(0, tk.END)

def clear_login_fields():
    """Clear login form fields."""
    entry_username_login.delete(0, tk.END)
    entry_password_login.delete(0, tk.END)

# Show the login frame by default when the app starts
show_login_frame()

# Start the Tkinter event loop
root.mainloop()
