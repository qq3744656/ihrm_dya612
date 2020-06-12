import config
import requests


class LoginHandle:
    def __init__(self):
        self.path = "/api/sys/login"
        self.heanders = {"Content-Type": "application/json"}

    def login(self, body={"mobile": 13800000002, "password": 123456}):
        response = requests.post(config.IHRM_URL + self.path, json=body, headers=self.heanders)
        return response

    def get_token(self):
        response = requests.post(config.IHRM_URL + self.path, json={"mobile": 13800000002, "password": 123456},
                                 headers=self.heanders)
        config.TOKEN = "Bearer " + response.json().get("data")
        return config.TOKEN


if __name__ == '__main__':
    lh = LoginHandle()
    print(lh.login().json())
