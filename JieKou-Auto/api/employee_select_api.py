import requests

class EmployeeApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_employee_page(self, token, page=1, pagesize=10, name=None):
        """
                员工分页查询接口
                :param token: 登录token（从conftest fixture传递）
                :param page: 页码，默认1
                :param pagesize: 每页条数，默认10
                :param name: 员工姓名（可选，用于模糊查询）
                :return: requests响应对象
                """

        url = f"{self.base_url}/api/employee/page"
        headers = {"token": token}  # 把token放到请求头
        params = {
            "page": page,
            "pageSize": pagesize,
            "name": name
        }
        res=requests.get(url, headers=headers, params=params)
        return res