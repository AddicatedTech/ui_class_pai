#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 20:33
# @Author  : Addicated
# @Site    : 
# @File    : userinfo_locator.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


class UserInfoLocator:
	# 关闭重要提醒
	show_alert = (By.XPATH, "//a[@class='close']")
	# 退出登录 相关操作
	btn_quit_avatar = (By.XPATH, "//img[@class='avatar']")
	# 退出登录
	btn_quit_link = (By.XPATH, "//a[@class='link logout']")

	# 加入班级按钮
	btn_join_class = (By.XPATH, "//div[@class='ktcon1l fr']")
	# 加入课程弹框 用于等待或者判断
	alert_join_class = (By.XPATH, "//div[@class='chuangjiankctop']")
	# 加课码输入框
	input_joinClass = (By.XPATH, "//div[@class='chuangjiankccon']//input")
	# 加课码输入确认按钮
	btn_confirm_join = (By.XPATH, "//li[@class='cjli2']//a[@class='btn btn-positive']")
	# 班级更多按钮
	btn_class_detail = (By.XPATH, "//dt[@class='bgclass1']//a[@class='kdmore']//span")
	# 加课码元素定位 去得到的字符串为  加课码：P69UVV
	# join_code_info = (By.XPATH, "//dt[@class='bgclass1']//p[1]")
	# 退课按钮
	btn_class_leave = (By.XPATH, "//dt[@class='bgclass1']//li[@class='kdli3']//a")
	# 退课弹框 用作等待或者判断
	alert_leave_class = (By.XPATH, "//div[@class='deletecon cl']//p//span")
	# 退课密码输入框
	input_leaveClass = (By.XPATH, "//div[@class='deletekccon']//input")
	# 退课确认按钮
	btn_confirm_leave = (By.XPATH, "//li[@class='dli2']//a[@class='btn btn-positive']")
	# 进入班级详情
	btn_inClassDetail = (By.XPATH, "//dt[@class='bgclass1']//a[@class='jumptoclass']")

	# 课程加入，退出，已添加课程提示框
	show_tip = (By.XPATH, "//div[@id='show-tip']/span")

	# 已添加的错误提示框
	error_tip = (By.XPATH, "//div[@id='error-tip']/span")
