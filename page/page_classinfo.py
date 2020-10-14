#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 20:33
# @Author  : Addicated
# @Site    :
# @File    : page_classinfo.py
# @Software: PyCharm
import time
from page.base_page import BasePage
from locator.classinfo_locator import ClassInfoLocator as loc
from pywinauto.keyboard import  send_keys

class ClassInfoPage(BasePage):
	# 进入班级详情页
	def to_classinfo(self):
		self.click_ele(loc.href_toClassInfo, '课堂详情页---点击跳转课堂详情页')

	# 点击作业超链接
	def to_homework(self):
		self.click_ele(loc.href_toTask, '课堂详情页---点击作业超链')

	# 上传作业 通过input框直传文件的方式
	def upload_task_input(self, filename):
		self.click_ele(loc.href_toUploadTaskPage, '课堂详情页---点击转到上传作业详情页')
		self.click_ele(loc.btn_update_submit, '课堂详情页---点击更新提交')
		self.click_ele(loc.btn_update_submit_confirm, "课堂详情页---点击更新提交之后，点击弹框确认")

		self.input_text(loc.input_file, filename, '课堂详情页---上传文件操作')
		time.sleep(2)

	# 上传作业 通过点击的方式来进行上传
	def upload_task_by_click(self,filename):
		self.click_ele(loc.href_toUploadTaskPage, '课堂详情页---点击转到上传作业详情页')
		self.click_ele(loc.btn_update_submit, '课堂详情页---点击更新提交')
		self.click_ele(loc.btn_update_submit_confirm, "课堂详情页---点击更新提交之后，点击弹框确认")

		self.run_js("window.scrollTo(0, document.body.scrollHeight)")
		# ele =self.wait_ele_clickble(loc.btn_window_upload,"课堂详情也---等待通过windows上传文件按钮可点击")
		# ele.location_once_scrolled_into_view()
		time.sleep(1)
		self.click_ele(loc.btn_window_upload,"课堂详情页---点击上传按钮，通过窗口上传")
		time.sleep(2)
		send_keys(filename)
		send_keys('{VK_RETURN}')
	# 通过点击的方式来上传

	# 上传文件后点击更新提交按钮
	def click_to_upload(self):

		self.wait_ele_presence(loc.btn_after_update_submit, "课堂详情也---等待更新按钮可点击")
		self.click_ele(loc.btn_after_update_submit, '课堂详情页---上传文件后点击更新提交按钮')

	# 获取更新作业成功的提示信息
	def get_upload_res(self):
		return self.get_ele_attr(loc.dialog_suceess, '课堂详情页---获取更新作业成功信息', "innerText")

	# 关闭成功提示框的方法
	def close_dialog(self):
		self.click_ele(loc.dialog_success_close, '课堂详情也---关闭更新成功提示框')

	# 作业处留言
	def comment_task(self, comment):
		self.input_text(loc.input_commont, comment, '课堂详情也---输入作业留言')
		self.click_ele(loc.btn_uploadCommont, '课堂详情页---点击上按钮')

	# 查看作业提交状态
	def check_task_status(self):
		pass
