import pymysql
from TestAPI.src.utilities.credentialUtilities import CredentialsUtility


class DBUtility(object):

    def __init__(self):

        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()
        self.host = 'localhost'

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                     password=self.creds['db_password'], port=10014)

        return connection

    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_db = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"failed runing the sql: {sql} \n  Error: {str(e)}")

        finally:
            conn.close()
        return rs_db





    def execute_sql(self):

        pass
