# ApplicationVault - Job Application Tracker (Django + DRF)

A smart backend system to manage and track job applications, built using Django REST Framework.Includes:
- Django REST Framework (DRF)
- Token-based authentication (JWT)
- Public and protected API endpoints
- Celery with Redis for background tasks
- Telegram Bot Integration (on /start and new job alert)
- Modular project structure
-Production-ready `.env` management

---

## ⚙️ Setup Instructions

### 1 Clone the Repository
```bash
git clone https://github.com/DikshaKapse/ApplicationVault.git
cd ApplicationVault

2. Setup Virtual Environment
python -m venv env
env\Scripts\activate   # On Windows
# source env/bin/activate  # On Mac/Linux

3 Install Dependencies
pip install -r requirements.txt

4 Configure Environment Variables
Create a .env file in the root directory:
cp .env.example .env

Replace the placeholder values in .env with your actual values:

##  Environment Variables

| Key                 | Description                                        |
|---------------------|----------------------------------------------------|
| `SECRET_KEY`        | Django secret key                                  |
| `DEBUG`             | Set to `False` in production                       |
| `ALLOWED_HOSTS`     | Comma-separated list, e.g. `127.0.0.1,localhost`   |
| `TELEGRAM_BOT_TOKEN`| Your Telegram bot token                            |
| `TELEGRAM_CHAT_ID`  | Your personal chat ID (retrieved after `/start`)   |


▶ Running the Project
Start the Django Server
python manage.py migrate
python manage.py runserver

Start Redis Server
(Download Redis for Windows and run redis-server.exe)

Start Celery Worker
celery -A applicationvault_main worker --pool=solo -l info

##  API Testing (Postman)

| Endpoint                       | Method    | Auth | Description                          |
|-------------------------------|------------|------|---------------------------------------|
| `/api/v1/auth/registration/`  | POST       | No   | Register a new user                   |
| `/api/v1/auth/login/`         | POST       | No   | Login and receive JWT tokens          |
| `/api/public-info/`           | GET        | No   | Public endpoint (no auth needed)      |
| `/api/user-dashboard/`        | GET        | Yes  | Private user dashboard                |
| `/api/applications/`          | GET/POST   | Yes  | CRUD operations on job applications   |
| `/api/test-telegram/`         | GET        | No   | Sends a test message via Telegram bot |

 Telegram Bot
After registering, start your bot on Telegram using /start

You'll receive messages when new job applications are created

Tech Stacks:

Django 5.2.3
Django REST Framework
JWT Auth (SimpleJWT)
Redis + Celery
Telegram Bot API
Python Decouple
SQLite (default, easy testing)
