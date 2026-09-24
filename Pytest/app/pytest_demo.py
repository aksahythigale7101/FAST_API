import pytest
from app.calculator import divide, add


# Testing Exceptions
def test_divisor_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 10)


# Pytest Parameters
@pytest.mark.parametrize(
    "a,b,expected", [(10, 10, 20), (50, 25, 25), (500, 500, 1000), (10, 10, 0)]
)
def test_addition(a, b, expected):
    assert add(a, b) == expected


# Pytest Fixture
@pytest.fixture
def user():
    return {"id": 1, "username": "akshay", "email": "akshay@gmail.com"}

@pytest.fixture
def database():
    print("Database setup")
    yield "database connection"
    print("Database cleanup")




