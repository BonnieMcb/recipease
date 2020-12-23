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
    allergens = mongo.db.allergens.find()

    # default is no filtering
    user_filter = None
    url_filter = None

    # if a user is logged in, get their allergens
    username = session.get("user")
    if username:
        user = mongo.db.users.find_one({"username": username})
        user_filter = user["allergen_name"]

    # if url filter parameters are set
    url_params = request.args.get("filter")
    if url_params:
        url_filter = url_params.split('-')

    filter = []
    if user_filter:
        filter += user_filter
    if url_filter:
        filter += url_filter

    recipes = mongo.db.recipes.find({"allergen_name": {"$nin": filter}})

    return render_template(
        "recipes.html", recipes=recipes, allergens=allergens)


@app.route("/register", methods=["GET", "POST"])
def register():
    allergens = mongo.db.allergens.find()
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # sanitise user input allergen name for matching, with help from:
        # https://stackoverflow.com/a/19562453/14135937
        allergen_name = request.form.getlist("allergen_name")
        allergens = [''.join(x.split()).lower() for x in allergen_name]

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "allergen_name": allergens
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successfull")
        return redirect(url_for("favourites", username=session["user"]))

    return render_template("register.html", allergens=allergens)


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
    allergens = mongo.db.allergens.find().sort("allergen_name", 1)
    return render_template(
        "/add_recipe.html", categories=categories, allergens=allergens)


@app.route("/edit_recipe/<recipes_id>", methods=["GET", "POST"])
def edit_recipe(recipes_id):
    # from session user, get username from db
    user = mongo.db.users.find_one({"username": session["user"]})
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})

    if user["username"] == recipe["created_by"]:

        if request.method == "POST":
            recipe_edit = {
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
            print(recipe_edit)
            mongo.db.recipes.update({"_id": ObjectId(recipes_id)}, recipe_edit)
            flash("Recipe successfully updated!")
            return redirect(url_for("my_recipes"))

        recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
        categories = mongo.db.categories.find().sort("category", 1)
        allergens = mongo.db.allergens.find()

        return render_template(
            "/edit_recipe.html", recipes=recipes, categories=categories,
            allergens=allergens)

    else:
        flash("You can only edit your own recipes")
        return redirect(url_for("my_recipes"))


@app.route("/delete_recipe/<recipes_id>")
def delete_recipe(recipes_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipes_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("my_recipes"))


@app.route("/show_recipe/<recipes_id>", methods=["GET"])
def show_recipe(recipes_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    ingredients = recipes.get("ingredients").split(',')
    methods = recipes.get("method").split(',')
    return render_template(
        "/show_recipe.html", recipes=recipes, ingredients=ingredients,
        methods=methods)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)