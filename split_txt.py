#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018/4/12
# @File:split_txt.py


import re
import os

# txt_path = r'E:\PycharmProjects\hck_proj\host_check\20170426.txt'
txt_path = os.path.join(os.getcwd(), '20170426.txt')


# 定义截取两个关键字之间的函数，截取有关数据库的巡检信息
def db_pick_content(start_flg, end_flg, secstart_flg, secend_flg):
    with open(txt_path, 'r') as tp:
        tp_rb = tp.read()
        tp_chg = re.sub('-|\d+(rowsselected.)|^Password:|^\n', '', tp_rb)
        tp_pk = re.compile(start_flg + '(.*?)' + end_flg, re.S)
        tp_pkcontent = tp_pk.findall(tp_chg)

    # 将tp_pkcontent的列表格式转换成字符形式，以便进一步截取需要的内容
    pk_chg = ''.join(tp_pkcontent)
    pk_content = re.compile(secstart_flg + '(.*?)' + secend_flg, re.S)
    pk_result = pk_content.findall(pk_chg)
    # 将结果转换成字符格式，后续调用需要字符形式
    pk_result = ''.join(pk_result)
    # 去除多余空行
    pk_result = re.sub('^\\n+|\\n+$', '', pk_result)
    return pk_result


# 定义截取有关主机的巡检信息的函数
def host_pick_content(secstart_flg, secend_flg, start_flg='check disk cpu memory io', end_flg='WangZhuangWang'):
    with open(txt_path, 'r') as tp:
        tp_rb = tp.read()
        tp_chg = re.sub('-|\d+(rowsselected.)|^Password:|^\n', '', tp_rb)
        # 先截取所有主机的信息
        tp_pk = re.compile(start_flg + '(.*?)' + end_flg, re.S)
        tp_pkcontent = tp_pk.findall(tp_chg)
    # 转换findall列表格式为字符串格式，以便进一步截取
    pk_chg = ''.join(tp_pkcontent)
    # 截取单个主机的巡检信息
    pk_content = re.compile(secstart_flg + '(.*?)' + secend_flg, re.S)
    tp_result = pk_content.findall(pk_chg)
    tp_result = ''.join(tp_result)
    # 再进一步截取单个主机中的文件系统空间的巡检信息
    # 设置compile的结束标志位
    file_endflg = re.search('\d.\d+\s*%', tp_result).group()
    file_sys_pk = re.compile('(.*?)' + file_endflg, re.S)
    file_sys_space = file_sys_pk.findall(tp_result)
    file_sys_space = ''.join(file_sys_space)
    # 截取cpu，内存，io的巡检信息
    host_load = re.search('(?P<cpu_load>\d.\d+\s*%)\n(?P<mem_load>\d.\d+%)\n(?P<IO_load>\d.\d+%)', tp_result)
    cpu_load = host_load.group('cpu_load')
    mem_load = host_load.group('mem_load')
    io_load = host_load.group('IO_load')
    return file_sys_space, cpu_load, mem_load, io_load

def wzw_stat(start_flg):
    with open(txt_path, 'r') as tp:
        tp_rb = tp.read()
        tp_chg = re.sub('-|\d+(rowsselected.)|^Password:|^\n', '', tp_rb)
        tp_pk = re.compile(start_flg + '(.*?)', re.S)
        tp_pkcontent = tp_pk.findall(tp_chg)
        wzw_result = ''.join(tp_pkcontent)
        return wzw_result

#PSMS数据库
# cell_PSMSindex = db_pick_content('PSMSDB1', 'CBBSDB3', 'checkindex', 'checkconection')
# cell_PSMSconection = db_pick_content('PSMSDB1', 'CBBSDB3', 'checkconection', 'checktablespace')
# cell_PSMStablesp = db_pick_content('PSMSDB1', 'CBBSDB3', 'checktablespace', 'checktablepartition')
# cell_PSMStablepart = db_pick_content('PSMSDB1', 'CBBSDB3', 'checktablepartition', 'CBBSDB3')
#
# #CBBS数据库
# cell_CBBSindex = db_pick_content('CBBSDB3', 'check process', 'checkindex', 'checkconection')
# cell_CBBSconection = db_pick_content('CBBSDB3', 'check process', 'checkconection', 'checktablespace')
# cell_CBBStablesp = db_pick_content('CBBSDB3', 'check process', 'checktablespace', 'checktablepartition')
# cell_CBBStablepart = db_pick_content('CBBSDB3', 'check process', 'checktablepartition', 'check process')
#
#
# file_jfx1,cpu_jfx1,mem_jfx1,io_jfx1 = host_pick_content('WLWJFX1', 'WLWJFX2')
# file_jfx2,cpu_jfx2,mem_jfx2,io_jfx2 = host_pick_content('WLWJFX2', 'WLWJFX3')
# file_jfx3,cpu_jfx3,mem_jfx3,io_jfx3 = host_pick_content('WLWJFX3', 'WLWJFX4')
# file_jfx4,cpu_jfx4,mem_jfx4,io_jfx4 = host_pick_content('WLWJFX4', 'WLWJFX5')
# file_jfx5,cpu_jfx5,mem_jfx5,io_jfx5 = host_pick_content('WLWJFX5', 'WLWJFX6')
# file_jfx6,cpu_jfx6,mem_jfx6,io_jfx6 = host_pick_content('WLWJFX6', 'WLWDXX1')
# file_dxx1,cpu_dxx1,mem_dxx1,io_dxx1 = host_pick_content('WLWDXX1','WLWDXX2')
# file_dxx2,cpu_dxx2,mem_dxx2,io_dxx2 = host_pick_content('WLWDXX2','WLWBYX1')
# file_byx1,cpu_byx1,mem_byx1,io_byx1 = host_pick_content('WLWBYX1','WLWBYX2')
# file_byx2,cpu_byx2,mem_byx2,io_byx2 = host_pick_content('WLWBYX2','WLWCCX1')
# file_ccx1,cpu_ccx1,mem_ccx1,io_ccx1 = host_pick_content('WLWCCX1','WLWCCX2')
# file_ccx2,cpu_ccx2,mem_ccx2,io_ccx2 = host_pick_content('WLWCCX2','WLWCCX3')
# file_ccx3,cpu_ccx3,mem_ccx3,io_ccx3 = host_pick_content('WLWCCX3','wlwjs7')
# file_js7,cpu_js7,mem_js7,io_js7 = host_pick_content('wlwjs7','wlwjs8')
# file_js8,cpu_js8,mem_js8,io_js8 = host_pick_content('wlwjs8','WLWJS1')
# file_JS1,cpu_JS1,mem_JS1,io_JS1 = host_pick_content('WLWJS1','WLWJS2')
# file_JS2,cpu_JS2,mem_JS2,io_JS2 = host_pick_content('WLWJS2','WLWJS4')
# file_JS4,cpu_JS4,mem_JS4,io_JS4 = host_pick_content('WLWJS4','WLWJS5')
# file_JS5,cpu_JS5,mem_JS5,io_JS5 = host_pick_content('WLWJS5','WLWJKX1')
# file_JKX1,cpu_JKX1,mem_JKX1,io_JKX1 = host_pick_content('WLWJKX1','WLWJKX2')
# file_JKX2,cpu_JKX2,mem_JKX2,io_JKX2 = host_pick_content('WLWJKX2','WLWJKX3')
# file_JKX3,cpu_JKX3,mem_JKX3,io_JKX3 = host_pick_content('WLWJKX3','WLWJKX4')
# file_JKX4,cpu_JKX4,mem_JKX4,io_JKX4 = host_pick_content('WLWJKX4','WLWJKX5')
# file_JKX5,cpu_JKX5,mem_JKX5,io_JKX5 = host_pick_content('WLWJKX5','check connection')

wzw_status = wzw_stat('check connection')
print(wzw_status)