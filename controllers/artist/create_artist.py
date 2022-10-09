from flask import flash, render_template
from server import app, db
from models.artist import Artist
from forms import ArtistForm

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/artists/create', methods=['GET'])
def create_artist_form():
    form = ArtistForm()
    return render_template('forms/new_artist.html', form=form)


@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
    # called upon submitting the new artist listing form
    error = False
    form = ArtistForm()
    try:
        create_artist = Artist(
            name=form.name.data,
            city=form.city.data,
            state=form.state.data,
            phone=form.phone.data,
            genres=form.genres.data,
            facebook_link=form.facebook_link.data,
            image_link=form.image_link.data,
            website=form.website_link.data,
            seeking_venue=form.seeking_venue.data,
            seeking_description=form.seeking_description.data
        )
        db.session.add(create_artist)
        db.session.commit()
    except Exception as ex:
        error = True
        db.session.rollback()
        app.logger.error(ex, exc_info=True)
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Artist ' +
              form.name.data + ' could not be listed.', 'danger')
    else:
        flash('Artist ' + form.name.data + ' was successfully listed!', 'info')
        return render_template('pages/home.html')
