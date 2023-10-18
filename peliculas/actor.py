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
          """ SELECT first_name AS Nombre, last_name AS Apellido ,
           actor_id 
          FROM actor ORDER BY Nombre """ 

    ).fetchall()
    return render_template('actor/index.html', actors=actors)



@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    info_actor = db.execute( 
         """SELECT first_name, last_name FROM actor
         WHERE actor_id = ?;""", 
        (id,)).fetchone()
    
    peliculas = db.execute( 
        #aca hay que agregar 
         """ SELECT title, ac.film_id
         FROM film ac JOIN film_actor fia ON ac.film_id = fia.film_id  
         WHERE fia.actor_id = ?; """,
        (id,)).fetchall()
    



    return render_template('actor/detalle.html', info_actor=info_actor, peliculas=peliculas)


