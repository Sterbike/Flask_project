from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            fav_mob = request.form["fav_minecraft_mob"]
            fav_football_team = request.form["fav_football_team"]
            fav_food = request.form["fav_food"]
            fav_car = request.form["fav_car"]
            with sqlite3.connect("favorites.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Favorites (name, email, fav_minecraft_mob, fav_football_team, fav_food, fav_car) values (?,?,?,?,?,?)", (name, email, fav_mob, fav_football_team, fav_food, fav_car))
                con.commit()
                msg = "Person successfully Added"
        except:
            con.rollback()
            msg = "We can not add the person to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()


@app.route("/view")
def view():
    con = sqlite3.connect("favorites.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Favorites")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("favorites.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Favorites where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/updatedetails", methods=["POST"])
def updaterecord():
    msg = "msg"
    if request.method == "POST":
        try:
            id = request.form["id"]
            name = request.form["name"]
            email = request.form["email"]
            fav_minecraft_mob = request.form["fav_minecraft_mob"]
            fav_football_team = request.form["fav_football_team"]
            fav_food = request.form["fav_food"]
            fav_car = request.form["fav_car"]
            with sqlite3.connect("favorites.db") as con:
                cur = con.cursor()
                cur.execute("UPDATE Favorites SET name=?, email=?, fav_minecraft_mob=?, fav_football_team=?, fav_food=?, fav_car=? WHERE id=?", (name, email, fav_minecraft_mob, fav_football_team, fav_food, fav_car, id))
                con.commit()
                msg = "Datas successfully Updated"
        except:
            con.rollback()
            msg = "We can not update the person on the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

if __name__ == "__main__":
    app.run(debug=True)