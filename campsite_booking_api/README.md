# 🏕 Campsite Booking API (Django + DRF + JWT)

## 📌 Overview

This project is a minimal **Campsite Booking API** built using Django and Django REST Framework.
It allows users to:

* View available campsites (paginated)
* Register and authenticate using JWT
* Create bookings (with validation)
* View their bookings
* Prevent overlapping bookings


---

## 🚀 Features

* 🔐 User Registration
* 🔑 JWT Login Authentication
* 🏕 Campsite Listing (Paginated)
* 📅 Booking Creation (Login Required)
* 📋 User Booking List

---

## 🔗 API Endpoints

### 🏕 Campsites

#### Get Campsites

```
GET /api/campsites
```

---

### 🔐 Authentication

#### Register User

```
POST /api/register/
```

**Request Body:**

```json
{
  "username": "uday",
  "password": "yourpassword"
}
```

---

#### Login (Get JWT Token)

```
POST /api/token/
```

**Request Body:**

```json
{
  "username": "uday",
  "password": "yourpassword"
}
```

**Response:**

```json
{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}
```

---

### 📅 Bookings

#### Create Booking (Authenticated)

```
POST /api/bookings/create/
```

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
Content-Type: application/json
```

**Request Body:**

```json
{
  "campsite": 1,
  "start_date": "2026-04-10",
  "end_date": "2026-04-12"
}
```

---

#### Get User Bookings (Authenticated)

```
GET /api/bookings/
```

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

---

## 📊 Validation Rules

* `start_date` must be before `end_date`
* Bookings must not overlap for the same campsite
* (Optional) Capacity-based validation supported

---

## 🧱 Project Structure

```
├── camps
│   ├── admin.py
│   ├── apps.py
│   ├── dataclasses.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_booking_guests.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-39.pyc
│   │       ├── 0002_booking_guests.cpython-39.pyc
│   │       └── __init__.cpython-39.pyc
│   ├── mixins.py
│   ├── models.py
│   ├── pagination.py
│   ├── __pycache__
│   │   ├── admin.cpython-39.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── dataclasses.cpython-39.pyc
│   │   ├── __init__.cpython-39.pyc
│   │   ├── mixins.cpython-39.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── pagination.cpython-39.pyc
│   │   ├── serializers.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   ├── validators.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── validators.py
│   └── views.py
├── campsite_booking_api
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── settings.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── wsgi.cpython-39.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── Questions.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone <repo-url>
cd project
```

---

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create Superuser (Optional)

```
python manage.py createsuperuser
```

---

### 6. Run Server

```
python manage.py runserver
```

---

## 🧪 Testing Flow

1. Register user
2. Login → get JWT token
3. Create campsite (via admin)
4. Fetch campsites
5. Create booking
6. Fetch user bookings

---

## 🧠 Design Highlights

* Uses **Class-Based Views (CBVs)**
* Booking validation via **Abstract Base Class**
* Shared fields via **Model Mixins**
* Uses **@property** and **@staticmethod**
* Dataclass used for structured input handling

---

## 📌 Notes

* Authentication is stateless using JWT
* No separate auth app (uses Django default User)
* Designed for clarity and maintainability

---

## 👨‍💻 Author

Uday
