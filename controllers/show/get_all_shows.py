from flask import render_template
from server import app, db
from models.show import Show

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/shows')
def shows():
    # displays list of shows at /shows
    show_query = Show.query.options(db.joinedload(
        Show.venue), db.joinedload(Show.artist)).all()
    data = list(map(Show.show_details, show_query))
    return render_template('pages/shows.html', shows=data)
