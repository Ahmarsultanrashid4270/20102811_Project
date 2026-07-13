from flask import Flask, request, jsonify
import sqlite3
 
app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response



@app.route("/animals", methods=["POST"])
def add_animal():
 
    data = request.get_json()
 
    conn = sqlite3.connect("database.db")
 
    cur = conn.cursor()
 
    cur.execute(
        "INSERT INTO animals(animal_id,name,species,breed,age,gender,status) VALUES(?,?,?,?,?,?,?)",
        (
            data["animal_id"],
            data["name"],
            data["species"],
            data["breed"],
            data["age"],
            data["gender"],
            data["status"]
        )
    )
 
    conn.commit()
 
    conn.close()
 
    return jsonify({"message":"Animal Added"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    