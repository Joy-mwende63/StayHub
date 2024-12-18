# Room Reservation System
This is a Room Reservation System written in Python that allows users to interact with a hotel to view available rooms, reserve rooms, cancel reservations, and view current reservations.

## Features:
List available rooms: Display all rooms in the hotel with their details such as room type, capacity, price, and reservation status.
Reserve a room: Users can reserve a room if it is available.
Cancel a reservation: Cancel an existing reservation if it exists.
View current reservations: View all rooms that have been reserved, including their details.
### Requirements:

Python 3.x
SQLAlchemy for interacting with the database (if you're using a database for persistence)
Getting Started:
To get started with the Room Reservation System, follow the steps below to set up and run the application.

## Prerequisites
Before running the application, ensure you have Python 3.x installed on your machine. Additionally, you will need to install the required dependencies, including SQLAlchemy.

1. Clone the Repository
Clone the repository to your local machine using git:

bash
Copy code
git clone https://github.com/Joy-mwende63/StayHub
Alternatively, you can download the project as a ZIP file and extract it to your preferred location.

2. Install Dependencies
Navigate to the project directory and install the required dependencies by running:

bash
Copy code
cd StayHub
pip install -r requirements.txt
If you're using SQLAlchemy for database functionality, make sure it's included in the requirements.txt file. Example requirements.txt:

makefile
Copy code
SQLAlchemy==2.0.0
If you're not using a database and want to store data in memory, you can skip this step.

## Usage
1. Run the Application
To start the Room Reservation System, simply run the main.py script:

bash
Copy code
python main.py
This will run the program, allowing users to interact with the hotel, view rooms, and manage reservations.

## System Overview
1. Hotel Class
The Hotel class is responsible for managing a collection of rooms. It allows adding rooms to the hotel, listing rooms, reserving a room, and canceling reservations.

## Key Methods:
add_room(room): Adds a room to the hotel.
list_rooms(): Lists all rooms in the hotel.
reserve_room(room_id): Reserves a room with a specific room ID.
cancel_reservation(room_id): Cancels a reservation for a given room ID.
show_reservations(): Displays all current reservations.
2. Room Class
The Room class represents a single room in the hotel. It contains details like room type, capacity, price per night, and reservation status.

## Key Methods:
reserve(): Marks the room as reserved.
cancel_reservation(): Cancels the reservation for the room.
__str__(): Returns a string representation of the room with all its details.
3. Database Integration (Optional)
If you'd like to use a database to store the rooms and reservations, the project uses SQLAlchemy to interact with the database. The Room and Hotel classes are mapped to tables, and you can create and interact with these tables through the database.

To create the tables, run the models.py file to create the rooms and hotels tables in your database.
The database used in the example is SQLite, but you can easily change it to use MySQL or PostgreSQL by modifying the connection string in create_engine().
Example for creating tables:

python db/models.py
Example Interaction
When running the main.py script, the user will interact with the system through the following options:

1. List Rooms
The user can list all available rooms in the hotel:

List of rooms:
Room ID: 101, Type: Single, Capacity: 1, Price: $100.00, Reserved: No
Room ID: 102, Type: Double, Capacity: 2, Price: $150.00, Reserved: No
Room ID: 103, Type: Suite, Capacity: 4, Price: $250.00, Reserved: No

2. Reserve a Room
The user can reserve a room by its ID:

Please enter the room ID you want to reserve: 101
Room 101 has been successfully reserved!

3. Cancel a Reservation
The user can cancel a reservation by its ID:

Please enter the room ID you want to cancel: 101
Reservation for room 101 has been canceled.

4. View Reservations
The user can view all currently reserved rooms:

Current reservations:
Room ID: 101, Type: Single, Capacity: 1, Price: $100.00, Reserved: Yes

## Project Structure

The directory structure of the project looks like this:

Copy code
room-reservation-system/
│
├── db/
│   ├── models.py         # Database models using SQLAlchemy
│   └── seed.py           # Seed the database with initial data
│
├── main.py               # Main application logic
├── requirements.txt      # Required dependencies
└── README.md             # This README file
db/models.py: Contains the Room and Hotel models, along with database setup and table creation.
main.py: Contains the core logic for interacting with the hotel and managing reservations.
requirements.txt: Lists the Python dependencies required to run the project.

## Troubleshooting

Error: ModuleNotFoundError (SQLAlchemy): If you get this error, ensure that you have installed SQLAlchemy with pip install sqlalchemy.
Error: Database connection issues: If you're using a different database (MySQL/PostgreSQL), check the connection string in models.py and ensure that your database server is running.
## License

This project is open-source and available under the MIT License.

## Acknowledgments

Thanks to SQLAlchemy for making database integration easy in Python.
Inspired by hotel reservation systems and real-world booking applications.