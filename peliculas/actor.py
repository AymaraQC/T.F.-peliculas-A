from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('actor',__name__, url_prefix="/actor/")


@bp.route('/')
def index():
    db = get_db()
    actors = db.execute(
          """ SELECT first_name AS Nombre, last_name AS Apellido FROM actor ORDER BY Nombre """ 

    ).fetchall()
    return render_template('actor/index.html', actors=actors)