import pytest
import os

def test_exercise():
    os.chdir('src')

    from pet import Pet
    from person import Person
    lucky = Pet("Lucky", "collie")
    james = Person("James", lucky)

    assert str(james) == "James, has a friend called Lucky (collie)"
