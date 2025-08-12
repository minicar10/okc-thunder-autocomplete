# 🏀 OKC Thunder Autocomplete

A full-stack web application for displaying NBA player statistics with shot chart visualizations, built using **Django REST Framework** (backend) and **Angular** (frontend).  
This version is customized for the Oklahoma City Thunder but can be adapted for other NBA teams.

---

## 📌 Features

- **Autocomplete Search** for player names.
- **Detailed Player Summary** view with:
  - Game-by-game statistics (points, assists, rebounds, steals, blocks, fouls, turnovers, FG/3PT/FT stats).
  - Shot chart visualization with make/miss locations.
- **REST API** powered by Django REST Framework.
- **Responsive UI** built with Angular Material.

---

## 🛠️ Tech Stack

### 🔧 Backend
- Python 3.x  
- Django 4.x  
- Django REST Framework  
- SQLite (default, can be replaced with PostgreSQL)  

### 🎨 Frontend
- Angular 15+  
- Angular Material  
- Node.js (via NVM)  

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

- **Python 3.10+**
- **Node.js** (via [NVM for Windows](https://github.com/coreybutler/nvm-windows))  
  - Node 16.x for Angular  
  - (Optional) Node 20.x for other tooling  
- **npm** (comes with Node.js)
- **Git**
- **PowerShell** (for running demo script)

---

### 2️⃣ Clone the Repository

```
git clone <your-repo-url>
cd okc-thunder-autocomplete
```

---

### 3️⃣ Install Dependencies

#### 🔙 Backend (Django)

```
cd backend
python -m venv venv
.env\Scriptsctivate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

#### 🔜 Frontend (Angular)

```
cd ../frontend
nvm use 16.20.2
npm install
```

---

### 4️⃣ Run the Project

#### ✅ Option A — One Command Demo Script (Recommended)

```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\demo.ps1
```

This opens **two PowerShell windows**:

- Backend → \`http://127.0.0.1:8000/\`
- Frontend → \`http://localhost:4200/\`

---

#### 🛠 Option B — Run Manually

```
# Terminal 1 — Backend
cd backend
.env\Scriptsctivate
python manage.py runserver
```

```
# Terminal 2 — Frontend
cd frontend
nvm use 16.20.2
npm start
```

---

## 📡 API Endpoints

**Example:**

```http
GET /api/v1/playerSummary/1/
```

**Returns:**

```json
{
  "name": "Michael Jordan",
  "games": [
    {
      "date": "2023-02-10",
      "isStarter": true,
      "minutes": 35,
      "points": 38,
      ...
    }
  ]
}
```

---

## 🎯 How to Demo

1. Start the servers with \`.\demo.ps1\`
2. Open \`http://localhost:4200\` in your browser.
3. Search for a player (e.g., **Shai Gilgeous-Alexander**).
4. Select a player to view:
   - 📊 Game statistics table  
   - 🎯 Shot chart with make/miss locations  
5. For raw JSON, go to:  
   \`http://127.0.0.1:8000/api/v1/playerSummary/1/\`

---

## 🧩 Customization

To adapt for a different team:

- 🐍 **Backend:** Change API data source or fixture data.
- 🎨 **Frontend:** Update branding (logos, colors).

To add new stats:

- Modify \`PlayerSummarySerializer\` (backend).
- Update stats table component (Angular).

---

## 📝 License

**MIT License** — free to use and modify for personal or commercial projects.

---

## 👨‍💻 Author

**Zachariah Joseph**  
*CS Student & basketball enthusiast*
