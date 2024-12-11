# Login-and-registration-using-python-and-json

---

# **Login & Registration System**

## **Overview**

The **Login & Registration System** is a Python-based desktop application that enables users to register and log into their accounts using a simple yet secure authentication process. This system is built using **Tkinter** for the graphical user interface (GUI) and **hashlib** for securely hashing passwords with **SHA-256**.

This project offers a lightweight, user-friendly login and registration system with clear feedback for actions like successful logins, invalid credentials, or already existing users.

---

## **Key Features**

- **User Registration**: Allows users to create a new account by entering a unique username and password.
- **Secure Password Handling**: Passwords are hashed using the **SHA-256** algorithm, making them secure before being saved.
- **Login System**: Users can log into the system with their username and hashed password.
- **JSON Database**: User data (username and hashed passwords) is stored locally in a **JSON** file.
- **Modern GUI**: A visually appealing interface designed with **Tkinter** and enhanced by **ttkthemes**.
- **User-Friendly Error Handling**: Clear messages are displayed for common issues like empty fields, incorrect credentials, or existing usernames.
- **Clean and Intuitive Design**: Simple navigation between registration and login frames.

---

## **Technologies Used**

- **Python**: The primary programming language for building the application.
- **Tkinter**: A Python library used for building the graphical user interface (GUI).
- **ttkthemes**: Provides modern and attractive themes for the Tkinter GUI components.
- **hashlib**: Used for hashing user passwords securely with the **SHA-256** algorithm.
- **json**: Handles storing and retrieving user data (username and hashed passwords) in a **JSON file**.

---

## **Installation and Setup**

Follow the steps below to set up the **Login & Registration System** on your local machine.

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/your-username/Login-Registration-System.git
cd Login-Registration-System
```

### **Step 2: Create a Virtual Environment (Optional but Recommended)**

Creating a virtual environment isolates the dependencies of your project.

```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
```

### **Step 3: Install Required Dependencies**

Use the following command to install all the necessary libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

**requirements.txt** includes:
- `tkinter`
- `ttkthemes`
- `hashlib`

### **Step 4: Run the Application**

After installing dependencies, run the following command to launch the application:

```bash
python main.py
```

The application window will open, allowing you to use the login and registration system.

---

## **How to Use the Application**

Once the application is running, you will see the main window with two options: **Login** and **Register**.

### **Registration Process**:

1. Click on the **Register** button.
2. Enter a **username** and **password** in the corresponding fields.
3. Click on **Register** to create your account.
4. If the username is already taken, you will see an error message. Otherwise, a confirmation message will pop up, indicating successful registration.

### **Login Process**:

1. Click on the **Login** button.
2. Enter your **username** and **password** in the respective fields.
3. Click on **Login** to log into your account.
4. If the credentials are correct, you will be welcomed with a success message. Otherwise, an error message will inform you that the username or password is invalid.

### **Switch Between Registration and Login Screens**:

- You can easily navigate between the **Login** and **Registration** screens using the provided buttons.

---

## **How the System Works**

### **Registration Process**
- When a new user registers, the application checks whether the username already exists.
- If the username doesn't exist, the password entered by the user is hashed using the **SHA-256** algorithm.
- The username and hashed password are then saved in a local **JSON** file.
- The user is redirected to the login screen after a successful registration.

### **Login Process**
- When a user tries to log in, the application fetches the stored user data from the **JSON** file.
- The entered password is hashed, and the system checks if the **username** and **hashed password** match any existing user data.
- If the credentials are correct, the user is logged in. Otherwise, an error message is displayed.

### **Password Hashing**
- The password is hashed using the **SHA-256** hashing algorithm, which ensures that sensitive user data (passwords) is not stored in plain text.
- This makes the system secure as hashed passwords cannot be easily retrieved or cracked.

---

## **Folder Structure**

The repository follows a simple folder structure:

```
📦 Login-Registration-System
├── 📂 users.json           # Stores user data (username and hashed password)
├── 📄 main.py              # Main application code
├── 📄 requirements.txt     # Required libraries for the project
└── 📄 README.md            # Project documentation (this file)
```

### **users.json**

This file contains the user data in JSON format, where each entry is an object containing a `username` and a `password` (hashed).

Example content of `users.json`:

```json
[
  {
    "username": "user1",
    "password": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  }
]
```

---

## **Detailed Code Explanation**

### **Key Functions**

| **Function**               | **Description**                                                  |
|----------------------------|------------------------------------------------------------------|
| `register_user()`           | Handles the registration process, checks for duplicate usernames, and saves the new user data. |
| `login_user()`              | Handles the login process, validates entered credentials against stored data. |
| `hash_password()`           | Hashes the password using **SHA-256** for secure storage.        |
| `load_users()`              | Loads the list of users from the `users.json` file.             |
| `save_users()`              | Saves the user data (username and hashed password) to `users.json`. |
| `clear_registration_fields()` | Clears the registration form after submission.               |
| `clear_login_fields()`      | Clears the login form after submission.                         |
| `show_frame()`              | Switches between the registration and login screens.            |
| `create_styled_frame()`     | Creates a styled frame for both the login and registration screens. |
| `create_styled_button()`    | Creates a styled button with customizable options.              |

### **Graphical User Interface (GUI)**

The application uses **Tkinter** to create an intuitive graphical interface with the following components:
- **Entry widgets** for username and password inputs.
- **Labels** for instructions and error messages.
- **Buttons** for actions like login, registration, and switching screens.
- **Frames** for organizing the layout of the login and registration sections.

### **Error Handling**

The system provides informative feedback for the following scenarios:
- **Empty fields**: If any field (username or password) is empty, an error message prompts the user to complete the form.
- **Username already exists**: During registration, if the username is already in the database, an error message is shown.
- **Invalid login credentials**: If the username or password is incorrect, a message alerts the user.

---

## **Troubleshooting**

**Issue**: Application does not start.  
**Solution**: Make sure all dependencies are installed by running `pip install -r requirements.txt`. Also, ensure that you are using a supported version of Python (preferably Python 3.x).

**Issue**: The login credentials are invalid even though the user exists.  
**Solution**: Double-check that you are using the correct username and password. Remember that passwords are hashed, so ensure you have entered the correct password.

**Issue**: The **users.json** file does not exist or is empty.  
**Solution**: If the `users.json` file is missing or empty, the application will automatically create and populate it after a successful registration.

---

## **Future Enhancements**

This project can be expanded with additional features:

- **Password Strength Validation**: Implement a password strength checker during registration to encourage users to choose secure passwords.
- **Password Reset**: Add a "Forgot Password" feature that allows users to reset their passwords via email or security questions.
- **Profile Management**: Allow users to edit their profiles and change their passwords after login.
- **Database Upgrade**: Transition from using a JSON file to a more robust database system like **SQLite** for scalability and reliability.

---

## **Contributing**

We welcome contributions! If you would like to contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request and describe your changes.

---

## **License**

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## **Author**

- **GitHub**: [your-username](https://github.com/your-username)
- **Email**: [sameerymeshram.com](mailto:sameerymeshram.com)

--- 

