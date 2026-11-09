# Generation prompt

Generate a complete Flask application from the specification below. Follow it exactly. Do not add features, authentication, deployment files or anything listed under Out of scope.

Output the complete application file by file. Before each file, state its path relative to the project root, for example `app.py` or `templates/base.html`. Include every file needed to run it:

- Application code split across several files (for example `app.py`, `db.py`, `routes.py`). No single file over about 150 lines.
- `templates/` with one base template that the other pages extend.
- `requirements.txt` pinned to Flask 3.x.
- `.gitignore` covering `.venv/`, `__pycache__/`, `*.pyc`, `*.db` and `.env`.
- `README.md` with setup and run steps.

Requirements:

- Use the standard library `sqlite3` with parameterised queries only.
- Create the tables on first run.
- Validate: reference is required, unique and at most 20 characters; address is required and at most 200; inspection_date is required; notes is optional and at most 1000; status is only `draft` or `complete`.
- List properties and inspections newest first.
- Use the routes table exactly as written, including paths and methods.

Output only the files and the run instructions.

---

# Property Inspection Application - Specification

## Purpose
Surveyors record inspections of residential properties and mark each one as draft or complete. It replaces paper notes so a surveyor can see every inspection for a property in one place.

## Entities
### Property
- id (integer, primary key)
- reference (text, required, unique, max 20)
- address (text, required, max 200)

### Inspection
- id (integer, primary key)
- property_id (integer, required, references Property)
- inspection_date (date, required)
- status (one of: draft, complete; default draft)
- notes (text, optional, max 1000)
- created_at (timestamp)

## Routes
| Method | Path | Does |
|---|---|---|
| GET | / | List all properties, newest first |
| GET | /property/new | Form to add a property |
| POST | /property | Create a property, redirect to / |
| GET | /property/<id> | Show one property and its inspections, newest first |
| POST | /property/<id>/inspection | Start a draft inspection for the property, redirect to it |
| GET | /inspection/<id> | Show one inspection |
| POST | /inspection/<id>/status | Change status to draft or complete, redirect back |

## Technical constraints
- Python 3.11+, Flask 3.x
- SQLite via the standard library `sqlite3` (no ORM this week)
- Jinja2 templates in `templates/`, one base template
- No authentication this week
- No JavaScript framework

## Out of scope
- User accounts and login
- Inspection questions or measurement sections
- Photographs, PDF reports, file attachments
- Editing or deleting properties or inspections
- An API
