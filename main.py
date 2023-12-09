from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog-posts.db"
db = SQLAlchemy()
db.init_app(app)


class blogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False, nullable=False)
    post = db.Column(db.String, unique=False, nullable=False)


with app.app_context():
    db.create_all()

with app.app_context():
    blog_post = blogPost(title="Day 1", post="Some random content")
    db.session.add(blog_post)
    blog_post = blogPost(title="Day 2", post="Some random content")
    db.session.add(blog_post)
    blog_post = blogPost(title="Day 3", post="Some random content")
    db.session.add(blog_post)
    blog_post = blogPost(title="Day 4", post="Some random content")
    db.session.add(blog_post)
    db.session.commit()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/historicalposts')
def historicalposts():
    posts = db.session.execute(db.select(blogPost).order_by(blogPost.id))
    a = posts.scalars().all()
    return render_template("histroicalposts.html", posts=a)

@app.route('/about')
def about():
    return render_template("aboutme.html")


if __name__ == "__main__":
    app.run(debug=True)