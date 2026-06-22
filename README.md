# 🌸 Whisper Pages

A soft, elegant, and secure digital diary built with Flask.

🌐 **Live Demo:** https://whisper-pages.onrender.com

Whisper Pages is a personal journaling application where users can create an account, write private diary entries, revisit memories, edit existing entries, and manage their profile through a calm and aesthetically pleasing interface.

The project was built while learning Flask, backend development, authentication systems, databases, and application structure.

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
git clone https://github.com/noturs06/Whisper-Pages.git
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

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
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

---

## 💜 About

Whisper Pages was created as a learning project while exploring Flask and backend development.

The goal was not only to build a functional diary application, but also to create a peaceful writing experience through thoughtful design and user-friendly interactions.
