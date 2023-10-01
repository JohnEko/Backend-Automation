

import pytest
import logging as logger
import pdb
from TestAPI.src.utilities.requestUtility import RequestUtilities

@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtilities()
    re_api = req_helper.get('customers')
    assert re_api, f'Response of list all customers is empty'

    #pdb.set_trace()

