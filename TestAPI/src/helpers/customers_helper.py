
from TestAPI.src.utilities.genericUtilities import generates_random_email_password
from TestAPI.src.utilities.requestUtility import RequestUtilities



class CustomerHelper(object):

    def __init__(self):
        self.requestUtilities = RequestUtilities()


    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            email = generates_random_email_password()
        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(**kwargs)

        cus_created = self.requestUtilities.post('customers', payload=payload, expected_status_code=201)

        return cus_created

