import requests



class LoginApi:
    def __init__(self):
        self.login_url = "http://localhost:8081"

    def login(self, username,password):
        url=f'{self.login_url}/api/employee/login'
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(url=url , json=data)
        return response