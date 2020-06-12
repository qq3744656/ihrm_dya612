import logging
import unittest
from parameterized import parameterized
from api.login import LoginHandle
from utils import get_json, assert_common


class TestLogin(unittest.TestCase):

    @parameterized.expand(get_json("login.json"))
    def test_login(self,info,data,msg):
        logging.info("test %s"% info)
        lh = LoginHandle().login(data)
        assert_common(self, msg, lh.json())