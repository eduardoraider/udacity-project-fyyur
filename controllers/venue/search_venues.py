from flask import render_template, request
from server import app
from models.venue import Venue

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/venues/search', methods=['POST'])
def search_venues():
    # search for Hop should return "The Musical Hop".
    # search for "Music" should return "The Musical Hop" and
    # "Park Square Live Music & Coffee"

    search_term = request.form['search_term']
    result = Venue.query.filter(Venue.name.ilike('%' + search_term + '%'))

    response = {
        "count": result.count(),
        "data": result
    }
    return render_template('pages/search_venues.html', results=response,
                           search_term=request.form.get('search_term', ''))
