# 🔐 Authentication System using Django Backend

A secure and scalable user authentication system built with Django. This project demonstrates user registration, login, logout, session management, and authentication using Django's built-in authentication framework.

## 🚀 Features

- User Registration (Sign Up)
- User Login
- User Logout
- Password Hashing & Security
- Session-Based Authentication
- Form Validation
- Protected Routes
- Django Authentication Framework
- SQLite Database Support

## 🛠️ Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap (if used)

## 📂 Project Structure

```bash
Authentication-System-using-Django-Backend/
│
├── authentication/        # Authentication app
├── templates/             # HTML templates
├── static/                # CSS, JS, Images
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tanishq826/Authentication-System-using-Django-Backend-.git
cd Authentication-System-using-Django-Backend-
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 📸 Screenshots

### Login Page
<dev>
<img width="1919" height="976" alt="Screenshot 2026-06-11 182509" src="https://github.com/user-attachments/assets/e05b18fa-5d1f-4420-a042-5c66b5bee8d0" />
  
</dev>

## 🔒 Authentication Workflow

1. User registers with username and password.
2. Password is securely hashed before storage.
3. User logs in using valid credentials.
4. Django creates a session for authenticated users.
5. Protected pages are accessible only after login.
6. User can logout to terminate the session.

Django's built-in authentication system handles user verification and session management securely. :contentReference[oaicite:0]{index=0}

## 🎯 Learning Outcomes

Through this project, I learned:

- Django Authentication System
- User Session Management
- Form Handling
- URL Routing
- Django Models
- Template Rendering
- Security Best Practices

## 🔮 Future Improvements

- Password Reset via Email
- Email Verification
- JWT Authentication
- OAuth Login (Google/GitHub)
- User Profile Management
- Docker Deployment

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

## 📜 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

**Tanishq Saini**

- GitHub: https://github.com/tanishq826
- LinkedIn: (Add your LinkedIn profile)

⭐ If you found this project helpful, consider giving it a star!
