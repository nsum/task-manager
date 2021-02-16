import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# ObjectId is imported because mongo stores data in JSON like
# format called bson
from werkzeug.security import generate_password_hash, check_password_hash
# We import above to enable user registration
if os.path.exists("env.py"):
    import env


# Create instance of flask
app = Flask(__name__)

# Grab database name
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Configure connection string
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Grab SECRET_KEY
app.secret_key = os.environ.get("SECRET_KEY")
# Add instane of pymongo
# app in brackets is app object we created above (instance of Flask)
mongo = PyMongo(app)


# / refers to default route
@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = mongo.db.tasks.find()
    return render_template("tasks.html", tasks= tasks)
    # 1st task is what tamplate will use and that = 2nd tasks we created (var)


# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check is username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
