#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2020/5/30 20:33
# # @Author  : Addicated
# # @Site    :
# # @File    : classinfo_locator.py
# # @Software: PyCharm
from selenium.webdriver.common.by import By


class ClassInfoLocator:
	# 加课码div，跳转后进行判断
	join_code = (By.XPATH, "//body//div[@class='topm cl']//div//div[2]")
	# 跳转到classinfo
	href_toClassInfo =(By.XPATH,"//a[contains(text(),'python-web')]")

	# 作业超链
	href_toTask = (By.XPATH, "//div[@class='banner cl coursebanner coursebannernew']//a[2]")
	# 上传作业页面跳转btn
	href_toUploadTaskPage = (By.XPATH, "//a[contains(text(),'20191126-')]")
	# 添加作业btn
	# btn_uploadTask = (By.XPATH, "//a[@class='sc-btn webuploader-container']//div[@class='webuploader-pick']")
	# 文件上传的按钮
	# btn_window_upload =(By.XPATH,"//a/div[contains(text(),'添加作业文件')]")
	btn_window_upload =(By.XPATH,"//a[@class='sc-btn webuploader-container']")
	#  更新提交按钮，在第一次提交之后，会自动更新变成更新提交按钮
	btn_update_submit=(By.XPATH,"//a[contains(text(),'更新提交')]")
	# 上传后更新提交按钮
	btn_after_update_submit=(By.XPATH,"(//a[contains(text(),'更新提交')])[last()]")
	# 更新作业弹框确认按钮  最好进行一次等待
	btn_update_submit_confirm =(By.XPATH,"//div[@class='btns']//a[@class='sure active']")
	# 上传作业的input
	input_file = (By.XPATH, "(//input[@type='file'])[2]")
	# 提交成功之后的弹框提示
	dialog_suceess=(By.XPATH,"//div[@class='weui_dialog_bd']")
	# 提交成功后弹框提示关闭
	dialog_success_close=(By.XPATH,"//a[@class='weui_btn_dialog primary']")
	# 作业留言输入框
	input_commont = (By.XPATH, "//textarea[@id='comment']")
	# 提交留言按钮
	btn_uploadCommont = (By.XPATH, "//div[@class='work-message2 clearfix']//a[@class='sure active']")
	# 查看作业提交日志
	btn_checkLog = (By.XPATH, "//a[@class='togglesee']")

	# 跳转同学页面
	href_toClassMate = (By.XPATH, "//a[contains(text(),'107')]")
