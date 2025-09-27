\# Flask CRUD API - Student Records (Week 1 Project)



\## Project overview

Simple Flask REST API that implements CRUD operations for managing student records.

Features:

\- Get all students with pagination

\- Get a student by ID

\- Create a new student

\- Update an existing student

\- Delete a student

\- Input validation and basic error handling

\- JSON-based API



\## Project structure

week\_1\_project/

├── main.py

├── requirements.txt

├── pyproject.toml

├── test-api.rest

└── README.md



markdown

Copy code



\## Requirements

\- Python 3.9+

\- `Flask >= 3.1.2`

\- `python-dotenv >= 1.1.1`



\## Installation (pip)

1\. Create and activate a virtual environment:

```bash

python -m venv .venv

\# Linux/Mac

source .venv/bin/activate

\# Windows (PowerShell)

.venv\\Scripts\\Activate.ps1

Install dependencies:



bash

Copy code

pip install -r requirements.txt

(Optional) Create a .env file to override defaults (e.g. PORT or FLASK\_DEBUG).



Run the app (development)

Option A — Run with Python directly (recommended for dev)

bash

Copy code

python main.py

This runs Flask in debug mode on port 5001 by default.



Option B — Using flask CLI

Set the environment variables (example, Linux/macOS):



bash

Copy code

export FLASK\_APP=main.py

export FLASK\_ENV=development

export FLASK\_DEBUG=1

flask run --port=5001

Option C — Run with an ASGI server (uV/uvicorn/hypercorn)

NOTE: Flask 3 aims to be compatible with ASGI; you may run under uvicorn or hypercorn in production-like setups:

Example (if uvicorn is installed):



bash

Copy code

uvicorn main:app --port 5001

