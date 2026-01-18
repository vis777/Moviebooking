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
1. Install Django
```bash
pip install django
```
2. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
3. Create superuser
```bash
python manage.py createsuperuser
```
4. Run the server
 ```bash
python manage.py runserver
```
5. Access admin panel
 ```bash
http://127.0.0.1:8000/admin
