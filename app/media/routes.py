from flask import render_template, url_for, redirect
from flask_login import current_user, login_required
from app import db
from app.media import bp

@bp.route('/headlines')
@login_required
def headlines():
    return render_template('media/headlines.html', title='News Headlines')