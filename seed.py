from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
first_user = User(first_name="Tom", last_name="Smith", image_url="https://i.pinimg.com/originals/92/a6/2f/92a62f0221f58fe503a15fcb13f5c107.png")
second_user = User(first_name="Jack", last_name="Sparrow", image_url="https://iadsb.tmgrup.com.tr/0999d9/0/0/0/0/2048/1199?u=https://idsb.tmgrup.com.tr/2017/03/19/jack-sparrow-might-be-inspired-by-a-muslim-captain-1489951367309.jpg")

# Add new objects to session, so they'll persist
db.session.add(first_user)
db.session.add(second_user)

# Commit--otherwise, this never gets saved!
db.session.commit()