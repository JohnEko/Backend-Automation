
from TestAPI.src.utilities.dbUtility import DBUtility
import random

import pdb
class CustomerDao(object):

    def __init__(self):

        self.db_helper = DBUtility()

    def get_customer_email(self, email):

        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_random_customer_from_db(self, qty=1):

        sql = "SELECT * FROM local.wp_users order by id desc limit 200;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))