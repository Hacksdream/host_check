#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018/5/2
# @File:xls_write.py

import host_check.split_txt as st
import openpyxl
import os

xls_path = os.path.join(os.getcwd(),'日报模板.xlsx')

xls_rb = openpyxl.load_workbook(xls_path)
sheet_names = xls_rb.sheetnames
data_sheet_name = sheet_names[0]
data_sheet = xls_rb[data_sheet_name]


# #wlwjfx1主机巡检结果
# data_sheet['D2'] = st.file_jfx1
# data_sheet['D3'] = st.cpu_jfx1
# data_sheet['D4'] = st.mem_jfx1
# data_sheet['D5'] = st.io_jfx1
#
# #wlwjfx2主机巡检结果
# data_sheet['D6'] = st.file_jfx2
# data_sheet['D7'] = st.cpu_jfx2
# data_sheet['D8'] = st.mem_jfx2
# data_sheet['D9'] = st.io_jfx2
#
# #wlwjfx3主机巡检结果
# data_sheet['D10'] = st.file_jfx3
# data_sheet['D11'] = st.cpu_jfx3
# data_sheet['D12'] = st.mem_jfx3
# data_sheet['D13'] = st.io_jfx3
#
# #wlwjfx4主机巡检结果
# data_sheet['D14'] = st.file_jfx4
# data_sheet['D15'] = st.cpu_jfx4
# data_sheet['D16'] = st.mem_jfx4
# data_sheet['D17'] = st.io_jfx4
#
# #wlwjfx5主机巡检结果
# data_sheet['D18'] = st.file_jfx5
# data_sheet['D19'] = st.cpu_jfx5
# data_sheet['D20'] = st.mem_jfx5
# data_sheet['D21'] = st.io_jfx5
#
# #wlwjfx6主机巡检结果
# data_sheet['D22'] = st.file_jfx6
# data_sheet['D23'] = st.cpu_jfx6
# data_sheet['D24'] = st.mem_jfx6
# data_sheet['D25'] = st.io_jfx6
#
# #wlwdxx1主机巡检结果
# data_sheet['D26'] = st.file_dxx1
# data_sheet['D27'] = st.cpu_dxx1
# data_sheet['D28'] = st.mem_dxx1
# data_sheet['D29'] = st.io_dxx1
#
# #wlwdxx2主机巡检结果
# data_sheet['D30'] = st.file_dxx2
# data_sheet['D31'] = st.cpu_dxx2
# data_sheet['D32'] = st.mem_dxx2
# data_sheet['D33'] = st.io_dxx2
#
# #wlwbyx1主机巡检结果
# data_sheet['D34'] = st.file_byx1
# data_sheet['D35'] = st.cpu_byx1
# data_sheet['D36'] = st.mem_byx1
# data_sheet['D37'] = st.io_byx1
#
# #wlwbyx2主机巡检结果
# data_sheet['D38'] = st.file_byx2
# data_sheet['D39'] = st.cpu_byx2
# data_sheet['D40'] = st.mem_byx2
# data_sheet['D41'] = st.io_byx2
#
# #wlwccx1主机巡检结果
# data_sheet['D42'] = st.file_ccx1
# data_sheet['D43'] = st.cpu_ccx1
# data_sheet['D44'] = st.mem_ccx1
# data_sheet['D45'] = st.io_ccx1
#
# #wlwccx2主机巡检结果
# data_sheet['D46'] = st.file_ccx2
# data_sheet['D47'] = st.cpu_ccx2
# data_sheet['D48'] = st.mem_ccx2
# data_sheet['D49'] = st.io_ccx2
#
# #wlwccx2主机巡检结果
# data_sheet['D50'] = st.file_ccx3
# data_sheet['D51'] = st.cpu_ccx3
# data_sheet['D51'] = st.mem_ccx3
# data_sheet['D52'] = st.io_ccx3
#
# #wlwjs7主机巡检结果
# data_sheet['D53'] = st.file_js7
# data_sheet['D54'] = st.cpu_js7
# data_sheet['D55'] = st.mem_js7
# data_sheet['D56'] = st.io_js7
#
# #wlwjs8主机巡检结果
# data_sheet['D57'] = st.file_js8
# data_sheet['D58'] = st.cpu_js8
# data_sheet['D59'] = st.mem_js8
# data_sheet['D60'] = st.io_js8

xls_rb.save('test.xlsx')
