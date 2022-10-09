from flask import render_template, request
from server import app
from models.artist import Artist

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/artists/search', methods=['POST'])
def search_artists():
    # search for "A" should return "Guns N Petals", "Matt Quevado",
    # and "The Wild Sax Band".
    # search for "band" should return "The Wild Sax Band".

    search_term = request.form['search_term']
    result = Artist.query.filter(Artist.name.ilike('%' + search_term + '%'))

    response = {
        "count": result.count(),
        "data": result
    }

    return render_template('pages/search_artists.html', results=response,
                           search_term=request.form.get('search_term', ''))
