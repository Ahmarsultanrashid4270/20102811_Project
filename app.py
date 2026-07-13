from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


# Main HTML page
@app.route("/")
def home():
    return render_template("index.html")


# CORS
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


# Add animal
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

    return jsonify({"message": "Animal Added"})


# Get animals
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


# Update animal
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

    return jsonify({"message": "Animal Updated"})


# Delete animal
@app.route("/animals/<int:id>", methods=["DELETE"])
def delete_animal(id):

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM animals WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Animal Deleted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)