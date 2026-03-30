import pytest
import requests

pytest.mark.nondestructive = pytest.mark.nondestructive


@pytest.fixture(scope="session")
def token():
    """
    全局登录获取token，所有用例共享
    """
    login_url = "http://localhost:8081/api/employee/login"
    login_data = {
        "username": "admin",
        "password": "123456"
    }
    resp = requests.post(login_url, json=login_data)
    return resp.json()["data"]["token"]  # 返回token给所有用例

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:8081"