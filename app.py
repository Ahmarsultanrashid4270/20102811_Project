from flask import Flask, request, jsonify
import sqlite3
 
app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.route("/animals", methods=["GET"])
def get_animals():
 
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
 
    cur = conn.cursor()
 
    cur.execute("SELECT * FROM animals")
 
    rows = cur.fetchall()
 
    conn.close()
 
    data = []
 
    for row in rows:
 
        data.append({
            "id": row["id"],
            "animal_id": row["animal_id"],
            "name": row["name"],
            "species": row["species"],
            "breed": row["breed"],
            "age": row["age"],
            "gender": row["gender"],
            "status": row["status"]
        })
 
    return jsonify(data)