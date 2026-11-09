from datetime import date

import queries

REFERENCE_MAX = 20
ADDRESS_MAX = 200
NOTES_MAX = 1000
STATUSES = ("draft", "complete")


def validate_property(form):
    reference = form.get("reference", "").strip()
    address = form.get("address", "").strip()
    errors = {}

    if not reference:
        errors["reference"] = "Reference is required."
    elif len(reference) > REFERENCE_MAX:
        errors["reference"] = f"Reference must be {REFERENCE_MAX} characters or fewer."
    elif queries.reference_exists(reference):
        errors["reference"] = "That reference is already in use."

    if not address:
        errors["address"] = "Address is required."
    elif len(address) > ADDRESS_MAX:
        errors["address"] = f"Address must be {ADDRESS_MAX} characters or fewer."

    return {"reference": reference, "address": address}, errors


def validate_inspection(form):
    inspection_date = form.get("inspection_date", "").strip()
    notes = form.get("notes", "").strip()
    errors = {}

    if not inspection_date:
        errors["inspection_date"] = "Inspection date is required."
    else:
        try:
            date.fromisoformat(inspection_date)
        except ValueError:
            errors["inspection_date"] = "Enter a valid date."

    if len(notes) > NOTES_MAX:
        errors["notes"] = f"Notes must be {NOTES_MAX} characters or fewer."

    return {"inspection_date": inspection_date, "notes": notes}, errors


def is_valid_status(value):
    return value in STATUSES
