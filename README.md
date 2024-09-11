# Django Web API

This project is a Django-based API that allows users to manage car advertisements, user authentication, and other operations using JWT for secure authentication.

## Features

- User Signup, Login (using JWT), and Change Password
- List, filter, and paginate car ads
- JWT Authentication for secure user login
- Custom user model with email as the unique identifier
- Filtering car ads based on body type (SUV, Crossover, etc.)

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.12
- pip
- PostgreSQL (or your preferred database)
- Virtual environment package (optional but recommended)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/YasinArabi83/django-web-API.git

2. Navigate to the project directory:

   ```bash
   cd django-web-API

3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

5. Configure the `.env` file as `.env.sample` or update the DATABASES section in `settings.py`

6. Apply migrations to set up the database:
   ```bash
   python manage.py migrate

7. Create a superuser to access the Django admin:
   ```bash
   python manage.py createsuperuser
   
8. Start the development server:
   ```bash
   python manage.py runserver
9. Navigate to `http://localhost:8000/admin` and log in using your superuser credentials to access the admin panel.


## Endpoints


### Authentication

- Sign up: `api/signup/` (POST)
  - Request Body:
  ```JSON
  {
  "email": "example@example.com",
  "password": "yourpassword",
  "password_confirm": "yourpassword",
  "first_name": "John",
  "last_name": "Doe"
  }
- Login: `api/login/` (POST)
    - Request Body:
  ```JSON
  {
  "email": "example@example.com",
  "password": "yourpassword"
  }
- Change Password: `api/change-password/` (POST, Auth required)

    - Request Body:
  ```JSON
  {
  "old_password": "oldpassword",
  "new_password": "newpassword"
  }
- Token Refresh: /token/refresh/ (POST)



## Car Ads

- List All Ads: `api/car/` (GET)
- Filter by Body Type: `api/car/type/<body_type>/` (GET)
  - Example: /car/type/suv/
- Pagination: The car ads list is paginated with 20 items per page by default. You can navigate using next and previous links in the response.


## Built With
- Django - The high-level Python Web framework used.
- Django Rest Framework (DRF) - Used for building the API.
- PostgreSQL - The database used for data persistence.
- JWT - For authentication.
