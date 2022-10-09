from flask import flash, render_template
from server import app, db
from models.venue import Venue
from forms import VenueForm

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/venues/create', methods=['GET'])
def create_venue_form():
    form = VenueForm()
    return render_template('forms/new_venue.html', form=form)


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():

    error = False
    form = VenueForm()
    try:
        create_venue = Venue(
            name=form.name.data,
            city=form.city.data,
            state=form.state.data,
            address=form.address.data,
            phone=form.phone.data,
            genres=form.genres.data,
            image_link=form.image_link.data,
            facebook_link=form.facebook_link.data,
            website=form.website_link.data,
            seeking_talent=form.seeking_talent.data,
            seeking_description=form.seeking_description.data
        )
        db.session.add(create_venue)
        db.session.commit()
    except Exception as ex:
        error = True
        db.session.rollback()
        app.logger.error(ex, exc_info=True)
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Venue ' +
              form.name.data + ' could not be listed.', 'danger')
    else:
        flash('Venue ' + form.name.data + ' was successfully listed!', 'info')
        return render_template('pages/home.html')
