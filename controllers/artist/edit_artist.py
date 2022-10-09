from flask import (
    flash,
    redirect,  
    render_template,
    url_for
)
from server import app, db
from models.artist import Artist
from forms import ArtistForm

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
    artist = Artist.query.get(artist_id)
    form = ArtistForm(data=artist.to_dict())
    return render_template('forms/edit_artist.html', form=form, artist=artist)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
    # artist record with ID <artist_id> using the new attributes
    error = False
    form = ArtistForm()
    artist = Artist.query.get(artist_id)

    try:
        artist.name = form.name.data
        artist.city = form.city.data
        artist.state = form.state.data
        artist.phone = form.phone.data
        artist.genres = form.genres.data
        artist.facebook_link = form.facebook_link.data
        artist.image_link = form.image_link.data
        artist.website = form.website_link.data
        artist.seeking_venue = form.seeking_venue.data
        artist.seeking_description = form.seeking_description.data

        db.session.commit()
    except Exception as ex:
        error = True
        db.session.rollback()
        app.logger.error(ex, exc_info=True)
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Artist ' +
              form.name.data + ' could not be updated!', 'danger')
    else:
        flash('Artist ' + form.name.data + ' was successfully updated!', 'info')
        return redirect(url_for('show_artist', artist_id=artist_id))
