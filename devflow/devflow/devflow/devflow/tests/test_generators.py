from devflow.utils import random_project

def test_random():
    assert random_project() is not None
