#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 20:33
# @Author  : Addicated
# @Site    : 
# @File    : classmate_locator.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
class ClassMateLocator:

	# 全部学生索引
	btn_allStudents=(By.XPATH,"//li[@class='all']")
	# 学生私聊按钮  应该考虑随机发私信的情况
	btn_chat =(By.XPATH,"//div[@class='member-page cWidth']//li[4]//a[1]")
	# 私信编辑区
	input_editMsg=(By.XPATH,"//textarea[@class='ps-container']")
	# 发送私信按钮
	btn_sendMsg=(By.XPATH,"//a[@class='btn btn-positive']")
	# 聊天记录区域  # 如何进行断言需要思考
	log_chat=(By.XPATH,"//li[1]//div[1]//div[1]")