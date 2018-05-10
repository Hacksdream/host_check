#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018/5/2
# @File:xls_write.py

import split_txt as st
import openpyxl
import os

xls_path = os.path.join(os.getcwd(), '日报模板.xlsx')

xls_rb = openpyxl.load_workbook(xls_path)
sheet_names = xls_rb.sheetnames
data_sheet_name = sheet_names[0]
data_sheet = xls_rb[data_sheet_name]

for row in range(2, 106):
    cell = 'D' + str(row)
    count = 0
    for value in st.content:
        value = value.replace('\n', '', count)
        data_sheet[cell] = value
        st.content.pop(0)
        count += 1
        if count != 0:
            break
xls_rb.save('test.xlsx')
