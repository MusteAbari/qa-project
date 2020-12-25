import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Cars, Reviews

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
        test_car = Cars(
            reg= "P744AAY", 
            make="Mazda", 
            model="Xedos", 
            mileage=80000, 
            age=1995, 
            colour="Navy" 
        )
        db.session.add(test_car)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_addcar_get(self):
        response = self.client.get(url_for('addcar'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', car_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', car_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class TestRead(TestBase):
    def test_read_task(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"Mazda", response.data)

class TestCreate(TestBase):
    def test_addcar_task(self):
        response = self.client.post(
            url_for("addcar"),
            data=dict(reg="P744AAY"),
            follow_redirects=True
        )
        self.assertIn(b"P744AAY", response.data)
    
class TestUpdate(TestBase):
    def test_update_task(self):
        response = self.client.post(
            url_for("update", car_id=1),
            data=dict(reg="SK06XKD",
            make="Mazda", 
            model="Xedos", 
            mileage=80000, 
            age=1995, 
            colour="Navy"),
            follow_redirects=True
        )
        self.assertIn(b"SK06XKD", response.data)

class TestDelete(TestBase):
    def test_delete_task(self):
        response = self.client.get(
            url_for("delete", car_id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"P744AAY", response.data)