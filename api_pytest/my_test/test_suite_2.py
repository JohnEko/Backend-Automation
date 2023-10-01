import pytest
pytestmark = [pytest.mark.fe, pytest.mark.slow]

class TestCheckout(object):

    def test_checkout(self):
        print("Login user is checkout")
        print("Login user failed to checkout")

    def test_check_out_with_user(setup_user):
        print("Check out user is Valid")
        print("Check out products")