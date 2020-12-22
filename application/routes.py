from application import app, db
from application.models import Cars, Reviews
from application.forms import CarForm, ReviewForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_cars = Cars.query.all()
    output = ""
    return render_template("index.html", title="Home", all_cars=all_cars)

@app.route("/addcar", methods=["GET","POST"])
def addcar(id):
    form = CarForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_car = Cars(
                reg=form.reg.data,
                make=form.make.data,
                model=form.model.data,
                mileage=form.mileage.data,
                colour=form.colour.data,
                age=form.age.data)
            db.session.add(new_car)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("addcar.html", title="Add a Car", form=form)

