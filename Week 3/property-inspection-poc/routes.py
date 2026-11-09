import sqlite3

from flask import Blueprint, abort, redirect, render_template, request, url_for

import queries
from validation import is_valid_status, validate_inspection, validate_property

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    return render_template("index.html", properties=queries.list_properties())


@bp.get("/property/new")
def new_property():
    return render_template("property_new.html", values={}, errors={})


@bp.post("/property")
def create_property():
    values, errors = validate_property(request.form)
    if errors:
        return render_template("property_new.html", values=values, errors=errors), 400
    try:
        queries.create_property(values["reference"], values["address"])
    except sqlite3.IntegrityError:
        errors["reference"] = "That reference is already in use."
        return render_template("property_new.html", values=values, errors=errors), 400
    return redirect(url_for("main.index"))


@bp.get("/property/<int:property_id>")
def show_property(property_id):
    return _render_property(property_id, values={}, errors={})


@bp.post("/property/<int:property_id>/inspection")
def start_inspection(property_id):
    if queries.get_property(property_id) is None:
        abort(404)
    values, errors = validate_inspection(request.form)
    if errors:
        return _render_property(property_id, values, errors, status=400)
    inspection_id = queries.create_inspection(
        property_id, values["inspection_date"], values["notes"] or None
    )
    return redirect(url_for("main.show_inspection", inspection_id=inspection_id))


@bp.get("/inspection/<int:inspection_id>")
def show_inspection(inspection_id):
    inspection = queries.get_inspection(inspection_id)
    if inspection is None:
        abort(404)
    return render_template("inspection.html", inspection=inspection)


@bp.post("/inspection/<int:inspection_id>/status")
def change_status(inspection_id):
    if queries.get_inspection(inspection_id) is None:
        abort(404)
    status = request.form.get("status", "")
    if not is_valid_status(status):
        abort(400)
    queries.update_inspection_status(inspection_id, status)
    return redirect(url_for("main.show_inspection", inspection_id=inspection_id))


def _render_property(property_id, values, errors, status=200):
    prop = queries.get_property(property_id)
    if prop is None:
        abort(404)
    html = render_template(
        "property.html",
        prop=prop,
        inspections=queries.list_inspections_for_property(property_id),
        values=values,
        errors=errors,
    )
    return html, status
