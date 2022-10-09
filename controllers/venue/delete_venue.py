from flask import (
    flash,
    redirect,
    url_for
)
from server import app, db
from models.venue import Venue

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#

# Browsers support PUT and DELETE only with AJAX request, but not with HTML
# form submission. HTML form tag will allow only GET and POST methods.


@app.route('/venues/<int:venue_id>/delete', methods=['GET', 'POST'])
def delete_venue(venue_id):
    # SQLAlchemy ORM to delete a record. Handle cases where the
    # session commit could fail.

    # BONUS CHALLENGE: Implement a button to delete a Venue on a
    # Venue Page, have it so that
    # clicking that button delete it from the db then redirect
    # the user to the homepage
    error = False

    try:
        venue = db.session.query(Venue).filter_by(id=venue_id).first()
        venue_name = venue.name
        db.session.delete(venue)
        db.session.commit()
    except Exception as ex:
        error = True
        db.session.rollback()
        app.logger.error(ex, exc_info=True)
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Venue ' +
              venue_name + ' could not be deleted!', 'danger')
    else:
        flash('Venue ' + venue_name + ' was successfully deleted!', 'info')
        return redirect(url_for('.index'))
