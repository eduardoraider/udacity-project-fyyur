from flask import flash, render_template
from server import app, db
from forms import ShowForm
from models.show import Show

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/shows/create')
def create_shows():
    # renders form. do not touch.
    form = ShowForm()
    return render_template('forms/new_show.html', form=form)


@app.route('/shows/create', methods=['POST'])
def create_show_submission():
    # called to create new shows in the db,
    # upon submitting new show listing form
    error = False
    form = ShowForm()
    try:
        create_show = Show(
            venue_id=form.venue_id.data,
            artist_id=form.artist_id.data,
            start_time=form.start_time.data
        )
        db.session.add(create_show)
        db.session.commit()
    except Exception as ex:
        error = True
        db.session.rollback()
        app.logger.error(ex, exc_info=True)
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Show could not be listed. Invalid ID', 'danger')
        return render_template('pages/home.html')
    else:
        flash('Show was successfully listed!', 'info')
        return render_template('pages/home.html')
