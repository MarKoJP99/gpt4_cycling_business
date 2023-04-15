# Main application file that sets up the Flask app and routes


from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        search_query = request.form["search"]
        results = db.search_products(search_query)
        if results:
            return render_template("results.html", results=results)
        else:
            return render_template("no_results.html", search_query=search_query)
    return render_template("home.html")

@app.route("/back")
def back():
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)

