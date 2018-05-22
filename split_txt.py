#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018/4/12
# @File:split_txt.py

import re
import os

txt_path = os.path.join(os.getcwd(), 'host_check.txt')


# 定义截取两个关键字之间的函数，截取有关数据库的巡检信息
def db_pick_content(start_flg, end_flg, secstart_flg, secend_flg):
    with open(txt_path, 'r') as tp:
        tp_rb = tp.read()
        #将多余与无关的内容剔除
        tp_chg = re.sub('-|^Password:|^\\n', '', tp_rb)
        #匹配数据库检查项相关内容
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
def host_pick_content(secstart_flg, secend_flg,
                      start_flg='check disk cpu memory io', end_flg='WangZhuangWang'):
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
    host_load = re.search('(?P<cpu_load>\d+.\d+\s*%)\n(?P<mem_load>\d+.\d+%)\n(?P<IO_load>\d+.\d+%)', tp_result)
    cpu_load = float(host_load.group('cpu_load').strip('%'))
    mem_load = float(host_load.group('mem_load').strip('%'))
    io_load = float(host_load.group('IO_load').strip('%'))
    return file_sys_space, cpu_load, mem_load, io_load


# 网状网状态检查
def wzw_stat():
    with open(txt_path, 'r') as tp:
        tp_rb = tp.read()
        # tp_chg = re.sub('-|\d+(rowsselected.)|^Password:|^\n', '', tp_rb)
        tp_pk = re.search('http.*', tp_rb)
        wzw_result = tp_pk.group()
        return wzw_result

#空列表用以存储各个单元格对应的的内容
content_filesys = []
content_perf = []
content_db = []

#提取各主机、数据库的巡检结果
file_jfx1, cpu_jfx1, mem_jfx1, io_jfx1 = host_pick_content('WLWJFX1', 'WLWJFX2')
content_filesys.append(file_jfx1)
content_perf.append(cpu_jfx1)
content_perf.append(mem_jfx1)
content_perf.append(io_jfx1)

file_jfx2, cpu_jfx2, mem_jfx2, io_jfx2 = host_pick_content('WLWJFX2', 'WLWJFX3')
content_filesys.append(file_jfx2)
content_perf.append(cpu_jfx2)
content_perf.append(mem_jfx2)
content_perf.append(io_jfx2)

file_jfx3, cpu_jfx3, mem_jfx3, io_jfx3 = host_pick_content('WLWJFX3', 'WLWJFX4')
content_filesys.append(file_jfx3)
content_perf.append(cpu_jfx3)
content_perf.append(mem_jfx3)
content_perf.append(io_jfx3)

file_jfx4, cpu_jfx4, mem_jfx4, io_jfx4 = host_pick_content('WLWJFX4', 'WLWJFX5')
content_filesys.append(file_jfx4)
content_perf.append(cpu_jfx4)
content_perf.append(mem_jfx4)
content_perf.append(io_jfx4)

file_jfx5, cpu_jfx5, mem_jfx5, io_jfx5 = host_pick_content('WLWJFX5', 'WLWJFX6')
content_filesys.append(file_jfx5)
content_perf.append(cpu_jfx5)
content_perf.append(mem_jfx5)
content_perf.append(io_jfx5)

file_jfx6, cpu_jfx6, mem_jfx6, io_jfx6 = host_pick_content('WLWJFX6', 'WLWDXX1')
content_filesys.append(file_jfx6)
content_perf.append(cpu_jfx6)
content_perf.append(mem_jfx6)
content_perf.append(io_jfx6)

file_dxx1, cpu_dxx1, mem_dxx1, io_dxx1 = host_pick_content('WLWDXX1', 'WLWDXX2')
content_filesys.append(file_dxx1)
content_perf.append(cpu_dxx1)
content_perf.append(mem_dxx1)
content_perf.append(io_dxx1)

file_dxx2, cpu_dxx2, mem_dxx2, io_dxx2 = host_pick_content('WLWDXX2', 'WLWBYX1')
content_filesys.append(file_dxx2)
content_perf.append(cpu_dxx2)
content_perf.append(mem_dxx2)
content_perf.append(io_dxx2)

file_byx1, cpu_byx1, mem_byx1, io_byx1 = host_pick_content('WLWBYX1', 'WLWBYX2')
content_filesys.append(file_byx1)
content_perf.append(cpu_byx1)
content_perf.append(mem_byx1)
content_perf.append(io_byx1)

file_byx2, cpu_byx2, mem_byx2, io_byx2 = host_pick_content('WLWBYX2', 'WLWCCX1')
content_filesys.append(file_byx2)
content_perf.append(cpu_byx2)
content_perf.append(mem_byx2)
content_perf.append(io_byx2)

file_ccx1, cpu_ccx1, mem_ccx1, io_ccx1 = host_pick_content('WLWCCX1', 'WLWCCX2')
content_filesys.append(file_ccx1)
content_perf.append(cpu_ccx1)
content_perf.append(mem_ccx1)
content_perf.append(io_ccx1)

file_ccx2, cpu_ccx2, mem_ccx2, io_ccx2 = host_pick_content('WLWCCX2', 'WLWCCX3')
content_filesys.append(file_ccx2)
content_perf.append(cpu_ccx2)
content_perf.append(mem_ccx2)
content_perf.append(io_ccx2)

file_ccx3, cpu_ccx3, mem_ccx3, io_ccx3 = host_pick_content('WLWCCX3', 'wlwjs7')
content_filesys.append(file_ccx3)
content_perf.append(cpu_ccx3)
content_perf.append(mem_ccx3)
content_perf.append(io_ccx3)

file_js7, cpu_js7, mem_js7, io_js7 = host_pick_content('wlwjs7', 'wlwjs8')
content_filesys.append(file_js7)
content_perf.append(cpu_js7)
content_perf.append(mem_js7)
content_perf.append(io_js7)

file_js8, cpu_js8, mem_js8, io_js8 = host_pick_content('wlwjs8', 'WLWJS1')
content_filesys.append(file_js8)
content_perf.append(cpu_js8)
content_perf.append(mem_js8)
content_perf.append(io_js8)

file_JS1, cpu_JS1, mem_JS1, io_JS1 = host_pick_content('WLWJS1', 'WLWJS2')
content_filesys.append(file_JS1)
content_perf.append(cpu_JS1)
content_perf.append(mem_JS1)
content_perf.append(io_JS1)

file_JS2, cpu_JS2, mem_JS2, io_JS2 = host_pick_content('WLWJS2', 'WLWJS4')
content_filesys.append(file_JS2)
content_perf.append(cpu_JS2)
content_perf.append(mem_JS2)
content_perf.append(io_JS2)

file_JS4, cpu_JS4, mem_JS4, io_JS4 = host_pick_content('WLWJS4', 'WLWJS5')
content_filesys.append(file_JS4)
content_perf.append(cpu_JS4)
content_perf.append(mem_JS4)
content_perf.append(io_JS4)

file_JS5, cpu_JS5, mem_JS5, io_JS5 = host_pick_content('WLWJS5', 'WLWJKX1')
content_filesys.append(file_JS5)
content_perf.append(cpu_JS5)
content_perf.append(mem_JS5)
content_perf.append(io_JS5)
file_JKX1, cpu_JKX1, mem_JKX1, io_JKX1 = host_pick_content('WLWJKX1', 'WLWJKX2')
content_filesys.append(file_JKX1)
content_perf.append(cpu_JKX1)
content_perf.append(mem_JKX1)
content_perf.append(io_JKX1)

file_JKX2, cpu_JKX2, mem_JKX2, io_JKX2 = host_pick_content('WLWJKX2', 'WLWJKX3')
content_filesys.append(file_JKX2)
content_perf.append(cpu_JKX2)
content_perf.append(mem_JKX2)
content_perf.append(io_JKX2)

file_JKX3, cpu_JKX3, mem_JKX3, io_JKX3 = host_pick_content('WLWJKX3', 'WLWJKX4')
content_filesys.append(file_JKX3)
content_perf.append(cpu_JKX3)
content_perf.append(mem_JKX3)
content_perf.append(io_JKX3)

file_JKX4, cpu_JKX4, mem_JKX4, io_JKX4 = host_pick_content('WLWJKX4', 'WLWJKX5')
content_filesys.append(file_JKX4)
content_perf.append(cpu_JKX4)
content_perf.append(mem_JKX4)
content_perf.append(io_JKX4)

file_JKX5, cpu_JKX5, mem_JKX5, io_JKX5 = host_pick_content('WLWJKX5', 'check connection')
content_filesys.append(file_JKX5)
content_perf.append(cpu_JKX5)
content_perf.append(mem_JKX5)
content_perf.append(io_JKX5)

# PSMS数据库
PSMSindex = db_pick_content('PSMSDB1', 'CBBSDB3', 'checkindex', 'checkconection')
content_db.append(PSMSindex)

PSMSconection = db_pick_content('PSMSDB1', 'CBBSDB3', 'checkconection', 'checktablespace')
content_db.append(PSMSconection)

PSMStablesp = db_pick_content('PSMSDB1', 'CBBSDB3', 'checktablespace', '7rowsselected.')
content_db.append(PSMStablesp)

PSMStablepart = db_pick_content('PSMSDB1', 'CBBSDB3', 'checktablepartition', '16rowsselected.')
content_db.append(PSMStablepart)

# #CBBS数据库
CBBSindex = db_pick_content('CBBSDB3', 'check process', 'checkindex', 'checkconection')
content_db.append(CBBSindex)

CBBSconection = db_pick_content('CBBSDB3', 'check process', 'checkconection', 'checktablespace')
content_db.append(CBBSconection)

CBBStablesp = db_pick_content('CBBSDB3', 'check process', 'checktablespace', 'checktablepartition')
content_db.append(CBBStablesp)

CBBStablepart = db_pick_content('CBBSDB3', 'check process', 'checktablepartition', '40rowsselected.')
content_db.append(CBBStablepart)

#网状网的状态检查
wzw_status = wzw_stat()
