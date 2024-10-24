import os
from .user import User
from .bigquery_api import BigQueryAPI


class CredentialsAPI():
    def __init__(self):
        self.__client = BigQueryAPI()

    def username_and_password_match(self, username, password_hash) -> bool:
        sql = f"""
        SELECT 
            COUNT(*) AS ct
        FROM 
            {os.getenv('BQ_DATASET_ID')}.{os.getenv('BQ_CREDENTIALS_TABLE')}      
        WHERE 
            UserName = '{username}' AND PasswordHash = '{password_hash}'     
        """
        df = self.__client.sql_to_pandas(sql)
        if df['ct'][0] == 1:
            return True
        else:
            return False
        
    
    def init_user(self, username, password_hash) -> User:
        sql = f"""
        SELECT
            KeyUserId,
            UserName,
            Role,
            PasswordHash
        FROM 
            {os.getenv('BQ_DATASET_ID')}.{os.getenv('BQ_CREDENTIALS_TABLE')} 
        WHERE 
            UserName = '{username}' AND PasswordHash = '{password_hash}'
        """
        df = self.__client.sql_to_pandas(sql)
        if df.shape[0] == 1:
            return User(id=df['KeyUserId'][0] ,name=df['UserName'][0], role=df['Role'][0], is_logged_in=True)
        else:
            return User(-1, '', '', False)
        
    


    

    