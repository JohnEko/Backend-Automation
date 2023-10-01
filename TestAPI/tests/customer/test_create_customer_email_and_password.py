import pytest
import logging as logger
from TestAPI.src.utilities.genericUtilities import generates_random_email_password
from TestAPI.src.helpers.customers_helper import CustomerHelper
from TestAPI.src.databasetesting.customer_dao import CustomerDao
from TestAPI.src.utilities.requestUtility import RequestUtilities
import pdb



@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("***************New Customer Created*********************")

    random_info = generates_random_email_password()
    logger.info(random_info)


    email = random_info['email']
    password =random_info['password']


    #create a payload that will generate our customer email and password and

    #make a call from the payload
    cust_obj = CustomerHelper()
    cust_obj_info = cust_obj.create_customer(email=email, password=password)


   #verify email and first name in the response
    assert cust_obj_info['email'] == email, f'The Customer email is wrong: {email} make sure is write email'
    #assert cust_obj_info['display_name'] == '', f'Customer created first name is empty, Customer need to add is firstname'


    #DATABASE TESTING
    #verify customer is created in the database
    cust_dao = CustomerDao()
    cust_info = cust_dao.get_customer_email(email)

    #pdb.set_trace()

    #verify customer "id, email and name" is same in the database as on the API
    cust_id_api = cust_obj_info['id']
    cust_id_db = cust_info[0]['ID'] #get the list of list in the db

    assert cust_id_api == cust_id_db, f'Customer ID response in API not as same in Database' \
                                      f'Email: {email}'


#@pytest.mark.tcid31
#def create_customer_with_existing_email_to_fail():
#Testing a particular customer from the database
    cust_dao = CustomerDao()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    # make a call from the API
    req_obj = RequestUtilities()
    payload = {
        "email" : existing_email,
        "password": "Password1"
    }
    cust_obj_info = req_obj.post(endpoint="customers", payload=payload, expected_status_code=400)

    assert cust_obj_info['code'] == 'registration-error-email-exists' f"Create customer already have an existing email" \
                              f"Expected: 'registration-error-email-exists' But actual: {cust_obj_info['code'] }"

    assert cust_obj_info['message'] == 'An email is registration with this account' f"Create customer already have an existing email" \
                                    f"Expected: 'An email is registration with this account' But actual: {cust_obj_info['code']}"

    pdb.set_trace()
