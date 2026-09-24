
from app.calculator import *
from app.pytest_demo import user, database   


def test_add():
    assert add(10, 20) == 30


def test_subtract():
    assert subtract(50, 25) == 25


def test_greater():
    assert greater(50, 100) is True


def test_even_number():
    assert is_even(10) is True


def test_odd_number():
    assert is_even(7) is False


def test_user(user):
    assert user["id"] == 1


def test_user_username(user):
    assert user["username"] == "aditya"


def test_user_email(user):
    assert user["email"] == "akshay@gmail.com"


def test_database(database):
    print(database)#-s फ्लॅग महत्त्वाचा आहे — त्याशिवाय print() स्टेटमेंट्स दिसणार नाहीत.