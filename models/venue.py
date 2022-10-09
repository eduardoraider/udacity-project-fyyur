from server import db

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.ARRAY(db.String()), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120), nullable=True)
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500), default='')
    shows = db.relationship('Show', backref='venues',
                            lazy='dynamic', cascade='all, delete')

    def __repr__(self):
        return f'<Venue ID: {self.id}, name: {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'address': self.address,
            'phone': self.phone,
            'genres': self.genres,
            'image_link': self.image_link,
            'facebook_link': self.facebook_link,
            'website_link': self.website,
            'seeking_talent': self.seeking_talent,
            'seeking_description': self.seeking_description,
        }
