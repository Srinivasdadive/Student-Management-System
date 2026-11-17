# 🎓 Student Management System

A web-based **Student Management System** developed using Python, FastAPI, SQLite, HTML, and CSS. This application helps manage student records efficiently through a simple and user-friendly interface.

## 🚀 Features

- **Create:** Add new student records with details.
- **Read:** View all registered students.
- **View Details:** Display individual student information.
- **Update:** Edit and update existing student records.
- **Delete:** Remove student records from the database.
- **Data Validation:** Validate student information using Pydantic.
- **Database Management:** Store and manage student information using SQLite.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| FastAPI | Web Framework |
| SQLite | Database |
| HTML5 | Web Page Structure |
| CSS3 | Styling and Layout |
| Jinja2 | HTML Templating |
| Pydantic | Data Validation |

## 📂 Project Structure

```text
Student-Management-System/
│
├── templates/
│   ├── home.html
│   ├── add-student.html
│   ├── single-std.html
│   └── update-std.html
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Srinivasdadive/Student-Management-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Student-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

### 7. Open in Browser

Visit:

```text
http://127.0.0.1:8000
```

## 🗄️ Database

This project uses SQLite to store student information.

Student records include:

- Student ID
- Name
- Age
- Gender
- Marks
- Course
- Image
- Status

The database table is automatically created when the application starts.

## 🎯 Project Objectives

- Understand FastAPI fundamentals.
- Implement CRUD operations.
- Connect Python applications with SQLite.
- Work with HTML forms and Jinja2 templates.
- Implement data validation using Pydantic.
- Develop a complete web application.

## 👨‍💻 Developer

**Srinivas Dadive**

B.Tech Graduate | Python Full Stack Developer (Learning)

GitHub: [Srinivasdadive](https://github.com/Srinivasdadive)

---

⭐ If you find this project useful, consider giving it a star!
