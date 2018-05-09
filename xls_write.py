#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018/5/2
# @File:xls_write.py

from host_check.split_txt import db_pick_content
import openpyxl,os

xls_path = os.path.join(os.getcwd(),'物联网内容计费主机巡检日报模板.xlsx')
xls_rb = openpyxl.load_workbook(xls_path)
sheet_names = xls_rb.sheetnames
data_sheet_name = sheet_names[0]
data_sheet = xls_rb[data_sheet_name]





data_sheet['D102'] = cell_PSindex
xls_rb.save('test.xlsx')
