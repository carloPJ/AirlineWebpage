from flask import Blueprint, render_template, request, flash
from website.models import Flug, Flugzeug
from website import db


@views.route('/flugzeug_erstellen', methods=['GET', 'POST'])
def flugzeug_erstellen():
    if request.method == 'POST':
        modell = request.form.get('Modell')
        hersteller = request.form.get('Hersteller')
        anzahlsitzplaetze = request.form.get('anzahlsitzplaetze')

        new_flugzeug = Flugzeug(modell=modell, hersteller=hersteller, anzahlsitzplaetze=anzahlsitzplaetze)
        db.session.add(new_flugzeug)
        db.session.commit()
        flash('Flugzeug added!', category='success')

    return render_template("Verwaltungspersonal/flugzeug_erstellen.html")
