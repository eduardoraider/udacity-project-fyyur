from flask import render_template
from server import app, db
from models.artist import Artist
from models.venue import Venue
from models.show import Show
from datetime import datetime
# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
    # shows the artist page with the given artist_id

    artist = Artist.query.get(artist_id)

    current_time = datetime.now().strftime('%Y-%m-%d %H:%S:%M')

    past_shows_query = db.session.query(Show).join(Venue).filter(
        Show.artist_id == artist_id).filter(
        Show.start_time < current_time).all()
    past_shows = list(map(Show.show_venue_details, past_shows_query))

    upcoming_shows_query = db.session.query(Show).join(Venue).filter(
        Show.artist_id == artist_id).filter(
        Show.start_time >= current_time).all()
    upcoming_shows = list(map(Show.show_venue_details, upcoming_shows_query))

    data = artist.to_dict()
    data['past_shows'] = past_shows
    data['upcoming_shows'] = upcoming_shows
    data['past_shows_count'] = len(past_shows)
    data['upcoming_shows_count'] = len(upcoming_shows)

    return render_template('pages/show_artist.html', artist=data)
