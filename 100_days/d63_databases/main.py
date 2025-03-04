from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# all_books = []

# create database
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'

# create the extension
db = SQLAlchemy(model_class=Base)
# Initialize the app with extension
db.init_app(app)

# create table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # optional : allow each book to be identified by its title
    def __repr__(self):
        return f'<Book {self.title}>'


# create table schema in database
with app.app_context():
    db.create_all()


# # create record
# with app.app_context():
#     new_book = Book(id=1, title='Harry PoOTER', author='J.K Rowling', rating=9.23)
#     db.session.add(new_book)
#     db.session.commit()


@app.route('/')
def home():
    ##READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Book).order_by(Book.title))

    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title = request.form["title"],
            author = request.form["author"],
            rating = request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")

@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()

        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)

    return render_template("edit.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)

    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

