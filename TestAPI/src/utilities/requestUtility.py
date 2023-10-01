import os
import requests
from requests_oauthlib import OAuth1
import json
import logging as logger
from TestAPI.src.configuration.hosts_config import API_HOST
from TestAPI.src.utilities.credentialUtilities import CredentialsUtility

import pdb

class RequestUtilities(object):

    def __init__(self):

        self.env = os.environ.get("ENV", "test")
        self.base_url = API_HOST[self.env]
        cred = CredentialsUtility.get_api_keys()
        self.auth =OAuth1(cred['wc_key'], cred['wc_secret'])

    def assert_status_code(self):
        self.status_code = self.expected_status_code, f"Bad status code." \
            f"Expected status code{self.expected_status_code}, But actual status code: {self.status_code}," \
            f"URL: {self.url}, Response Json: {self.rs_json}"



    def post(self, endpoint, payload=None, headers=None,  expected_status_code=200):


        if not headers:
            headers = {
                "Content-Type": "application/json"
            }
        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.info(f"API POST response: {self.rs_json}")
        #pdb.set_trace()
        return rs_api.json()



    def get(self, endpoint, payload=None, headers=None,  expected_status_code=200):
        if not headers:
            headers = {
                "Content-Type": "application/json"
            }
        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        # pdb.set_trace()
        logger.info(f"API GET response: {self.rs_json}")
        return rs_api.json()