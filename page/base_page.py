#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 22:59
# @Author  : Addicated
# @Site    : 
# @File    : base_page.py
# @Software: PyCharm
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.handle_logging import log
from common.handle_path import ERROR_IMG
import os
import time


class BasePage:
	''' 封装公共操作方法 '''

	def __init__(self, driver: WebDriver):
		self.driver = driver

	''' 老三样，三个等待封装 '''

	def wait_ele_visibility(self, locator, img_info, timeout=15, poll_frequency=0.5):
		# 等待元素可见
		st_time = time.time()
		try:
			ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
				EC.visibility_of_element_located(locator))
		except Exception as e:
			log.error("元素--{}--等待可见超时".format(locator))
			log.exception(e)
			# 报错之后进行截图
			self.save_error_image(img_info)
			raise e
		else:
			end_time = time.time()
			log.info("元素--{}--等待成功,等待时间{}秒".format(locator, end_time - st_time))
			return ele

	def wait_ele_clickble(self, locator, img_info, timeout=15, poll_frequency=0.5):
		# 可点击
		st_time = time.time()
		try:
			ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
				EC.element_to_be_clickable(locator))
		except Exception as e:
			log.error("元素--{}--等待可点击超时".format(locator))
			log.exception(e)
			# 截图方法
			self.save_error_image(img_info)
			raise e
		else:
			end_time = time.time()
			log.info("元素--{}--等待成功,等待时间{}秒".format(locator, end_time - st_time))
			return ele

	def wait_ele_presence(self, locator, img_info, timeout=15, poll_frequency=0.5):
		# 等待元素被加载出来
		st_time = time.time()
		try:
			ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
				EC.presence_of_element_located(locator))
		except Exception as e:
			log.error("元素--{}--等待被加载超时".format(locator))
			log.exception(e)
			# 截图方法
			self.save_error_image(img_info)
			raise e
		else:
			end_time = time.time()
			log.info("元素--{}--等待成功,等待时间{}秒".format(locator, end_time - st_time))
			return ele

	def save_error_image(self, img_info):
		# 错误信息截图方法
		record_time = time.time()
		img_name = F'{img_info}_{record_time}.png'  # 拼接图片名 主要包含用例执行信息，执行时间
		file_path = os.path.join(ERROR_IMG, img_name)  # 拼接组成文件路径
		self.driver.save_screenshot(file_path)  # 调用方法进行保存
		log.info(F"错误页面截屏成功，保存路径为{file_path}")

	''' 元素操作相关封装基础方法 '''

	# 思考都有哪些需要封装，输入，点击，获取元素节点的文本，属性，上传文件，
	# 向元素输入内容
	def input_text(self, locator, input, img_info):
		try:
			self.driver.find_element(*locator).send_keys(input)
		except Exception as e:
			# 输出日志
			log.error("输入文本--{}--失败".format(locator))
			log.exception(e)
			# 对当前页面进行截图
			# filename = '{}_{}.png'.format(img_info, start_time)
			# file_path = os.path.join(ERROR_IMG, filename)
			self.save_error_image(img_info)
			raise e
		else:
			log.info(F"文本内容输入--{locator}--成功")

	# 获取到元素节点
	def get_ele(self, locator, img_info):
		try:
			ele = self.driver.find_element(*locator)
		except Exception as e:
			log.error(F"获取元素--{locator}--失败")
			log.exception(e)
			# 进行截图
			self.save_error_image(img_info)
		else:
			log.info(F"元素--{locator}--获取成功")
			return ele

	# 点击元素
	def click_ele(self, locator, img_info):
		try:
			ele = self.driver.find_element(*locator).click()
		except Exception as e:
			log.error(F"点击元素--{locator}--失败")
			log.exception(e)
			# 进行截图
			self.save_error_image(img_info)
		else:
			log.info(F"元素--{locator}--点击成功")

	# 根据传入参数获取元素节点内的内容
	def get_ele_attr(self, locator, img_info, attr_name):
		try:
			ele = self.driver.find_element(*locator)
			attr_value = ele.get_attribute(attr_name)
		except Exception as e:
			# 输出日志
			log.error(F"获取元素--{locator}--属性失败")
			log.exception(e)
			# 对当前页面进行截图
			self.save_error_image(img_info)
			raise e
		else:
			log.info(F"获取元素--{locator}--属性成功")
			return attr_value

	# 封装一个执行js代码的操作
	def run_js(self,script):
		self.driver.execute_script(script)