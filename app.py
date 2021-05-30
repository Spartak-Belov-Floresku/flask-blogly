from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask_user:password@localhost/blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "hello"
app.debug = True
DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """List users"""

    return redirect('/users')

@app.route('/users')
def list_users():
    """List users"""

    users = User.query.all()
    return render_template('list_users.html', users = users)


@app.route('/users/new')
def add_form():
    """Show form to create a new user"""

    return render_template('form.html')


@app.route('/users/new', methods=['POST'])
def add_user():
    """Add a new user to the database"""

    '''get data from POST request'''
    first_name = request.form.get('first_name', "empty")
    last_name = request.form.get('last_name', "empty")
    img_url = request.form.get('img_url', "empty")

    '''create User object'''
    user = User(first_name=first_name, last_name=last_name, image_url=img_url)

    '''Add new objects to session, so they'll persist'''
    db.session.add(user)

    '''Commit--otherwise, this never gets saved!'''
    db.session.commit()

    return redirect('/users')


@app.route("/users/<int:id>")
def data_user(id):
    """Show a user page"""

    '''Get user from db'''
    user = User.query.get(id)

    return render_template('user.html', user=user)


@app.route('/users/<int:id>/edit')
def edit_form(id):
    '''Show an edit user form.'''

    '''Get user from db'''
    user = User.query.get(id)

    return render_template('edit.html', user=user)


@app.route('/users/<int:id>/edit', methods=['POST'])
def edit_user(id):
    """Update user data"""

    '''get user from db'''
    user = User.query.get(id)

    '''get data from form'''
    first_name = request.form.get('first_name', "empty")
    last_name = request.form.get('last_name', "empty")
    image_url = request.form.get('img_url', "empty")

    '''update user data'''
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    db.session.add(user)
    db.session.commit()


    return redirect(f'/users')


@app.route('/users/<int:id>/delete', methods=['POST'])
def delete_user(id):

    """Delete user data from database"""

    User.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(f'/users')


if __name__ == "__main__":
    app.run(debug=True)

