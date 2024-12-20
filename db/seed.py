from db.models import Room, Hotel

def seed_hotel():
    # Create hotels and add rooms to them
    hotel1 = Hotel("Sunset Hotel")
    hotel1.add_room(Room(101, "Single", 1, 100))
    hotel1.add_room(Room(102, "Double", 2, 150))
    hotel1.add_room(Room(103, "Suite", 4, 250))

    hotel2 = Hotel("Mountain View Resort")
    hotel2.add_room(Room(201, "Single", 1, 120))
    hotel2.add_room(Room(202, "Double", 2, 180))
    hotel2.add_room(Room(203, "Suite", 3, 300))
    hotel2.add_room(Room(204, "Penthouse", 6, 500))

    hotel3 = Hotel("City Central Inn")
    hotel3.add_room(Room(301, "Single", 1, 90))
    hotel3.add_room(Room(302, "Double", 2, 130))
    hotel3.add_room(Room(303, "Suite", 4, 220))

    hotel4 = Hotel("Ocean Breeze Hotel")
    hotel4.add_room(Room(401, "Single", 1, 110))
    hotel4.add_room(Room(402, "Double", 2, 160))
    hotel4.add_room(Room(403, "Suite", 3, 280))
    hotel4.add_room(Room(404, "Presidential Suite", 5, 750))

    hotel5 = Hotel("Green Valley Lodge")
    hotel5.add_room(Room(501, "Single", 1, 80))
    hotel5.add_room(Room(502, "Double", 2, 130))
    hotel5.add_room(Room(503, "Suite", 4, 210))
    hotel5.add_room(Room(504, "Luxury Suite", 6, 450))

    # Return a list of all hotels
    return [hotel1, hotel2, hotel3, hotel4, hotel5]


