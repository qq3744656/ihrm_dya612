from BeautifulReport import BeautifulReport

from script.test01_login import TestLogin
import time
import unittest
from config import BASE_DIR
from script.test02_department import TestDepartment

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestDepartment))

# report_name = "report" + ".html"
report_name = time.strftime("%Y%m%d %H%M%S") + ".html"
report_dir = BASE_DIR + "/report"
BeautifulReport(suite).report(description="必填注释", filename=report_name,report_dir=report_dir)