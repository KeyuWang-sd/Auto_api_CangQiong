import json

import allure
import pytest
import yaml
from api.employee_select_api import EmployeeApi


def load_data():
    with open("./data/employee_select_data.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["test_select_data"]

@allure.epic("苍穹外卖")
@allure.feature("员工查询接口")

class TestEmployeeSelectApi:
    # def __init__(self):
    #     self.employee_api = EmployeeApi(base_url="http://localhost:8081")
    #
    def setup_class(self):
        self.employee_api = EmployeeApi(base_url="http://localhost:8081")

    @allure.story("员工分页查询")
    @allure.title("查询第{page}页，每页{pagesize}条，姓名:{name}")
    @pytest.mark.parametrize("data",load_data())
    @pytest.mark.nondestructive
    def test_select_employee(self, token, data):
        resp = self.employee_api.get_employee_page(
            token=token,
            page=data["page"],
            pagesize=data["page_size"],
            name=data["name"]
        )
        # 打印响应结果
        print("接口响应结果：", resp.json())
        # 主动把响应 JSON 附加到 Allure 报告
        allure.attach(
            body=json.dumps(resp.json(), ensure_ascii=False, indent=2),
            name="接口响应JSON",
            attachment_type=allure.attachment_type.JSON
        )

        # 先获取接口返回的 records 列表
        records= resp.json()["data"]["records"]
        assert len(records) > 0, "返回数据为空"
        first_records = records[0]

        assert first_records["status"] == data["status"]
        assert first_records["name"] == data["name"]


