from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login


followed_stocks = db.Table('followed_stocks',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('stock_id', db.Integer, db.ForeignKey('stock.id'), primary_key=True)    
)


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    phone_num = db.Column(db.String(15))
    dob = db.Column(db.DateTime)
    contact_pref = db.Column(db.Integer, default=1)

    account_change_notify = db.Column(db.Boolean, default=True)
    holds_notify = db.Column(db.Boolean, default=True)
    watchlist_notify = db.Column(db.Boolean, default=True)

    watch_list = db.relationship('Stock', secondary=followed_stocks, backref='users')

    def __repr__(self):
        return f'<User: {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))