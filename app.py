from flask import Flask, render_template, request, url_for, redirect
from db import search_products, init_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/wheels")
def wheels():
    return render_template("wheels.html")

@app.route("/frame_sets")
def frame_sets():
    return render_template("frame_sets.html")

@app.route("/components")
def components():
    return render_template("components.html")

@app.route("/results/<product_type>", methods=["GET", "POST"])
def results(product_type):
    if request.method == "POST":
        search_query = request.form["search"]
        results = search_products(product_type, search_query)  # Update your search_products function to handle product_type
        return render_template(f"results_{product_type}.html", results=results)
    return redirect(url_for("home"))

@app.route("/back")
def back():
    return redirect(url_for("home"))

if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)
