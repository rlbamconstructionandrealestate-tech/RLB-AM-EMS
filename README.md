# RLB-AM-EMS (Asset Management & Enterprise Management System)

A comprehensive management system tailored for construction and real estate operations, handling asset tracking, customer relationships, finances, and project workflows.

## 🚀 Features
- **Asset & Equipment Tracking:** Monitor maintenance schedules, fuel consumption, and rental statuses.
- **CRM & Real Estate:** Manage clients, properties, and rental contracts.
- **Finance & Reports:** Track project expenses, invoices, and generate system-wide reports.
- **Dashboard & Notifications:** Live metrics and automated alerts for system updates.

## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Frontend:** HTML5, CSS3, JavaScript, TailwindCSS / Bootstrap

## 💻 Local Setup Instructions

Follow these steps to run the project locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com
cd RLB-AM-EMS
```

### 2. Set Up Virtual Environment
```powershell
# Create environment
python -m venv venv

# Activate environment (Windows)
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root folder and populate it with your environment keys:
```env
DEBUG=True
SECRET_KEY=your-django-secret-key
```

### 5. Run Database Migrations
```bash
python manage.py migrate
```

### 6. Start the Server
```bash
python manage.py runserver
```
Open your browser and navigate to `http://127.0.0`.

## 🔒 License
This project is proprietary and confidential. Unauthorized copying or distribution is strictly prohibited.
