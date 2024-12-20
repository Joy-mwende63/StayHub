# db/seed.py
from db.models import Room, Hotel

def seed_hotel():
    hotel = Hotel("Sunset Hotel")

    # Adding rooms to the hotel
    hotel.add_room(Room(101, "Single", 1, 100))
    hotel.add_room(Room(102, "Double", 2, 150))
    hotel.add_room(Room(103, "Suite", 4, 250))

    return hotel


