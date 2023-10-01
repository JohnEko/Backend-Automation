import os


class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_api_keys():

        wc_key = 'WC_KEYS'
        wc_secret = 'WC_SECRET'

        if not wc_key or not wc_secret:
            raise Exception("The API wc_key and wc_secret must be in ENV")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_credentials():

        db_user = 'admin'
        db_password = 'password1'

        if not db_user or not db_password:
            raise Exception("The Database db_user and db_password must be in ENV")
        else:
            return {'db_user': db_user, 'db_password': db_password}
