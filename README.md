# app-moms-groups
Repository for managing mom groups

## Struttura progetto

- `backend`: API FastAPI con MySQL, SQLAlchemy, Alembic e autenticazione JWT
- `frontend`: scaffolding iniziale React Native

## Avvio backend in locale

Apri PowerShell dalla root del progetto e lancia:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Il backend legge host e porta dal file `backend/.env`.
Di default parte su:

```text
http://127.0.0.1:8000
```

Per verificare che il servizio sia attivo, apri:

```text
http://127.0.0.1:8000/health
```

La risposta attesa e':

```json
{"status":"ok"}
```

## Configurazione database

Prima di usare endpoint che leggono o scrivono sul database, assicurati che MySQL sia attivo e aggiorna `backend/.env`:

```env
DATABASE_URL=mysql+pymysql://moms_user:moms_password@127.0.0.1:3306/moms_groups
```

Sostituisci utente, password, host, porta e nome database con i valori del tuo ambiente locale.

## Frontend

La cartella `frontend` contiene la struttura iniziale React Native. Per ora e' uno scaffolding: lo step successivo sara' scegliere se completare il bootstrap con Expo o React Native CLI.
