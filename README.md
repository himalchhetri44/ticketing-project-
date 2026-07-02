# 🎟️ TicketFlow — MySQL Edition

## Folder Structure
```
ticketflow_mysql/
├── run.py
├── config.py              ← Edit your MySQL credentials here
├── seed_admin.py
├── requirements.txt
└── app/
    ├── __init__.py
    ├── models.py
    ├── controllers/
    │   ├── authController.py
    │   ├── mainController.py
    │   ├── bookingController.py
    │   ├── adminController.py
    │   └── scanController.py
    ├── repository/
    │   └── user_repo.py
    ├── routes/
    │   ├── mainRoutes.py
    │   ├── authRoutes.py
    │   ├── eventRoutes.py
    │   ├── bookingRoutes.py
    │   ├── adminRoutes.py
    │   └── scanRoutes.py
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   ├── event_detail.html
    │   ├── auth/ (login.html, register.html)
    │   ├── booking/ (new.html, confirm.html, my_tickets.html)
    │   ├── admin/ (dashboard.html)
    │   └── scan/ (scanner.html)
    └── static/
        ├── css/style.css
        └── js/main.js
```

## Setup Steps

### Step 1 — MySQL Workbench
1. Open MySQL Workbench
2. Connect to your local MySQL server
3. Run this SQL in the Query tab:
   CREATE DATABASE ticketflow_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

### Step 2 — Edit config.py
Open config.py and set:
- MYSQL_USER     = your MySQL username (usually 'root')
- MYSQL_PASSWORD = your MySQL password
- MYSQL_DB       = 'ticketflow_db'

### Step 3 — Virtual environment
python -m venv venv
venv\Scripts\activate   (Windows)
source venv/bin/activate (Mac/Linux)

### Step 4 — Install packages
pip install -r requirements.txt

### Step 5 — Create admin
python seed_admin.py

### Step 6 — Run
python run.py

### Step 7 — Open browser
http://127.0.0.1:5000

## Admin Login
Email:    admin@ticketflow.com
Password: admin123
