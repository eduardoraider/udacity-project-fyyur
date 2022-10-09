from flask import render_template
from server import app, db
from models.venue import Venue
from models.show import Show
from datetime import datetime

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
    # shows the venue page with the given venue_id

    venue = Venue.query.get(venue_id)

    current_time = datetime.now().strftime('%Y-%m-%d %H:%S:%M')

    past_shows_query = db.session.query(Show).join(Venue).filter(
        Show.venue_id == venue_id).filter(
        Show.start_time < current_time).all()
    past_shows = list(map(Show.show_artist_details, past_shows_query))

    upcoming_shows_query = db.session.query(Show).join(Venue).filter(
        Show.venue_id == venue_id).filter(
        Show.start_time >= current_time).all()
    upcoming_shows = list(map(Show.show_artist_details, upcoming_shows_query))

    data = venue.to_dict()
    data['past_shows'] = past_shows
    data['upcoming_shows'] = upcoming_shows
    data['past_shows_count'] = len(past_shows)
    data['upcoming_shows_count'] = len(upcoming_shows)

    return render_template('pages/show_venue.html', venue=data)
