from datetime import datetime

class Room:
    def __init__(self, room_id, room_type, capacity, price_per_night):
        self.room_id = room_id
        self.room_type = room_type
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.reserved = False
        self.special_requests = []
        self.reservation_dates = []
        self.ratings = []

    def reserve(self, check_in_date, check_out_date):
        if not self.reserved:
            self.reserved = True
            self.reservation_dates.append((check_in_date, check_out_date))
            return True
        return False

    def cancel_reservation(self):
        if self.reserved:
            self.reserved = False
            self.reservation_dates.pop()
            return True
        return False

    def add_special_request(self, request):
        self.special_requests.append(request)

    def rate_room(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            return f"Room {self.room_id} has been rated {rating} stars."
        return "Rating must be between 1 and 5."

    def get_average_rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return "No ratings yet."

    def __str__(self):
        avg_rating = self.get_average_rating() if isinstance(self.get_average_rating(), float) else "N/A"
        return f"Room ID: {self.room_id}, Type: {self.room_type}, Capacity: {self.capacity}, Price: ${self.price_per_night}, Reserved: {'Yes' if self.reserved else 'No'}, Average Rating: {avg_rating}"


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def list_rooms(self):
        return [str(room) for room in self.rooms]

    def search_rooms(self, room_type=None, max_price=None, min_capacity=None):
        available_rooms = [room for room in self.rooms if not room.reserved]
        if room_type:
            available_rooms = [room for room in available_rooms if room.room_type == room_type]
        if max_price:
            available_rooms = [room for room in available_rooms if room.price_per_night <= max_price]
        if min_capacity:
            available_rooms = [room for room in available_rooms if room.capacity >= min_capacity]
        return [str(room) for room in available_rooms]

    def reserve_room(self, room_id, check_in_date, check_out_date):
        room = next((room for room in self.rooms if room.room_id == room_id), None)
        if room and not room.reserved:
            if room.reserve(check_in_date, check_out_date):
                self.reservations.append(room)
                return f"Room {room_id} has been successfully reserved from {check_in_date} to {check_out_date}!"
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

    def total_revenue(self):
        return sum(room.price_per_night for room in self.reservations)

    def available_rooms(self):
        return [str(room) for room in self.rooms if not room.reserved]

    def apply_discount(self, room_id, discount_percentage):
        room = next((room for room in self.rooms if room.room_id == room_id), None)
        if room:
            discount = room.price_per_night * (discount_percentage / 100)
            room.price_per_night -= discount
            return f"Discount applied to room {room_id}. New price: ${room.price_per_night:.2f}."
        return f"Room {room_id} does not exist."


# Example Usage:
hotel = Hotel("Ocean View Resort")
room1 = Room(101, "Single", 1, 100)
room2 = Room(102, "Double", 2, 150)
hotel.add_room(room1)
hotel.add_room(room2)

print(hotel.reserve_room(101, "2024-12-21", "2024-12-23"))
print(hotel.reserve_room(102, "2024-12-22", "2024-12-24"))

room1.add_special_request("Extra pillows")
room2.add_special_request("Late check-in")

print(hotel.search_rooms(max_price=120))
print(hotel.show_reservations())

print(room1.rate_room(4))
print(room1.get_average_rating())
print(hotel.total_revenue())

# Applying a discount
print(hotel.apply_discount(101, 10))  # 10% discount
