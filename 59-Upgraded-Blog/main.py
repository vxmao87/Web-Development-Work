import requests
from flask import Flask, render_template

# Initializes the Flask server
app = Flask(__name__)

posts = requests.get(url="https://api.npoint.io/8c650484aa193ca1b103").json()

@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def get_post(index):
    wanted_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            wanted_post = blog_post
    return render_template("post.html", current_post=wanted_post)

# Replaces 'flask --app hello run' so that you can use the Play and Stop buttons on PyCharm.
# Add 'debug=True' inside the parameter to auto-reload the server whenever you save your work.
if __name__ == "__main__":
    app.run(debug=True)
