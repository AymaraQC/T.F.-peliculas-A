from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    peliculas = db.execute(
         """SELECT f.title, f.release_year, l.name AS idioma FROM film f JOIN language l
            ON f.language_id = l.language_id
            ORDER BY title """
        #"""SELECT f.title, f.release_year, "ingles" AS idioma 
        #FROM film f ORDER BY title """
    ).fetchall()
    return render_template('pelis/index.html', peliculas=peliculas)

# def get_post(id):
#     post = get_db().execute(
#         'SELECT p.id, title, body, created, author_id, username'
#         ' FROM post p JOIN user u ON p.author_id = u.id'
#         ' WHERE p.id = ?',
#         (id,)
#     ).fetchone()

#     if post is None:
#         abort(404, f"Post id {id} doesn't exist.")

#     return post