from flask import render_template
from server import app
from models.venue import Venue
from models.show import Show
from datetime import datetime

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/venues')
def venues():
    #  num_upcoming_shows should be aggregated based on number of
    # upcoming shows per venue.

    current_time = datetime.now().strftime('%Y-%m-%d %H:%S:%M')
    venues = Venue.query.group_by(Venue.id, Venue.state, Venue.city).all()
    venue_state_and_city = ''
    data = []

    for venue in venues:
        upcoming_shows = venue.shows.filter(
            Show.start_time > current_time).all()

        if venue_state_and_city == venue.city + venue.state:
            data[len(data) - 1]["venues"].append({
                "id": venue.id,
                "name": venue.name,
                "num_upcoming_shows": len(upcoming_shows)
            })
        else:
            venue_state_and_city == venue.city + venue.state
            data.append({
                "city": venue.city,
                "state": venue.state,
                "venues": [{
                    "id": venue.id,
                    "name": venue.name,
                    "num_upcoming_shows": len(upcoming_shows)
                }]
            })

    return render_template('pages/venues.html', areas=data)
