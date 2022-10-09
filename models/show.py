from server import db

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#


class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'),
                          nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'),
                         nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Show ID: {self.id}, Artist ID: {self.artist_id}, \
                Venue ID: {self.venue_id}, Start time: {self.start_time}>'

    venue = db.relationship('Venue', backref="show")
    artist = db.relationship('Artist', backref="show")

    def show_details(self):
        return{
            'venue_id': self.venue_id,
            'venue_name': self.venue.name,
            'artist_id': self.artist_id,
            'artist_name': self.artist.name,
            'artist_image_link': self.artist.image_link,
            'start_time': self.start_time
        }

    def show_artist_details(self):
        return {
            'artist_id': self.artist_id,
            'artist_name': self.artist.name,
            'artist_image_link': self.artist.image_link,
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M:%S')
        }

    def show_venue_details(self):
        return {
            'venue_id': self.venue_id,
            'venue_name': self.venue.name,
            'venue_image_link': self.venue.image_link,
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M:%S')
        }
