import json
import requests
from error_message import ErrorMessage

class PyNMB:

    OBP_host = "https://obp-api-sandbox.nmbbank.co.tz"
    bank_id = "nmbb.01.tz.nmbb"


    def __init__(self):
        """
            Initialize ErrorMessage class.
            Get Consumer key from consumer_key.json file.
        """
        self.err_msg = ErrorMessage()
        try:
            with open('consumer_key.json', 'r') as json_file:
                data = json.load(json_file)
                if 'consumer_key' in data:
                    self.consumer_key = data['consumer_key']
                else:
                    self.key_error_msg = self.err_msg.consumer_key_not_found
        except:
            self.key_error_msg = self.err_msg.consumer_key_file_not_found
            

    def login(self, username, password):
        """
            Login with username and password.
        """
        try:
            response = requests.post(f"{self.OBP_host}/my/logins/direct", headers = {'Authorization':f'DirectLogin username={username}, password={password}, consumer_key={self.consumer_key}', 'Content-Type':'application/json'})
            return response.json()
        except AttributeError:
            return self.error_msg(self.key_error_msg)
        except requests.exceptions.RequestException as e:
            return self.error_msg(self.err_msg.request_error_msg)


    def getBranches(self):
        """
            Get NMB registered branches.
        """
        response = requests.get(f"{self.OBP_host}/obp/v4.0.0/banks/{self.bank_id}/branches")
        return response.json()

    
    def error_msg(self, msg):
        """Jsonify error message."""
        return {"message": msg}