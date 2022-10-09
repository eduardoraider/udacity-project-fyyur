from server import app
from flask import render_template

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/')
def index():
    return render_template('pages/home.html')


# 400 Bad Request
@app.errorhandler(400)
def not_found_error(error):
    return render_template('errors/400.html'), 400


# 401 Unauthorized
@app.errorhandler(401)
def not_found_error(error):
    return render_template('errors/401.html'), 401


# 403 Forbidden
@app.errorhandler(403)
def not_found_error(error):
    return render_template('errors/403.html'), 403


# 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


# 405 Method Not Allowed
@app.errorhandler(405)
def not_found_error(error):
    return render_template('errors/405.html'), 405


# 409 Conflict
@app.errorhandler(409)
def not_found_error(error):
    return render_template('errors/409.html'), 409


# 422 Unprocessable Entity
@app.errorhandler(422)
def not_found_error(error):
    return render_template('errors/422.html'), 422


# 500 Internal Server Error
@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500
