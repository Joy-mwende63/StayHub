from db.models import Room, Hotel
from db.seed import seed_hotel
from debug import log_error
from datetime import datetime

def run_cli():
    hotels = seed_hotel()  # Get the list of hotels
    current_hotel = None

    while True:
        print("\nWelcome to the Room Reservation System")
        
        if current_hotel is None:
            print("1. Choose a hotel")
        else:
            print(f"1. List available rooms in {current_hotel.name}")
            print("2. Reserve a room")
            print("3. Cancel a reservation")
            print("4. Show all reservations")
            print("5. Add a room")
        
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            if current_hotel is None:
                print("Available Hotels:")
                for i, hotel in enumerate(hotels, 1):
                    print(f"{i}. {hotel.name}")
                hotel_choice = int(input("Choose a hotel by number: "))
                if 1 <= hotel_choice <= len(hotels):
                    current_hotel = hotels[hotel_choice - 1]
                    print(f"Now interacting with {current_hotel.name}")
                else:
                    print("Invalid choice. Please choose a valid hotel.")
            else:
                rooms = current_hotel.list_rooms()
                print("\nAvailable Rooms:")
                for room in rooms:
                    print(room)

        elif choice == "2":
            if current_hotel is not None:
                try:
                    room_id = int(input("Enter the room ID to reserve: "))
                    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
                    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

                    # Convert dates to datetime objects to ensure validity
                    try:
                        check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
                        check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")

                        if check_in_date >= check_out_date:
                            print("Error: Check-out date must be after check-in date.")
                        else:
                            result = current_hotel.reserve_room(room_id, check_in_date, check_out_date)
                            print(result)
                    except ValueError:
                        print("Error: Please enter valid dates in the format YYYY-MM-DD.")
                except ValueError:
                    log_error("Invalid input: Room ID must be an integer.")
                    print("Error: Room ID must be a number.")
            else:
                print("No hotel found. Please choose a hotel first.")

        elif choice == "3":
            if current_hotel is not None:
                try:
                    room_id = int(input("Enter the room ID to cancel reservation: "))
                    result = current_hotel.cancel_reservation(room_id)
                    print(result)
                except ValueError:
                    log_error("Invalid input: Room ID must be an integer.")
                    print("Error: Room ID must be a number.")
            else:
                print("No hotel found. Please choose a hotel first.")

        elif choice == "4":
            if current_hotel is not None:
                reservations = current_hotel.show_reservations()
                print("\nReservations:")
                if isinstance(reservations, list):
                    for res in reservations:
                        print(res)
                else:
                    print(reservations)
            else:
                print("No hotel found. Please choose a hotel first.")

        elif choice == "5":
            if current_hotel is not None:
                room_id = int(input("Enter room ID: "))
                room_type = input("Enter room type (e.g., Single, Double, Suite): ")
                capacity = int(input("Enter room capacity: "))
                price_per_night = float(input("Enter room price per night: $"))

                new_room = Room(room_id, room_type, capacity, price_per_night)
                current_hotel.add_room(new_room)
                print(f"Room {room_id} added successfully to {current_hotel.name}.")
            else:
                print("No hotel found. Please choose a hotel first.")

        elif choice == "6":
            print("Thank you for using the Room Reservation System. Goodbye!")
            break
        else:
            log_error(f"Invalid choice: {choice}")
            print("Invalid choice! Please choose again.")
