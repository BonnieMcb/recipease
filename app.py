import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    allergen = mongo.db.allergen.find()
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "allergen_name": request.form.getlist("allergen_name")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successfull")
        return redirect(url_for("favourites", username=session["user"]))

    return render_template("register.html", allergen=allergen)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if user already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "favourites", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect username or password")
                return redirect(url_for('login'))

        else:
            # username does not exist
            flash("Incorrect username or password")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/favourites", methods=["GET", "POST"])
def favourites():
    # from session user, get username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("favourites.html", username=username)

    return redirect(url_for("login"))


@app.route("/my_recipes")
def my_recipes():
    # from session user, get username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    my_recipes = mongo.db.recipes.find({"created_by": session["user"]})

    return render_template("my_recipes.html", recipes=my_recipes)


@app.route("/logout")
def logout():
    # remove the user from the session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("recipes"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category": request.form.get("category"),
            "recipe_name": request.form.get("recipe_name"),
            "servings": request.form.get("servings"),
            "time": request.form.get("time"),
            "allergen_name": request.form.getlist("allergen_name[]"),
            "image": request.form.get("image"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        print(recipe)
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added!")
        return redirect(url_for("recipes"))

    categories = mongo.db.categories.find().sort("category", 1)
    allergen = mongo.db.allergen.find().sort("allergen_name", 1)
    return render_template(
        "/add_recipe.html", categories=categories, allergen=allergen)


@app.route("/edit_recipe/<recipes_id>", methods=["GET", "POST"])
def edit_recipe(recipes_id):
    if request.method == "POST":
        recipe = {
            "category": request.form.get("category"),
            "recipe_name": request.form.get("recipe_name"),
            "servings": request.form.get("servings"),
            "time": request.form.get("time"),
            "allergen_name": request.form.getlist("allergen_name[]"),
            "image": request.form.get("image"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        print(recipe)
        mongo.db.recipes.update({"_id": ObjectId(recipes_id)}, recipe)
        flash("Recipe successfully updated!")
        return redirect(url_for("my_recipes"))
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    print(recipes)

    categories = mongo.db.categories.find().sort("category", 1)
    allergen = list(mongo.db.allergen.find())
    print(allergen)
    return render_template(
        "/edit_recipe.html", recipes=recipes, categories=categories,
        allergen=allergen)


@app.route("/delete_recipe/<recipes_id>")
def delete_recipe(recipes_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipes_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("my_recipes"))


@app.route("/show_recipe/<recipes_id>", methods=["GET"])
def show_recipe(recipes_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    return render_template(
        "/show_recipe.html", recipes=recipes,)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)