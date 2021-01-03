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
def index():
    user = session["user"]

    return render_template("index.html", user=user)


def get_filters():
    # help from:
    # https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
    class Filters:
        def __init__(self):
            # default is no filtering
            self.user = []
            self.url = []
            self.all = []

    output = Filters()

    # if a user is logged in and has safe search on, get their allergens
    username = session.get("user")
    safe_search = session.get("safe_search")
    if username and safe_search:
        user = mongo.db.users.find_one({"username": username})
        output.user = user["allergen_name"]

    # if url filter parameters are set
    url_params = request.args.get("filter")
    if url_params:
        output.url = url_params.split('-')

    if output.user:
        output.all += output.user
    if output.url:
        output.all += output.url

    return output


@app.route("/recipes")
def recipes():
    cat = mongo.db.categories.find()

    return render_template(
        "categories.html", categories=cat)


@app.route("/recipes/<category>")
def recipes_cat(category):
    allergens = mongo.db.allergens.find()

    # check category exists and is valid
    cat = mongo.db.categories.find_one({"category": category})
    if not cat:
        return redirect(url_for("recipes"))

    filters = get_filters()
    recipes = mongo.db.recipes.find({
        "category": category,
        "allergen_name": {"$nin": filters.all}
    })

    username = session.get("user")
    safe_search = session.get("safe_search")

    return render_template(
        "recipes.html", recipes=recipes, allergens=allergens,
        filters=filters.url, user_allergens=filters.user,
        safe_search=safe_search, username=username,
        category=cat)


@app.route("/recipes/all")
def all_recipes():
    allergens = mongo.db.allergens.find()

    filters = get_filters()
    recipes = mongo.db.recipes.find({"allergen_name": {"$nin": filters.all}})

    username = session.get("user")
    safe_search = session.get("safe_search")

    return render_template(
        "recipes.html", recipes=recipes, allergens=allergens,
        filters=filters.url, user_allergens=filters.user,
        safe_search=safe_search, username=username)


@app.route("/register", methods=["GET", "POST"])
def register():

    username = session.get("user")
    if username:
        return redirect(url_for('index'))

    allergens = mongo.db.allergens.find()
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        allergens = request.form.getlist("allergen_name")

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "allergen_name": allergens
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        # default to safe search being on
        session["safe_search"] = True

        flash("Registration successfull")
        return redirect(url_for("recipes", username=session["user"]))

    return render_template("register.html", allergens=allergens)


@app.route("/login", methods=["GET", "POST"])
def login():

    username = session.get("user")
    if username:
        return redirect(url_for('index'))

    if request.method == "POST":
        # check if user already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:

            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                # default to safe search being on
                session["safe_search"] = True
                flash("Welcome, {}!".format(request.form.get("username")))
                return redirect(url_for("recipes"))
            else:
                # invalid password match
                flash("Incorrect username or password")
                return redirect(url_for('login'))

        else:
            # username does not exist
            flash("Incorrect username or password")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/my_recipes")
def my_recipes():
    # from session user, get username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    my_recipes = mongo.db.recipes.find({"created_by": session["user"]})

    return render_template("my_recipes.html", username=username,
                           recipes=my_recipes)


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
        flash("You can only edit your own recipes!")
        return redirect(url_for("my_recipes"))


@app.route("/delete_recipe/<recipes_id>")
def delete_recipe(recipes_id):

    # from session user, get username from db
    user = mongo.db.users.find_one({"username": session["user"]})
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    if user["username"] == recipe["created_by"]:
        mongo.db.recipes.remove({"_id": ObjectId(recipes_id)})
        flash("Recipe successfully deleted")
    else:
        flash("You can only delete your own recipes!")

    return redirect(url_for("my_recipes"))


@app.route("/show_recipe/<recipes_id>", methods=["GET"])
def show_recipe(recipes_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    ingredients = recipes.get("ingredients").split(',')
    methods = recipes.get("method").split(',')
    referrer = request.referrer

    return render_template(
        "/show_recipe.html", recipes=recipes, ingredients=ingredients,
        methods=methods, referrer=referrer)


@app.route("/safe_search", methods=["POST"])
def safe_search():

    enabled = request.form.get("safe-search-enabled")

    username = session.get("user")
    if username:
        session["safe_search"] = enabled

    # Redirect to current page, taken from here:
    # https://stackoverflow.com/a/58367071
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
