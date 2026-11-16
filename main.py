from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field
import sqlite3


# Database connection
def get_connection():
    connection = sqlite3.connect("student.db")
    return connection


# Create student table
def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    q = """
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        marks INTEGER,
        course TEXT,
        image TEXT,
        status INTEGER
    )
    """

    cursor.execute(q)
    connection.commit()
    connection.close()


create_table()


# Jinja2 templates
templates = Jinja2Templates(directory="templates")


# Pydantic model
class Student(BaseModel):
    name: str = Field(min_length=3, max_length=25)
    age: int = Field(ge=18, le=60)
    gender: str
    marks: int = Field(ge=1, le=100)
    course: str
    image: str
    status: int


# FastAPI application
app = FastAPI()


# Display all students
@app.get("/")
def home(req: Request):

    connection = get_connection()
    cursor = connection.cursor()

    q = "SELECT * FROM students"

    cursor.execute(q)
    students = cursor.fetchall()

    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"stds": students}
    )


# View single student
@app.get("/student/{std_id}")
def single_std(req: Request, std_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    q = "SELECT * FROM students WHERE id=?"

    cursor.execute(q, (std_id,))
    student = cursor.fetchone()

    connection.close()

    if student is None:
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse(
        request=req,
        name="single-std.html",
        context={"std": student}
    )


# Delete student
@app.post("/std/delete/{std_id}")
def std_delete(std_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    q = "DELETE FROM students WHERE id=?"

    cursor.execute(q, (std_id,))

    connection.commit()
    connection.close()

    return RedirectResponse(url="/", status_code=303)


# Display add student page
@app.get("/students/add")
def create_student(req: Request):

    return templates.TemplateResponse(
        request=req,
        name="add-student.html",
        context={}
    )


# Add new student
@app.post("/students/add")
def create_std(
    name: str = Form(),
    age: int = Form(),
    gender: str = Form(),
    marks: int = Form(),
    course: str = Form(),
    image: str = Form(),
    status: int = Form()
):

    std_obj = Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )

    values = (
        std_obj.name,
        std_obj.age,
        std_obj.gender,
        std_obj.marks,
        std_obj.course,
        std_obj.image,
        int(bool(std_obj.status))
    )

    connection = get_connection()
    cursor = connection.cursor()

    q = """
    INSERT INTO students(
        name, age, gender, marks, course, image, status
    )
    VALUES(?,?,?,?,?,?,?)
    """

    cursor.execute(q, values)

    connection.commit()
    connection.close()

    return RedirectResponse(url="/", status_code=303)


# Display edit student page
@app.get("/student/edit/{std_id}")
def edit_std(req: Request, std_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    q = "SELECT * FROM students WHERE id=?"

    cursor.execute(q, (std_id,))
    student = cursor.fetchone()

    connection.close()

    if student is None:
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse(
        request=req,
        name="update-std.html",
        context={"std": student}
    )


# Update student details
@app.post("/student/edit/{std_id}")
def update_std(
    std_id: int,
    name: str = Form(),
    age: int = Form(),
    marks: int = Form(),
    gender: str = Form(),
    course: str = Form(),
    image: str = Form(),
    status: int = Form()
):

    std_obj = Student(
        name=name,
        age=age,
        marks=marks,
        gender=gender,
        course=course,
        image=image,
        status=status
    )

    connection = get_connection()
    cursor = connection.cursor()

    q = """
    UPDATE students
    SET name=?,
        age=?,
        marks=?,
        gender=?,
        course=?,
        image=?,
        status=?
    WHERE id=?
    """

    cursor.execute(
        q,
        (
            std_obj.name,
            std_obj.age,
            std_obj.marks,
            std_obj.gender,
            std_obj.course,
            std_obj.image,
            int(bool(std_obj.status)),
            std_id
        )
    )

    connection.commit()
    connection.close()

    return RedirectResponse(url="/", status_code=303)