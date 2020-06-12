import config
import requests
from utils import get_token
"""
当前函数封装部门的操作
"""

class DepartmentHandle:
    def __init__(self):
        self.path = config.IHRM_URL + "/api/sys/profile"
        self.path_department = config.IHRM_URL + "/api/company/department"
        self.headers = {"Authorization": get_token(), "Content-Type": "application/json"}

    def get_department(self):
        return requests.post(self.path, headers=self.headers)

    def get_department_info(self, id):
        return requests.get(self.path_department + "/%s" % id, headers=self.headers)

    def delete_department_info(self, id):
        return requests.delete(self.path_department + "/%s" % id, headers=self.headers)

    def put_department_info(self, id, name, code, manager=None, introduce=None, pid=None):
        return requests.put(self.path_department + "/%s" % id, headers=self.headers,
                            json={"name": name, "code": code, "manager": manager, "introduce": introduce, "pid": pid})

    def department_add(self, name, code, manager=None, introduce=None, pid=None):
        return requests.post(self.path_department, headers=self.headers,
                             json={"name": name, "code": code, "manager": manager, "introduce": introduce, "pid": pid})



if __name__ == '__main__':
    dh = DepartmentHandle()
    print(dh.get_department().json())
    print(dh.get_department_info(1271346870031036416).json())
    print(dh.put_department_info(1271346870031036416, "青花会", "001", "青花会职业杀手学校,成功的人生从这里开始").json())
    print(dh.delete_department_info(1271346870031036416).json())
    # print(dh.get_department_info().json())
    # print(type(get_token()))
    print(dh.department_add("zhjdfa", "jyb", "helloworld", "59412b", "1271332552107438080").json())
