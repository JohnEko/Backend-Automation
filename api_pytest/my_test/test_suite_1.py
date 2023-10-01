import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]
@pytest.mark.smoke
def test_login_page_user():
    print("Login user is Valid")
    print("Login user is not Valid")

@pytest.mark.regression
def test_login_password():
    print("Login password is Valid")
    print("Login password not Valid")
    