# cli.py
from db.seed import seed_hotel
from debug import log_error

def run_cli():
    hotel = seed_hotel()

    while True:
        print("\nWelcome to the Room Reservation System")
        print("1. List available rooms")
        print("2. Reserve a room")
        print("3. Cancel a reservation")
        print("4. Show all reservations")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            rooms = hotel.list_rooms()
            print("\nAvailable Rooms:")
            for room in rooms:
                print(room)
        elif choice == "2":
            try:
                room_id = int(input("Enter the room ID to reserve: "))
                result = hotel.reserve_room(room_id)
                print(result)
            except ValueError:
                log_error("Invalid input: Room ID must be an integer.")
                print("Error: Room ID must be a number.")
        elif choice == "3":
            try:
                room_id = int(input("Enter the room ID to cancel reservation: "))
                result = hotel.cancel_reservation(room_id)
                print(result)
            except ValueError:
                log_error("Invalid input: Room ID must be an integer.")
                print("Error: Room ID must be a number.")
        elif choice == "4":
            reservations = hotel.show_reservations()
            print("\nReservations:")
            if isinstance(reservations, list):
                for res in reservations:
                    print(res)
            else:
                print(reservations)
        elif choice == "5":
            print("Thank you for using the Room Reservation System. Goodbye!")
            break
        else:
            log_error(f"Invalid choice: {choice}")
            print("Invalid choice! Please choose again.")