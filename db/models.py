# db/models.py
class Room:
    def __init__(self, room_id, room_type, capacity, price_per_night):
        self.room_id = room_id
        self.room_type = room_type
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.reserved = False

    def reserve(self):
        if not self.reserved:
            self.reserved = True
            return True
        return False

    def cancel_reservation(self):
        if self.reserved:
            self.reserved = False
            return True
        return False

    def __str__(self):
        return f"Room ID: {self.room_id}, Type: {self.room_type}, Capacity: {self.capacity}, Price: ${self.price_per_night}, Reserved: {'Yes' if self.reserved else 'No'}"


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def list_rooms(self):
        return [str(room) for room in self.rooms]

    def reserve_room(self, room_id):
        room = next((room for room in self.rooms if room.room_id == room_id), None)
        if room and not room.reserved:
            if room.reserve():
                self.reservations.append(room)
                return f"Room {room_id} has been successfully reserved!"
            else:
                return f"Room {room_id} is already reserved."
        return f"Room {room_id} does not exist or is unavailable."

    def cancel_reservation(self, room_id):
        room = next((room for room in self.reservations if room.room_id == room_id), None)
        if room:
            if room.cancel_reservation():
                self.reservations.remove(room)
                return f"Reservation for room {room_id} has been canceled."
            else:
                return f"No reservation found for room {room_id}."
        return f"Room {room_id} was not reserved."

    def show_reservations(self):
        if not self.reservations:
            return "No rooms have been reserved."
        return [str(room) for room in self.reservations]
