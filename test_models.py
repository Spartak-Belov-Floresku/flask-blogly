from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask_user:password@localhost/blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Tests for model for User."""

    def setUp(self):
        """Clean up any existing Users."""

        User.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    '''run test to ctreate user object'''
    def test_create_user_obj(self):
        user = User(first_name="Tom", last_name="Smith")

        self.assertEqual(user.last_name, "Smith")

    '''run test to insert user data into database'''
    def test_insert_user_to_db(self):
        user = User(first_name="Tom", last_name="Smith")
        
        db.session.add(user)
        db.session.commit()

        self.assertEqual(user.id, 1)
