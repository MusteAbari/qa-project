from application import app, db
from application.models import Cars, Reviews
from application.forms import CarForm, ReviewForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_cars = Cars.query.all()
    all_reviews = Reviews.query.all()
    output = ""
    return render_template("index.html", title="Home", all_cars=all_cars, all_reviews=all_reviews)

@app.route("/addcar", methods=["GET","POST"])
def addcar():
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

@app.route("/update/<int:car_id>", methods=["GET", "POST"])
def update(car_id):
    form = CarForm()
    car = Cars.query.filter_by(car_id=car_id).first()
    if request.method == "POST":
        car.reg = form.reg.data
        car.make = form.make.data
        car.model = form.model.data
        car.mileage = form.mileage.data
        car.colour = form.colour.data
        car.age = form.age.data
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("update.html", form=form, title="Update car", car=car)

@app.route("/review/<int:car_id>", methods=["GET", "POST"])
def review(car_id):
    form = ReviewForm()
    car = Cars.query.filter_by(car_id=car_id).first()
    if request.method == "POST":
        if form.validate_on_submit():
            new_review = Reviews(
                name=form.name.data,
                review=form.review.data,
                raiting=form.raiting.data,
                car_id=car_id)
            db.session.add(new_review)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("review.html", form=form, title="Add a Review", review=review)


@app.route("/delete/<int:car_id>", methods=["GET", "POST"])
def delete(car_id):
    car = Cars.query.filter_by(car_id=car_id).first()
    db.session.delete(car)
    db.session.commit()
    return redirect(url_for("home"))