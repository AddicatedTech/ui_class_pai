#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 18:10
# @Author  : Addicated
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm

from page.page_login import LoginPage
from page.page_userinfo import UserInfoPage
from common.handle_logging import log
from selenium import webdriver
from data.case_data import LoginCase
import pytest


@pytest.fixture(scope="class")
def fixture():
	log.info("--------------开始执行登录的用例----------")
	driver = webdriver.Chrome()
	login_page = LoginPage(driver)
	userInfo_page = UserInfoPage(driver)
	yield login_page, userInfo_page
	driver.quit()
	log.info("---------------登录的测试用例执行完毕-------")


class TestLogin:
	''' 思考需要的前置
	    并且吧前置给分出去
	    使用到 loginPage，userInfoPage两个页面，
	    要使用前置方法生成两个页面的对象'''

	# 正常登录用例
	@pytest.mark.skip
	@pytest.mark.parametrize("case", LoginCase.success_case_data)
	def test_login_pass(self, case, fixture):
		login_page, userInfo_page = fixture
		login_page.login(case["user"], case["pwd"])
		# 实际执行结果
		res = userInfo_page.get_welcome()
		try:
			# 断言登录成功的条件
			assert "登录成功" == res
		except AssertionError as e:
			log.error(F'-------用例执行失败---case为：{case}--------')
			log.exception(e)
			raise e
		else:
			log.info("---------用例执行通过--------")
			# 退出登录。重新访问登录页面
			userInfo_page.quit_login()
			# 重新进入登录页面
			login_page.page_refresh()

	@pytest.mark.skip
	@pytest.mark.parametrize("case", LoginCase.error_case_data)
	def test_login_error(self, case, fixture):
		'''异常用例，窗口上会有提示'''
		login_page, userinfo_page = fixture
		# 刷新页面提高用例执行效率
		login_page.page_refresh()

		login_page.login(case['user'], case['pwd'])
		res = login_page.get_error_info()
		try:
			# 因为每次登录失败错误信息都不同，
			assert res != None
		except AssertionError as e:
			log.error(F'-------用例执行失败---case为：{case}--------')
			log.exception(e)
			raise e
		else:
			log.info("---------用例执行通过--------")
