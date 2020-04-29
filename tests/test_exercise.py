import pytest
from src.pet import Pet
from src.person import Person

def test_exercise():
    lucky = Pet("Lucky", "collie")
    james = Person("James", lucky)

    assert str(james) == "James, has a friend called Lucky (collie)"
