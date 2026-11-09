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
