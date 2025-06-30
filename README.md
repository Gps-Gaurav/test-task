# test-task

## Project: Booking API using Django REST Framework

This is a backend API where users can set their weekly availability, and guests can book time slots (15min, 30min, 45min, 60min) based on that. The system prevents overlapping bookings and only allows booking within available time ranges.

## How to Run the Project

## 1. Clone the repository and install dependencies

For Windows:
 python -m venv env
 env\Scripts\activate

For macOS/Linux:
 python3 -m venv env
 source env/bin/activate
 uv pip install -r requirements.txt

## 2. Apply migrations

python manage.py makemigrations
python manage.py migrate

## 3. Create superuser

python manage.py createsuperuser

-Use the following credentials:
  Username: admin
  Password: 123456

## 4. Run the server
python manage.py runserver

You can use this to log in at [http://127.0.0.1:8000/admin]

## Swagger UI (API Docs)

- After starting the server, open [http://127.0.0.1:8000/swagger/] in browser.

## 1. Weekly Availability
`GET /api/availability/` → List current user’s availability
`POST /api/availability/` → Add availability slot

## 2. Booking (Guest Slot Booking)
`GET /api/book/` → List all bookings
`POST /api/book/` → Create a new booking

## Booking Rules

| Day       | day\_of\_week |
| --------- | ------------- |
| Monday    | 0             |
| Tuesday   | 1             |
| Wednesday | 2             |
| Thursday  | 3             |
| Friday    | 4             |
| Saturday  | 5             |
| Sunday    | 6             |

- Booking durations can be: **15, 30, 45, or 60 minutes**.
- Booking must be **within available slots** set by the user.
- Bookings **cannot overlap** with existing ones.
- Time format should be `HH:MM`.
 example:
  {
  "guest_name": "Gaurav",
  "user": 1,
  "date": "2025-07-01",
  "start_time": "10:15",
  "end_time": "10:45"
  }

## Notes

- Use any API client like **Postman**, or use **Swagger UI** directly.
- The system checks both availability and existing bookings      before confirming a new booking.
- SQLite is used as default DB for simplicity.
