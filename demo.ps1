# demo.ps1 — start Django (8000) + Angular (4200) in separate terminals

$Root  = Split-Path -Parent $MyInvocation.MyCommand.Path
$Back  = Join-Path $Root "backend"
$Front = Join-Path $Root "frontend"

Write-Host "Starting backend (Django)..." -ForegroundColor Cyan
Start-Process -FilePath "powershell.exe" -ArgumentList @(
  "-NoExit", "-NoLogo", "-Command",
  @"
Set-Location '$Back';
if (Test-Path .\venv\Scripts\activate.ps1) {
  . .\venv\Scripts\activate.ps1
} else {
  python -m venv venv; . .\venv\Scripts\activate.ps1; pip install --upgrade pip; if (Test-Path requirements.txt) { pip install -r requirements.txt }
}
python manage.py migrate
python manage.py runserver
"@
)

Start-Sleep -Seconds 2

Write-Host "Starting frontend (Angular on Node 16)..." -ForegroundColor Cyan
Start-Process -FilePath "powershell.exe" -ArgumentList @(
  "-NoExit", "-NoLogo", "-Command",
  @"
Set-Location '$Front';
nvm use 16.20.2
if (Test-Path package.json) { npm install }
npm start
"@
)

Write-Host ""
Write-Host "---------------------------------------------" -ForegroundColor Green
Write-Host "Backend:  http://127.0.0.1:8000/" -ForegroundColor Green
Write-Host "Frontend: http://localhost:4200/" -ForegroundColor Green
Write-Host "Close the two opened terminals to stop servers." -ForegroundColor Green
Write-Host "---------------------------------------------" -ForegroundColor Green
