from db import get_db


def list_properties():
    return get_db().execute(
        "SELECT id, reference, address FROM property ORDER BY id DESC"
    ).fetchall()


def get_property(property_id):
    return get_db().execute(
        "SELECT id, reference, address FROM property WHERE id = ?",
        (property_id,),
    ).fetchone()


def reference_exists(reference):
    row = get_db().execute(
        "SELECT 1 FROM property WHERE reference = ?", (reference,)
    ).fetchone()
    return row is not None


def create_property(reference, address):
    db = get_db()
    cur = db.execute(
        "INSERT INTO property (reference, address) VALUES (?, ?)",
        (reference, address),
    )
    db.commit()
    return cur.lastrowid


def list_inspections_for_property(property_id):
    return get_db().execute(
        """
        SELECT id, inspection_date, status, created_at
        FROM inspection
        WHERE property_id = ?
        ORDER BY created_at DESC, id DESC
        """,
        (property_id,),
    ).fetchall()


def create_inspection(property_id, inspection_date, notes):
    db = get_db()
    cur = db.execute(
        """
        INSERT INTO inspection (property_id, inspection_date, status, notes)
        VALUES (?, ?, ?, ?)
        """,
        (property_id, inspection_date, "draft", notes),
    )
    db.commit()
    return cur.lastrowid


def get_inspection(inspection_id):
    return get_db().execute(
        """
        SELECT i.id, i.property_id, i.inspection_date, i.status,
               i.notes, i.created_at, p.reference, p.address
        FROM inspection AS i
        JOIN property AS p ON p.id = i.property_id
        WHERE i.id = ?
        """,
        (inspection_id,),
    ).fetchone()


def update_inspection_status(inspection_id, status):
    db = get_db()
    db.execute(
        "UPDATE inspection SET status = ? WHERE id = ?",
        (status, inspection_id),
    )
    db.commit()
