#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 20:33
# @Author  : Addicated
# @Site    :
# @File    : case_data.py
# @Software: PyCharm

class LoginCase:
    """登录功能的用例数据"""
    # 正常登录的用例
    success_case_data = [
        {'user': "414213352@qq.com", "pwd": "1981925d7", "expected": "登录成功"},
    ]
    # 异常的用例数据：错误提示在页面上
    error_case_data = [
        {'user': "42123123", "pwd": "python1", "expected": "1123"},
        {'user': "42123123", "pwd": "123124123", "expected": "1123"},
        {'user': "1231231", "pwd": "", "expected": "1123"},

    ]
# 班级课程操作用例数据
class ClassCase:

    success_case_data = [
        {'join_code': "P69UVV",'excepted':"加入课堂成功"},
    ]
    quit_class_data=[
        {"pwd":'1981925d7','excepted':"课程退课成功"},
        {"pwd" :'12','excepted':"密码错误"},
    ]
class ClassInfoCase:
    success_upload_data = [
        {'filename': r"F:\柠檬班资料\web自动化\ui_class_pai\error_image\用户页面---点击-班级下方更多按钮_1591051542.8233833.png",
         'excepted': "作业提交成功"}
    ]
    error_upload_data=[
        {"upload":"","excepted":""}
    ]
    success_comment_data=[
        {'comment':'','excepted':''}
    ]
    error_comment_data=[
        {'comment':'','excepted':''}
    ]