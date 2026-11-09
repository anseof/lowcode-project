# Property Inspections

A Flask app for surveyors to record inspections of residential properties and mark each one as draft or complete. It uses the standard library `sqlite3` and has no authentication.

Requires Python 3.11 or later.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Then open http://127.0.0.1:5000. Alternatively, run `flask --app app run`.

The tables are created in `inspections.db` on first run.

## Notes on behaviour

- Properties list newest first by id, because the Property entity has no timestamp.
- Inspections list newest first by creation time, with id as the tiebreaker.
- Starting an inspection requires a date. Notes are optional and can be entered at that point, since editing is out of scope.
- Changing a status redirects to the inspection page.
