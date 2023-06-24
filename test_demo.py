import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_demo(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        print("当前页面的url:{}".format(self.driver.current_url))
        # self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        # self.driver.get("http://www.baidu.com")

    def test_js(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element("xpath","")
        self.driver.execute_script()  #执行javascript代码


