import logging
import unittest
from parameterized import parameterized
from api.department import DepartmentHandle
from utils import get_json, assert_common


class TestDepartment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lh = DepartmentHandle()

    def test01_get_department(self):
        logging.info("test 组织架构列表")
        response = self.lh.get_department()
        self.assertIn("操作成功", response.json().get("message"))

    @parameterized.expand([["aa","bb","cc","Dd"],["aa1","b1b","c1c","D1d"]])
    def test02_department(self,name,code,put_name,put_code):
        add_info = self.lh.department_add(name,code)
        self.assertEqual(10000,add_info.json().get("code"))
        id = add_info.json().get("data").get("id")
        get_info = self.lh.get_department_info(id)
        self.assertEqual(10000,get_info.json().get("code"))
        put_info = self.lh.put_department_info(id,put_name,put_code)
        self.assertEqual(10000,put_info.json().get("code"))
        del_info = self.lh.delete_department_info(id)
        self.assertEqual(10000,del_info.json().get("code"))

