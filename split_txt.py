#!/usr/bin/env python
# --- coding:utf-8 ---
# @Time:2018/4/12
# @File:split_txt.py

import split_func as sf

# 提取各主机、数据库的巡检结果
db_func, file_func = sf.split()

# 主机文件系统空间巡检结果
file_func('-WLWJFX1-', '-WLWJFX2-')
file_func('-WLWJFX2-', '-WLWJFX3-')
file_func('-WLWJFX3-', '-WLWJFX4-')
file_func('-WLWJFX4-', '-WLWJFX5-')
file_func('-WLWJFX5-', '-WLWJFX6-')
file_func('-WLWJFX6-', '-WLWDXX1-')
file_func('-WLWDXX1-', '-WLWDXX2-')
file_func('-WLWDXX2-', '-WLWBYX1-')
file_func('-WLWBYX1-', '-WLWBYX2-')
file_func('-WLWBYX2-', '-WLWCCX1-')
file_func('-WLWCCX1-', '-WLWCCX2-')
file_func('-WLWCCX2-', '-WLWCCX3-')
file_func('-WLWCCX3-', '-wlwjs7-')
file_func('-wlwjs7-', '-wlwjs8-')
file_func('-wlwjs8-', '-WLWJS1-')
file_func('-WLWJS1-', '-WLWJS2-')
file_func('-WLWJS2-', '-WLWJS4-')
file_func('-WLWJS4-', '-WLWJS5-')
file_func('-WLWJS5-', '-WLWJKX1-')
file_func('-WLWJKX1-', '-WLWJKX2-')
file_func('-WLWJKX2-', '-WLWJKX3-')
file_func('-WLWJKX3-', '-WLWJKX4-')
file_func('-WLWJKX4-', '-WLWJKX5-')
file_func('-WLWJKX5-', '-check connection -')

# #CBBS数据库
db_func('CBBSDB3', 'check process', 'checkindex', 'checkconection')
db_func('CBBSDB3', 'check process', 'checkconection', 'checktablespace')
db_func('CBBSDB3', 'check process', 'checktablespace', 'checktablepartition')
db_func('CBBSDB3', 'check process', 'checktablepartition', '40rowsselected.')

# PSMS数据库
db_func('PSMSDB1', 'CBBSDB3', 'checkindex', 'checkconection')
db_func('PSMSDB1', 'CBBSDB3', 'checkconection', 'checktablespace')
db_func('PSMSDB1', 'CBBSDB3', 'checktablespace', '12rowsselected.')
sorted_content = db_func('PSMSDB1', 'CBBSDB3', 'checktablepartition', '16rowsselected.')

# 网状网的状态检查
wzw_status = sf.wzw_stat()

# 异常信息有无检查
sf.pick_abnormal()
