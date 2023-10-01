import pytest


@pytest.fixture(scope='module')
@pytest.mark.smoke
def setup_user():
    print("Login user is Valid")
    print("Login user is not Valid")

def test_checksetup(setup_user):
        print("Login user is checkout")
        print("Login user failed to checkout")


def test_with_user(setup_user):
        print("Check out user is Valid")
        print("Check out products")