#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018/5/2
# @File:xls_write.py

import split_txt as st
from openpyxl import load_workbook
from openpyxl.styles import Border, Side, NamedStyle, Font, Fill
import os

# 读取excle模板
xls_path = os.path.join(os.getcwd(), '日报模板.xlsx')
xls_wb = load_workbook(xls_path)
xls_ws = xls_wb.worksheets[0]

# 将检查结果填入相应的单元格中
for row in range(2, 106):
    cell = 'D' + str(row)
    count = 0
    for value in st.content:
        value = value.replace('\n', '', count)
        xls_ws[cell] = value
        st.content.pop(0)
        count += 1
        if count != 0:
            break
# 填入结果后，有些单元格格式（线框，字体，填充颜色）有变化，需进行适当调整
# 调整单元格线框
cell_bd = NamedStyle(name="cell_bd")
bd = Side(style='thin', color='000000')
cell_bd.border = Border(left=bd, top=bd, right=bd, bottom=bd)

for row in range(2, 120):
    for col in range(3, 8):
        xls_ws.cell(row, col).style = cell_bd

# 调整单元格字体
cell_ft = NamedStyle(name="cell_ft")
cell_ft.font = Font(size=10, bold=True)

for col in range(1, 8):
    xls_ws.cell(row=1, column=col).font = cell_ft

for row in range(1, 120):
    xls_ws.cell(row=row, column=col).font = cell_ft

cell_ft_else = NamedStyle(name="cell_ft_else")
cell_ft_else.font = Font(size=12)

for row in range(2, 120):
    xls_ws.cell(row=row, column=2).font = cell_ft_else

xls_wb.save('test.xlsx')
