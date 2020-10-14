#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 20:33
# @Author  : Addicated
# @Site    :
# @File    : page_login.py
# @Software: PyCharm
from common.handle_config import conf
from locator.login_locator import LoignLocator as loc
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from page.base_page import BasePage


class LoginPage(BasePage):
	'''登录页面涉及的操作，输入账号，输入密码，点击登录'''
	''''''
	url = conf.get("url", "base_url") + conf.get("url", "login_url")

	def __init__(self, driver):
		super().__init__(driver)
		# 打开登录页面
		self.driver.get(self.url)
		self.driver.implicitly_wait(15)

	def login(self, user, pwd):
		# 登录操作
		self.input_text(loc.acc_input, user, "登录---账号输入")
		self.input_text(loc.pwd_input, pwd, "登录---密码输入")
		self.click_ele(loc.btn_login, "登录---点击登录按钮")

	def get_error_info(self):
		# 获取错误提示信息
		return self.get_ele(loc.erro_info, '登录---获取错误提示信息').text

	def page_refresh(self):
		# 进行页面刷新，方便多次执行用例
		self.driver.get(url=self.url)
