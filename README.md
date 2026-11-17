
# FOSSEE Python Winter Internship Portal

A web application developed as part of the FOSSEE Python Winter Internship 2026 screening task.

## Features

- Registration
- Login Profile page
- Upload file
    - Drop down with fields (Hackathon, Workshop, Internship, Orientation)
    - Event Date
    - File upload option for csv

## Project Structure

```text
fossee_project/
├── manage.py
├── db.sqlite3
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── profile.html
│   │       └── upload.html
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── fossee_project/
    ├── settings.py
    └── urls.py
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd task/fossee_project
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Apply database migrations

```bash
python manage.py migrate
```

### 4. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

## Database

The application uses SQLite as its database. Django creates the database and required tables when migrations are applied.

## File Uploads

Uploaded CSV files are stored locally in the `media/uploads/csvs/` directory.