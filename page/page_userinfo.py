#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 20:33
# @Author  : Addicated
# @Site    :
# @File    : page_userinfo.py
# @Software: PyCharm
from page.base_page import BasePage
from locator.userinfo_locator import UserInfoLocator as loc
import time


class UserInfoPage(BasePage):

	# 获取登录欢迎弹框
	def get_welcome(self):
		try:
			self.wait_ele_clickble(loc.show_alert, "用户页面----等待欢迎弹窗")
		except:
			return "登录失败"
		else:
			return "登录成功"

	# 关闭欢迎弹框操作
	def close_welcome(self):
		self.wait_ele_clickble(loc.show_alert, "用户页面----等待-欢迎弹窗")
		self.click_ele(loc.show_alert, '用户页面---点击-关闭欢迎弹框')

	def quit_login(self):
		self.wait_ele_clickble(loc.show_alert, "用户页面----等待-欢迎弹窗")
		self.click_ele(loc.show_alert, "用户页面----点击-关闭欢迎弹框")
		self.wait_ele_clickble(loc.btn_quit_avatar, '用户页面----等待-头像可点击')
		self.click_ele(loc.btn_quit_avatar, "用户页面----点击-用户头像")
		self.click_ele(loc.btn_quit_link, "用户页面----点击-用户头像之后，登出")

	# 点击输入加课码，加课
	def join_class(self, join_code):
		self.click_ele(loc.btn_join_class, "用户页面---点击加课按钮")
		self.input_text(loc.input_joinClass, join_code, '用户页面----输入加课码')
		self.click_ele(loc.btn_confirm_join, "用户页面----点击确认加课按钮")

	# 得到加入课堂后的结果 加入课堂成功
	def res_join_class(self):
		self.wait_ele_visibility(loc.show_tip, '用户页面---等待加课成功后回显页面')
		return self.get_ele_attr(loc.show_tip, '用户页面---获取加课成功后的回显', "innerText")

	# 输入密码，退课
	def exit_class(self, leave_pwd):
		self.click_ele(loc.btn_class_detail, "用户页面---点击-班级下方更多按钮")
		self.click_ele(loc.btn_class_leave, '用户页面---点击-退课按钮点击')
		self.input_text(loc.input_leaveClass, leave_pwd, '用户页面---退课输入密码')
		self.wait_ele_clickble(loc.btn_confirm_leave, '用户界面---等待-确认退课按钮可点击')
		self.click_ele(loc.btn_confirm_leave, '用户页面---点击-确认退课按钮')
		time.sleep(2)

	# 得到退出课堂后的回显 提示为 课程退课成功
	def res_exit_class(self):
		self.wait_ele_visibility(loc.show_tip, '用户页面---等待退课成功后显示提示框')
		return self.get_ele_attr(loc.show_tip, '用户页面---获取退课之后的回显', "innerText")
