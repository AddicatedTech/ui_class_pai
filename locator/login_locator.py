#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 20:32
# @Author  : Addicated
# @Site    :
# @File    : login_locator.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


class LoignLocator:
	# 账户输入域
	acc_input = (By.XPATH, "//input[@name='account']")
	# 密码输入域
	pwd_input = (By.XPATH, "//input[@name='pass']")
	# 登录按钮
	btn_login = (By.XPATH, "//div[@class='padding-cont pt-login']//a[@class='btn-btn']")

	# 错误提示信息
	erro_info =(By.XPATH,"//p[@class='error-tips']")