# 📚 Syllabus API

A FastAPI-based backend to manage syllabus media content like videos, documents, and images categorized by age groups (child, teenager, man).

---

## 🚀 Features

- ✅ User Signup & Login with JWT Authentication
- 🎥 Add and retrieve media files (video/image/document)
- 👨‍👧 Media filtering by age groups (child, teenager, man)
- 🔐 Role-based user access (user/admin)
- 🧪 Token-based media access

---

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI
- **Database**: PostgreSQL + SQLAlchemy ORM
- **Auth**: JWT (with OAuth2 Password Flow)
- **Tools**: Alembic (migrations), Pydantic (validation)

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/jemin555github/syllabus-api.git
cd syllabus-api

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# to run this project
python main.py

you have to make .env file for configurations...

python version 3.10
to test api environment visit localhost:8000/docs in browser or you can check how to open swagger to test api.


//Install pgAdmin4 for DB Viewer
https://www.postgresql.org/ftp/pgadmin/pgadmin4/v9.5/macos/

// Install postgres for DB 
brew install postgresql@15
export LDFLAGS="-L/usr/local/opt/postgresql@15/lib"
export CPPFLAGS="-I/usr/local/opt/postgresql@15/include"
brew services start postgresql@15

####To start postgres
psql postgres
psql --version

CREATE USER your_username WITH PASSWORD 'your_password';
ALTER USER your_username WITH SUPERUSER;
CREATE DATABASE your_db OWNER your_username;

pip install psycopg2-binary (if not installed)

###Data migration to pgadmin4 (delete all version from pgadmin4)
alembic revision --autogenerate -m "models.py creation"
alembic upgrade head