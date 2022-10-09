from datetime import datetime
from flask_wtf import Form
from wtforms import (
    BooleanField,
    DateTimeField,
    StringField,
    SelectField,
    SelectMultipleField,
    ValidationError,
)
from wtforms.validators import DataRequired, Length, URL
import phonenumbers


# Choices State and Genre
state_choices = [
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('DC', 'DC'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
]

genres_choices = [
    ('Alternative', 'Alternative'),
    ('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Funk', 'Funk'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Heavy Metal', 'Heavy Metal'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Musical Theatre', 'Musical Theatre'),
    ('Pop', 'Pop'),
    ('Punk', 'Punk'),
    ('R&B', 'R&B'),
    ('Reggae', 'Reggae'),
    ('Rock n Roll', 'Rock n Roll'),
    ('Soul', 'Soul'),
    ('Other', 'Other'),
]
# End Choices State and Genre


# Validations
def validate_phone(form, field):
    if len(field.data) != 10:
        raise ValidationError('Invalid phone number.')
    try:
        input_number = phonenumbers.parse(field.data)
        if not (phonenumbers.is_valid_number(input_number)):
            raise ValidationError('Invalid phone number.')
    except:
        raise ValidationError('Invalid phone number.')


def validate_genres(form, field):
    if len(field.data) < 1:
        raise ValidationError('Invalid genres value.')
    try:
        genres_values = [choice[1] for choice in genres_choices]
        for value in field.data:
            if value not in genres_values:
                raise ValidationError('Invalid genres value.')
    except:
        raise ValidationError('Invalid genres value.')

# End validations


class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default=datetime.today()
    )


class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired(), Length(max=120)]
    )
    state = SelectField(
        'state', validators=[DataRequired(), Length(max=120)],
        choices=state_choices
    )
    address = StringField(
        'address', validators=[DataRequired(), Length(max=120)]
    )
    phone = StringField(
        'phone', validators=[DataRequired(), validate_phone, Length(max=120)]
    )
    image_link = StringField(
        'image_link', validators=[DataRequired(), URL(), Length(max=500)]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired(), validate_genres],
        choices=genres_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(), Length(max=120)]
    )
    website_link = StringField(
        'website_link', validators=[URL(), Length(max=120)]
    )

    seeking_talent = BooleanField('seeking_talent')

    seeking_description = StringField(
        'seeking_description', validators=[Length(max=500)]
    )


class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired(), Length(max=120)]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=state_choices
    )
    phone = StringField(
        'phone', validators=[DataRequired(), validate_phone, Length(max=120)]
    )
    image_link = StringField(
        'image_link', validators=[DataRequired(), URL(), Length(max=500)]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired(), validate_genres],
        choices=genres_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(), Length(max=120)]
    )

    website_link = StringField(
        'website_link', validators=[URL(), Length(max=120)]
    )

    seeking_venue = BooleanField('seeking_venue')

    seeking_description = StringField(
        'seeking_description', validators=[Length(max=500)]
    )
