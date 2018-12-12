#!/usr/bin/env python
# --- coding:utf-8 ---
# @Time:2018/4/12
# @File:split_txt.py
from split_func import db_content as dbc
from split_func import host_content as hc
from split_func import wzw_stat as ws
from split_func import pick_abnormal


# import split_func as sf
#
# # 提取各主机、数据库的巡检结果
# db_func, file_func = sf.split()


def content_store():
    content = {
        # 主机文件系统空间巡检结果
        "WLWJFX1": hc('-WLWJFX1-', '-WLWJFX2-'),
        "WLWJFX2": hc('-WLWJFX2-', '-WLWJFX3-'),
        "WLWJFX3": hc("-WLWJFX3-","-WLWJFX4-"),
        "WLWJFX4": hc("-WLWJFX4-","-WLWJFX5-"),
        "WLWJFX5": hc('-WLWJFX5-', '-WLWJFX6-'),
        "WLWJFX6": hc('-WLWJFX6-', '-WLWDXX1-'),
        "WLWDXX1": hc('-WLWDXX1-', '-WLWDXX2-'),
        "WLWDXX2": hc('-WLWDXX2-', '-WLWBYX1-'),
        "WLWBYX1": hc('-WLWBYX1-', '-WLWBYX2-'),
        "WLWBYX2": hc('-WLWBYX2-', '-WLWCCX1-'),
        "WLWCCX1": hc('-WLWCCX1-', '-WLWCCX2-'),
        "WLWCCX2": hc('-WLWCCX2-', '-WLWCCX3-'),
        "WLWCCX3": hc('-WLWCCX3-', '-wlwjs7-'),
        "wlwjs7": hc('-wlwjs7-', '-wlwjs8-'),
        "wlwjs8": hc('-wlwjs8-', '-WLWJS1-'),
        "WLWJS1": hc('-WLWJS1-', '-WLWJS2-'),
        "WLWJS2": hc('-WLWJS2-', '-WLWJS4-'),
        "WLWJS4": hc('-WLWJS4-', '-WLWJS5-'),
        "WLWJS5": hc('-WLWJS5-', '-WLWJKX1-'),
        "WLWJKX1": hc('-WLWJKX1-', '-WLWJKX2-'),
        "WLWJKX2": hc('-WLWJKX2-', '-WLWJKX3-'),
        "WLWJKX3": hc('-WLWJKX3-', '-WLWJKX4-'),
        "WLWJKX4": hc('-WLWJKX4-', '-WLWJKX5-'),
        "WLWJKX5": hc('-WLWJKX5-', '-check connection -'),

        # #CBBS数据库
        "CBBSDB3_10.255.233.62": [
            dbc('CBBSDB3', 'check process', 'checkindex', 'checkconection'),
            dbc('CBBSDB3', 'check process', 'checkconection', 'checktablespace'),
            dbc('CBBSDB3', 'check process', 'checktablespace', 'checktablepartition'),
            dbc('CBBSDB3', 'check process', 'checktablepartition', '40rowsselected.')
        ],

        # PSMS数据库
        "PSMSDB1_10.255.233.64": [
            dbc('PSMSDB1', 'CBBSDB3', 'checkindex', 'checkconection'),
            dbc('PSMSDB1', 'CBBSDB3', 'checkconection', 'checktablespace'),
            dbc('PSMSDB1', 'CBBSDB3', 'checktablespace', '12rowsselected.'),
            dbc('PSMSDB1', 'CBBSDB3', 'checktablepartition', '16rowsselected.')
        ]
    }
    return content

# 网状网的状态检查
wzw_status = ws()

# 异常信息有无检查
pick_abnormal()
