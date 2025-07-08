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

