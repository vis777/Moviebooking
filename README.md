# Moviebooking

## Overview
This project implements a backend-only seat management system for movie shows.
It focuses on seat availability and booking.

##Features
- Create shows and seats
- Hold seats temporarily
- Confirm booking
- Query seat status: available, held, booked
- Prevent double booking even with simultaneous users

## Seat States
 AVAILABLE - Can be selected by any user 
 HELD      - Temporarily reserved; expires automatically if not booked 
 BOOKED    - Successfully booked; cannot be reused 

 ## How the System Works

- Each seat is stored as an individual database row
- Seat booking operations run inside database transactions
- Row-level locking is used to prevent race conditions
- Held seats automatically expire if booking is not completed
## How to Run

```bash
# Install Django
pip install django
bash
Copy code
# Apply migrations
python manage.py makemigrations
python manage.py migrate
bash
Copy code
# Create superuser
python manage.py createsuperuser
bash
Copy code
# Run the server
python manage.py runserver
text
Copy code
# Access admin panel
http://127.0.0.1:8000/admin
