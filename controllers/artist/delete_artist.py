from flask import (
    flash,   
    redirect,
    url_for
)
from server import app, db
from models.artist import Artist

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#

# Browsers support PUT and DELETE only with AJAX request, but not with HTML
# form submission. HTML form tag will allow only GET and POST methods.


@app.route('/artists/<int:artist_id>/delete', methods=['GET', 'POST'])
def delete_artist(artist_id):
    error = False
    try:
        artist = db.session.query(Artist).filter_by(id=artist_id).first()
        artist_name = artist.name
        db.session.delete(artist)
        db.session.commit()
    except Exception as ex:
        error = True
        db.session.rollback()
        app.logger.error(ex, exc_info=True)
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Artist ' +
              artist_name + ' could not be deleted!', 'danger')
    else:
        flash('Artist ' + artist_name + ' was successfully deleted!', 'info')
        return redirect(url_for('.index'))
