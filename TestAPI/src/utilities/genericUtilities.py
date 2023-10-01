import logging as logger
import random
import string

def generates_random_email_password(domain=None, email_prefix=None):
    logger.debug("****************Generating random email and password*********************")

    if not domain:
        domain = 'apitest.com'

    if not email_prefix:
        email_prefix = 'customeremail'

    random_email_string_lenght = 10
    random_string = ''.join(random.choices(string.ascii_lowercase,  k=random_email_string_lenght))

    email = email_prefix + '_' + random_string + '@' + domain

    password_lenght = 20
    password_string = ''.join(random.choices(string.ascii_lowercase,  k=password_lenght))


    random_info = {"email" : email, "password" : password_string}
    logger.debug(f"*************Random email and password generated*******************:{random_info}")

    return random_info