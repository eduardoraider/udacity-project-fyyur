from flask import (
    flash,
    redirect,
    render_template,
    url_for,
    request
)
from server import app, db
from models.venue import Venue
from forms import VenueForm

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
    venue = Venue.query.get(venue_id)
    form = VenueForm(data=venue.to_dict())
    return render_template('forms/edit_venue.html', form=form, venue=venue)


@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
    # venue record with ID <venue_id> using the new attributes
    error = False
    form = VenueForm()
    venue = Venue.query.get(venue_id)
    
    try:
        venue.name = form.name.data
        venue.city = form.city.data
        venue.state = form.state.data
        venue.address = form.address.data
        venue.phone = form.phone.data
        venue.genres = form.genres.data
        venue.image_link = form.image_link.data
        venue.facebook_link = form.facebook_link.data
        venue.website = form.website_link.data
        venue.seeking_talent = form.seeking_talent.data
        venue.seeking_description = form.seeking_description.data

        db.session.commit()
    except Exception as ex:
        error = True
        db.session.rollback()
        app.logger.error(ex, exc_info=True)
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Venue ' +
            form.name.data + ' could not be updated!', 'danger')
    else:
        flash('Venue ' + form.name.data + ' was successfully updated!', 'info')
        return redirect(url_for('show_venue', venue_id=venue_id))
