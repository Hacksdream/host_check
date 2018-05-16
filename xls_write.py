#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018/5/2
# @File:xls_write.py

import split_txt as st
from openpyxl import load_workbook
from openpyxl.styles import Border, Side, NamedStyle, Font, Fill, Alignment
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
cell_bd = NamedStyle(name="cell_bd")
bd = Side(style='thin', color='000000')
cell_bd.border = Border(left=bd, top=bd, right=bd, bottom=bd)
# 设置单元格左对齐居中，自动换行
al1 = Alignment(horizontal="left", vertical="center", wrap_text=True)
al2 = Alignment(horizontal="center", vertical="center", wrap_text=True)

# 调整单元格线框，自动换行
for row in range(2, 120):
    for col in range(1, 8):
        xls_ws.cell(row, col).style = cell_bd
        xls_ws.cell(row, col).alignment = al1

for row in range(2, 120):
    xls_ws.cell(row=row, column=5).alignment = al2
# 调整单元格字体
for col in range(1, 8):
    xls_ws.cell(row=1, column=col).font = Font(size=10, bold=True)

for row in range(1, 120):
    xls_ws.cell(row=row, column=1).font = Font(size=10, bold=True)

for row in range(2, 120):
    xls_ws.cell(row=row, column=2).font = Font(size=12)

for row in range(2, 120):
    for col in range(3, 8):
        xls_ws.cell(row=row, column=col).font = Font(size=9)

# 网状网结果填写
al_wzw = Alignment(horizontal="left", vertical="bottom")
xls_ws['D119'] = st.wzw_status
xls_ws.cell(row=119, column=4).alignment = al_wzw

xls_wb.save('test.xlsx')
