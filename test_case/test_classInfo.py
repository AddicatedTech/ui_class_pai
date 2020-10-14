#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 7:54
# @Author  : Addicated
# @Site    : 
# @File    : test_classInfo.py
# @Software: PyCharm
import pytest
import time

from common.handle_logging import log
from selenium import webdriver
from page.page_login import LoginPage
from page.page_userinfo import UserInfoPage
from page.page_classinfo import ClassInfoPage
from common.handle_config import conf
from data.case_data import ClassInfoCase

@pytest.fixture(scope='class')
def op_fixture():
	# 前置需要	登录
	log.info("---------开始执行用户页面操作的用例----------")
	driver = webdriver.Chrome()
	driver.implicitly_wait(15)
	# 需要先登录进入用户主界面
	login_page = LoginPage(driver)
	userinfo_page = UserInfoPage(driver)
	classinfo_page = ClassInfoPage(driver)
	# 登录
	login_page.login(user=conf.get('test_data', 'user'), pwd=conf.get('test_data', 'pwd'))
	userinfo_page.close_welcome()
	yield classinfo_page
	# 每次用例执行结束之后将课程退出，保证环境纯净
	# userinfo_page.exit_class(leave_pwd=conf.get("test_data", 'pwd'))
	time.sleep(1)
	log.info("---------结束----------")
	driver.quit()

class TestClassInfo:

	# 测试上传作业，
	@pytest.mark.parametrize('case',ClassInfoCase.success_upload_data)
	def test_upload_task(self,case,op_fixture):
		classinfo_page = op_fixture
		classinfo_page.to_classinfo()  # 点击跳转课堂详情页面
		classinfo_page.to_homework()  # 点击跳转到作业页面
		# classinfo_page.upload_task_input(case['filename'])
		classinfo_page.upload_task_by_click(case['filename'])
		classinfo_page.click_to_upload()
		res = classinfo_page.get_upload_res()
		classinfo_page.close_dialog()
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
	# 测试留作业评论

	# 测试查看作业状态
