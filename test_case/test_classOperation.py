#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 20:34
# @Author  : Addicated
# @Site    : 
# @File    : test_classOperation.py
# @Software: PyCharm

# 登录之后进入用户页面之后操作课堂信息的测试用例
import pytest
from common.handle_logging import log
from selenium import webdriver
from page.page_login import LoginPage
from page.page_userinfo import UserInfoPage
from common.handle_config import conf
from data.case_data import ClassCase
import time


@pytest.fixture(scope='function')
def op_fixture():
	# 前置需要	登录
	log.info("---------开始执行用户页面操作的用例----------")
	driver = webdriver.Chrome()
	driver.implicitly_wait(15)
	# 需要先登录进入用户主界面
	login_page = LoginPage(driver)
	userinfo_page = UserInfoPage(driver)
	# 登录
	login_page.login(user=conf.get('test_data', 'user'), pwd=conf.get('test_data', 'pwd'))
	userinfo_page.close_welcome()
	yield userinfo_page
	# 每次用例执行结束之后将课程退出，保证环境纯净
	userinfo_page.exit_class(leave_pwd=conf.get("test_data", 'pwd'))
	time.sleep(1)
	log.info("---------结束----------")
	driver.quit()


# 思考，可不可以定义多个前后置方法，对应不同的用例需求
@pytest.fixture(scope='function')
def quit_fixture():
	#  用来测试退出课堂用例的前置
	log.info("----------开始执行测试退出课堂用例---------")
	driver = webdriver.Chrome()
	driver.implicitly_wait(15)
	# 先登录
	login_page = LoginPage(driver)
	userinfo_page = UserInfoPage(driver)
	# 登录
	login_page.login(user=conf.get('test_data', 'user'), pwd=conf.get('test_data', 'pwd'))
	userinfo_page.close_welcome()
	# 进行加入课堂
	userinfo_page.join_class(conf.get('test_data', 'join_code'))
	yield userinfo_page
	driver.quit()


class TestClassOperation:
	@pytest.mark.skip
	@pytest.mark.parametrize('case', ClassCase.success_case_data)
	def test_join_class(self, case, op_fixture):
		userinfo_page = op_fixture
		userinfo_page.join_class(case['join_code'])
		res = userinfo_page.res_join_class()
		print(res)
		try:
			# 判断加课码是否在节点元素内容内，在，则通过，不在则不通过
			assert case['excepted'] == res
		except AssertionError as e:
			log.error(F'-------用例执行失败---case为：{case}--------')
			log.exception(e)
			raise e
		else:
			log.info("---------用例执行通过--------")

	# 测试退出
	@pytest.mark.skip
	@pytest.mark.parametrize('case', ClassCase.quit_class_data)
	def test_quit_class(self, case, quit_fixture):
		userinfo_page = quit_fixture
		userinfo_page.exit_class(case['pwd'])
		# 调用退出方法之后开始进行断言
		res = userinfo_page.res_exit_class()
		print(res)
		try:
			# 判断加课码是否在节点元素内容内，在，则不通过，不在则通过
			assert case['excepted'] == res
		except AssertionError as e:
			log.error(F'-------用例执行失败---case为：{case}--------')
			log.exception(e)
			raise e
		else:
			log.info("---------用例执行通过--------")
