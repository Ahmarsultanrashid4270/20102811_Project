# 20102811_Project
Animal Shelter Management System.


Introduction

The Animal Shelter Management System is a simple web application developed for a small animal shelter. The purpose of this system is to store and manage information about animals living in the shelter. Staff can add new animals, view existing records, update animal information, and delete records when required.

The application follows the CRUD (Create, Read, Update, Delete) concept and uses a web API for communication between the frontend and backend.

---

Objectives

- Store animal information.
- Add new animal records.
- View all animals.
- Update existing records.
- Delete animal records.

---

Technologies Used

- HTML
- JavaScript
- Python
- Flask
- SQLite

---

System Features

- Add Animal
- View Animal Records
- Update Animal Information
- Delete Animal Records

---

Database

Table Name: animals

Field| Description
id| Primary Key
animal_id| Animal ID
name| Animal Name
species| Animal Species
breed| Animal Breed
age| Animal Age
gender| Male or Female
status| Available or Adopted

---

Project Structure

myproject/
│── app.py
│── database.db
│── init_db.py
│── index.html
│── script.js

---

How to Run

1. Install Python.
2. Install Flask.

pip install flask

3. Create the database.

python init_db.py

4. Start the application.

python app.py

5. Open the application in your web browser.

---

CRUD Operations

Create

Add a new animal.

Read

Display all animal records.

Update

Modify animal information.

Delete

Remove an animal record.

---

Conclusion

This project demonstrates a simple information system for an animal shelter. It allows users to perform CRUD operations through a web interface while storing data in an SQLite database using a Flask REST API.

## References

I used the following resources while working on this project:
W3Schools - For Html Table Creation
https://www.w3schools.com/html/html_tables.asp
SQLite Tutorial - Insert Data: https://www.sqlitetutorial.net/sqlite-python/insert/
SQLite Tutorial - Creating Tables: https://www.sqlitetutorial.net/sqlite-python/creating-tables/
For Python Request Handling:
https://flask.palletsprojects.com/en/stable/quickstart/
