import json

import pytest
import allure
import yaml
from api.login_api import LoginApi

# 读取数据
def load_data():
    with open("./data/login_data.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["test_data"]

@allure.epic("苍穹外卖")
@allure.feature("登录接口")
class TestLoginApi:

    # 初始化接口
    def setup_class(self):
        self.login_api = LoginApi()

    # 数据驱动
    @pytest.mark.parametrize("data", load_data())
    @allure.story("登录测试")
    @pytest.mark.nondestructive
    def test_login(self, data):
        # 1. 发送请求（调用封装的接口，自动拼接完整接口URL）
        resp = self.login_api.login(
            username=data["username"],
            password=data["password"]
        )
        # 主动把响应 JSON 附加到 Allure 报告
        allure.attach(
            body=json.dumps(resp.json(), ensure_ascii=False, indent=2),
            name="接口响应JSON",
            attachment_type=allure.attachment_type.JSON
        )

        # 2. 获取结果
        code = resp.json()["code"]
        msg = resp.json()["msg"]

        # 3. 断言
        assert code == data["expect_code"]
        assert msg == data["expect_msg"]