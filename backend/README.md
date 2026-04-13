# Moms Groups Backend

Backend API per MVP mobile di un gruppo di mamme.

## Stack

- Python 3.12
- FastAPI
- MySQL
- SQLAlchemy
- Alembic
- JWT authentication

## Avvio locale

Da PowerShell:

```powershell
cd C:\Users\LuciaZarbano\Desktop\STUDY\Moms\app-moms-groups\backend
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py -3.12 main.py
```

Il servizio usa `APP_HOST` e `APP_PORT` dal file `.env`.
Di default parte su:

```text
http://127.0.0.1:8000
```

Endpoint di verifica:

```text
http://127.0.0.1:8000/health
```

Risposta attesa:

```json
{"status":"ok"}
```

## Database

Prima di usare le rotte che accedono al database, avvia MySQL e aggiorna `DATABASE_URL` nel file `.env`:

```env
DATABASE_URL=mysql+pymysql://moms_user:moms_password@127.0.0.1:3306/moms_groups
```
