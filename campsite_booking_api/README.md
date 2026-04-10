# 🏕 Campsite Booking API (Django + DRF + JWT)

## 📌 Overview

This is a production-ready **Campsite Booking API** built using Django and Django REST Framework with JWT authentication. It allows users to view available campsites, register accounts, authenticate, and create bookings with comprehensive validation.

## 🚀 Features

* 🔐 User Registration & JWT Authentication
* 🏕 Campsite Listing with Pagination
* 📅 Booking Creation with Overlap & Capacity Validation
* 📋 User Booking Management
* 🔒 Rate Limiting & Security Headers
* 📚 API Documentation (Swagger/OpenAPI)
* 🛡️ CORS Support
* 📝 Comprehensive Logging
* 🗄️ Production Database Support (PostgreSQL)

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL (for production) or SQLite (for development)

### 1. Clone & Install Dependencies
```bash
git clone <repository-url>
cd campsite_booking_api
pip install -r requirements.txt
```

### 2. Environment Configuration
```bash
cp .env.example .env
# Edit .env with your configuration
```

**Required Environment Variables:**
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
DB_ENGINE=django.db.backends.postgresql  # For production
DB_NAME=campsite_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 3. Database Setup
```bash
# Development (SQLite)
python manage.py migrate

# Production (PostgreSQL)
# Ensure PostgreSQL is running and database exists
python manage.py migrate
```

### 4. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 5. Run Server
```bash
python manage.py runserver
```

---

## 🔗 API Endpoints

### Base URL: `http://localhost:8000/api/`

### 🏕 Campsites

#### Get Campsites (Paginated)
```
GET /api/campsites
```
**Query Parameters:**
- `page` (int): Page number
- `page_size` (int): Items per page (max 100)

**Response:**
```json
{
  "count": 25,
  "next": "http://localhost:8000/api/campsites?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Mountain View",
      "capacity": 4,
      "price_per_night": "75.00",
      "pricePerNight": "75.00"
    }
  ]
}
```

---

### 🔐 Authentication

#### Register User
```
POST /api/register/
```
**Request:**
```json
{
  "username": "johndoe",
  "password": "securepassword123"
}
```

#### Login (Get JWT Token)
```
POST /api/token/
```
**Request:**
```json
{
  "username": "johndoe",
  "password": "securepassword123"
}
```
**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
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
Authorization: Bearer <access_token>
Content-Type: application/json
```
**Request:**
```json
{
  "campsite": 1,
  "start_date": "2024-12-25",
  "end_date": "2024-12-27",
  "guests": 2
}
```

#### List User Bookings (Authenticated)
```
GET /api/bookings/
```
**Headers:**
```
Authorization: Bearer <access_token>
```

---

## 📚 API Documentation

Access the interactive API documentation at:
- **Swagger UI**: `http://localhost:8000/api/schema/swagger-ui/`
- **ReDoc**: `http://localhost:8000/api/schema/redoc/`
- **OpenAPI Schema**: `http://localhost:8000/api/schema/`

---

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run with coverage
coverage run manage.py test
coverage report
```

---

## 🚀 Deployment

### Environment Variables for Production
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourfrontend.com
DB_ENGINE=django.db.backends.postgresql
DB_NAME=prod_db
DB_USER=prod_user
DB_PASSWORD=prod_password
DB_HOST=prod-db-host
DB_PORT=5432
```

### Security Checklist
- [ ] `DEBUG=False`
- [ ] Strong `SECRET_KEY`
- [ ] `ALLOWED_HOSTS` configured
- [ ] HTTPS enabled
- [ ] Database credentials secured
- [ ] Regular security updates

### Docker Deployment (Optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "campsite_booking_api.wsgi:application", "--bind", "0.0.0.0:8000"]
```

---

## 🔍 Monitoring & Logging

### Logs Location
- Application logs: `logs/django.log`
- Console logs: Terminal output

### Health Check
```bash
curl http://localhost:8000/api/campsites
```

### Docker Logging Commands

#### View Web Service Logs (Real-time)
```bash
# Follow web service logs
docker compose logs -f web

# View last 100 lines of web logs
docker compose logs --tail=100 web

# View web logs with timestamps
docker compose logs -t web
```

#### View Worker Service Logs (Real-time)
```bash
# Follow worker service logs
docker compose logs -f worker

# View last 50 lines of worker logs
docker compose logs --tail=50 worker
```

#### View All Service Logs
```bash
# Follow all services logs
docker compose logs -f

# View logs from specific time range
docker compose logs --since "2024-01-01T00:00:00" --until "2024-01-02T00:00:00"

# View logs with specific service filtering
docker compose logs web worker
```

#### Advanced Docker Logging
```bash
# Export logs to file
docker compose logs > app_logs.txt

# Monitor logs with grep filtering
docker compose logs -f | grep "ERROR"

# View logs with line numbers
docker compose logs -f | nl

# Check container resource usage with logs
docker compose logs -f --no-log-prefix | head -20
```

---

## 🏗️ Architecture

```
campsite_booking_api/
├── camps/                    # Main app
│   ├── models.py            # Database models
│   ├── views.py             # API views
│   ├── serializers.py       # Data serialization
│   ├── validators.py        # Business logic validation
│   ├── urls.py              # URL routing
│   └── tests.py             # Unit tests
├── campsite_booking_api/     # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL config
│   └── wsgi.py              # WSGI config
├── logs/                    # Application logs
├── staticfiles/             # Static files
└── media/                   # User uploads
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests for new features
4. Ensure all tests pass
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.

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
