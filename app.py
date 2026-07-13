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

@app.route("/animals/<int:id>", methods=["PUT"])
def update_animal(id):
 
    data = request.get_json()
 
    conn = sqlite3.connect("database.db")
 
    cur = conn.cursor()
 
    cur.execute(
        "UPDATE animals SET animal_id=?,name=?,species=?,breed=?,age=?,gender=?,status=? WHERE id=?",
        (
            data["animal_id"],
            data["name"],
            data["species"],
            data["breed"],
            data["age"],
            data["gender"],
            data["status"],
            id
        )
    )
 
    conn.commit()
 
    conn.close()
 
    return jsonify({"message":"Animal Updated"})
 

if __name__ == "__main__":
    app.run(debug=True, port=5000)


    