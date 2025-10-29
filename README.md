# 🌤️ Weather Dashboard API

A Django REST API application with PostgreSQL database integration and real-time weather data from OpenWeatherMap API.

## 🚀 Features

### 1. CRUD Operations
- Full Create, Read, Update, Delete functionality for location management
- RESTful API endpoints built with Django REST Framework
- Pagination support for large datasets

### 2. Third-Party API Integration
- Real-time weather data fetching from OpenWeatherMap API
- Automatic weather data storage for historical analysis
- City search functionality using geocoding API

### 3. Data Visualization & Reporting
- Weather statistics endpoint with aggregated analytics
- Average, minimum, and maximum temperature calculations
- Humidity trends and weather pattern analysis

### 4. Database
- PostgreSQL database (Supabase for production)
- SQLite for local development
- Proper migrations and database schema management

## 🛠️ Technology Stack

- **Backend:** Django 4.2.7
- **API Framework:** Django REST Framework 3.14.0
- **Database:** PostgreSQL (Supabase) / SQLite
- **External API:** OpenWeatherMap API
- **Python:** 3.x

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd weather-dashboard
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Environment Variables

Create a `.env` file in the project root:
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=postgresql://user:password@host:port/database
OPENWEATHER_API_KEY=your-openweather-api-key
```

**Get OpenWeatherMap API Key:**
1. Sign up at https://openweathermap.org/api
2. Get your free API key
3. Add it to `.env` file

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Create Superuser
```bash
python manage.py createsuperuser
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## 📚 API Endpoints

### Locations API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/locations/` | List all locations |
| POST | `/api/locations/` | Create new location |
| GET | `/api/locations/{id}/` | Get specific location |
| PUT | `/api/locations/{id}/` | Update location |
| DELETE | `/api/locations/{id}/` | Delete location |
| GET | `/api/locations/{id}/current_weather/` | Get current weather for location |
| GET | `/api/locations/search_city/?city=name` | Search for a city |

### Weather Data API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/weather-data/` | List all weather records |
| GET | `/api/weather-data/{id}/` | Get specific weather record |
| GET | `/api/weather-data/statistics/` | Get weather statistics |

### Admin Panel

- URL: `/admin/`
- Manage locations and weather data through Django admin interface

## 🧪 Testing the API

### Example: Create a Location
```bash
POST /api/locations/
Content-Type: application/json

{
    "name": "New York",
    "country": "United States",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "is_active": true
}
```

### Example: Get Current Weather
```bash
GET /api/locations/1/current_weather/
```

### Example: Search City
```bash
GET /api/locations/search_city/?city=Mumbai
```

### Example: Get Statistics
```bash
GET /api/weather-data/statistics/
```

## 📊 Database Models

### Location Model
- `name`: City name
- `country`: Country name
- `latitude`: Latitude coordinate
- `longitude`: Longitude coordinate
- `is_active`: Active status
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### WeatherData Model
- `location`: Foreign key to Location
- `temperature`: Temperature in Celsius
- `feels_like`: Feels like temperature
- `humidity`: Humidity percentage
- `pressure`: Atmospheric pressure
- `wind_speed`: Wind speed in m/s
- `description`: Weather description
- `icon`: Weather icon code
- `recorded_at`: Recording timestamp

## 🌐 Deployment

The application is configured for easy deployment to platforms like:
- Heroku
- Railway
- Render
- PythonAnywhere

Database connection automatically switches based on environment.

## 📁 Project Structure
```
weather-dashboard/
├── dashboard/              # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # API views
│   ├── serializers.py     # DRF serializers
│   ├── urls.py            # App URLs
│   └── templates/         # HTML templates
├── weather_project/        # Django project settings
│   ├── settings.py        # Main settings
│   └── urls.py            # Root URLs
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in git)
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## 🔒 Security Notes

- Never commit `.env` file to version control
- Keep your `SECRET_KEY` and API keys secure
- Use environment variables for sensitive data
- Update `ALLOWED_HOSTS` for production deployment

## 🤝 Contributing

This is a demo project for interview purposes.

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

Swapnali Anarase

## 🙏 Acknowledgments

- OpenWeatherMap API for weather data
- Django & Django REST Framework documentation
- Supabase for PostgreSQL database hosting