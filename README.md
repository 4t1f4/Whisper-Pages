# 🌸 Whisper Pages

A soft, elegant, and secure digital diary built with Flask.

🌐 **Live Demo:** https://whisper-pages.onrender.com

Whisper Pages is a personal journaling application where users can create an account, write private diary entries, revisit memories, edit existing entries, and manage their profile through a calm and aesthetically pleasing interface.

The project was built while learning Flask, backend development, authentication systems, databases, application structure, deployment, and data security.

---

## ✨ Features

### Authentication

* User Registration
* User Login
* User Logout
* Password Hashing with Flask-Bcrypt
* Session Management with Flask-Login
* Protected Routes
* Authentication Feedback using Flash Messages

### Diary Management

* Create New Diary Entries
* View Entry Details
* Edit Existing Entries
* Delete Entries
* Entry History Page
* Personal Dashboard

### Security

* Password Hashing with Bcrypt
* Diary Entry Encryption using Fernet
* Environment Variable Based Secret Management
* Protected User Routes
* User Data Isolation

### User Profile

* View Profile Information
* Personalized User Experience
* Restricted Access for Authenticated Users

### Database

* PostgreSQL (Neon)
* SQLAlchemy ORM
* Database Migrations with Flask-Migrate and Alembic

### User Experience

* Soft Pastel UI Theme
* Glassmorphism Design
* Responsive Layout
* Animated Ambient Background
* Interactive Visual Effects
* Custom Typography

---

## 🛠 Tech Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-Login
* Flask-Bcrypt
* Cryptography (Fernet Encryption)
* PostgreSQL
* Alembic

### Frontend

* HTML
* CSS
* JavaScript
* Jinja2 Templates

### Deployment & Tools

* Git
* GitHub
* VS Code
* Render
* Neon PostgreSQL

---

## 📂 Project Structure

```text
Whisper-Pages/
│
├── run.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── migrations/
│
├── app/
│   │
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── crypto.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── entry.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── diary/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── profile/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── templates/
│   │   ├── auth/
│   │   ├── diary/
│   │   ├── profile/
│   │   ├── base.html
│   │   └── index.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       │
│       └── js/
│           └── main.js
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/4t1f4/Whisper-Pages.git
cd Whisper-Pages
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
ENCRYPTION_KEY=your_fernet_key
```

Run database migrations:

```bash
flask db upgrade
```

Start the application:

```bash
python run.py
```

Visit:

```text
http://127.0.0.1:5000
```

---

## 🔒 Security

Whisper Pages uses multiple layers of security:

### Password Protection

User passwords are hashed using Flask-Bcrypt before being stored in the database.

### Diary Encryption

All diary entries are encrypted using Fernet encryption before being stored in PostgreSQL.

This means:

* Database administrators cannot read diary contents directly.
* Raw database records contain encrypted text instead of readable entries.
* Entries are automatically decrypted only when viewed by the authenticated owner.

### Environment Variables

Sensitive information such as:

* SECRET_KEY
* DATABASE_URL
* ENCRYPTION_KEY

is stored using environment variables instead of hardcoded values.

---

## ☁️ Deployment

Whisper Pages is deployed using:

* Render (Web Hosting)
* Neon PostgreSQL (Database)

The application automatically deploys from GitHub whenever changes are pushed to the main branch.

---

## 📖 Learning Objectives

This project helped explore:

* Flask Application Factory Pattern
* Blueprints
* Authentication & Authorization
* SQLAlchemy ORM
* Database Relationships
* Database Migrations
* Session Management
* Jinja Templates
* Project Organization
* Git & GitHub Workflow
* PostgreSQL Integration
* Cloud Deployment with Render
* Environment Variables
* Data Encryption with Fernet

---

## 🌷 Future Improvements

* Password Reset System
* Entry Search
* Entry Categories & Tags
* Rich Text Editor
* Dark Mode
* User Settings
* Entry Favorites
* Profile Editing
* Email Verification
* REST API
* Automated Tests
* Docker Support
* User Profile Pictures

---

## 💜 About

Whisper Pages was created as a learning project while exploring Flask and backend development.

The goal was not only to build a functional diary application, but also to create a peaceful writing experience through thoughtful design, secure data handling, and user-friendly interactions.

Building this project provided hands-on experience with authentication systems, database design, deployment workflows, cloud databases, and encryption techniques used in real-world web applications.
