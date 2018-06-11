#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2018/6/4 10:45
# @File: split_func.py
# _author_: Neo
# Email: noobydream@gmail.com

import re
import os

txt_path = os.path.join(os.getcwd(), 'host_check.txt')


def split():
    '''
    定义闭包，让所有截取内容都存入conten_pick列表内
    :return: 返回函数体db_pick_content和host_pick_content(
    '''
    content_pick = []

    # 定义截取两个关键字之间的函数，截取有关数据库的巡检信息
    def db_pick_content(start_flg, end_flg, secstart_flg, secend_flg):
        '''
        定义截取数据库截取信息的函数
        :param start_flg: 正则外层截取开始标志
        :param end_flg: 正则外层结束标志
        :param secstart_flg: 正则内层截取开始标志
        :param secend_flg: 正则内层截取结束标志
        :return: 返回content_pick列表
        '''
        with open(txt_path, 'r', encoding="utf-8") as tp:
            tp_rb = tp.read()
            # 将多余与无关的内容剔除
            tp_chg = re.sub('-|^Password:|^\\n|Could.*', '', tp_rb)
            # 匹配数据库检查项相关内容
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
        content_pick.append(pk_result)
        return content_pick

    def host_pick_content(secstart_flg, secend_flg,
                          start_flg='-check disk cpu memory io -', end_flg='-WangZhuangWang-'):
        '''
        定义截取有关主机的巡检信息的函数
        :param secstart_flg:正则内层截取开始标志
        :param secend_flg:正则内层截取结束标志
        :param start_flg:正则截取外层固定开始标志
        :param end_flg:正则截取外层固定结束标志
        :return:返回content_pick列表
        '''
        with open(txt_path, 'r', encoding="utf-8") as tp:
            tp_rb = tp.read()
            tp_chg = re.sub('\d+(rowsselected.)|^Password:|^\n|Could.*', '', tp_rb)
            tp_chg = re.sub('-+', '-', tp_chg)
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
        file_endflg = re.search('\d+\.\d+\s*%', tp_result).group()
        file_sys_pk = re.compile('(.*?)' + file_endflg, re.S)
        file_sys_space = file_sys_pk.findall(tp_result)
        file_sys_space = ''.join(file_sys_space)
        # 去除转换成列表后添加的换行符
        file_sys_space = file_sys_space.replace('\n', '', 1)
        # 截取cpu，内存，io的巡检信息
        host_load = re.search('(?P<cpu_load>\d+\.\d+\s*%)\n(?P<mem_load>\d+\.\d+%)\n(?P<IO_load>\d+\.\d+%)', tp_result)
        # 为excle单元格格式百分比作准备
        cpu_load = float(host_load.group('cpu_load').strip('%')) * 0.01
        mem_load = float(host_load.group('mem_load').strip('%')) * 0.01
        io_load = float(host_load.group('IO_load').strip('%')) * 0.01
        content_pick.append(file_sys_space)
        content_pick.append(cpu_load)
        content_pick.append(mem_load)
        content_pick.append(io_load)
        return content_pick
    return db_pick_content, host_pick_content


def wzw_stat():
    '''
    网状网状态检查
    :return:返回网状网检查结果
    '''
    with open(txt_path, 'r', encoding="utf-8") as tp:
        tp_rb = tp.read()
        tp_pk = re.search('http.*', tp_rb)
        wzw_result = tp_pk.group()
        return wzw_result


def pick_abnormal():
    '''
    匹配异常内容
    :return: 在屏幕上输出异常信息
    '''
    with open(txt_path, 'r', encoding="utf-8") as tp:
        tp_line = tp.read()
        ab_content = re.findall('Could.*|cat:.*', tp_line)
        content_pick = '\n'.join(ab_content)
        if len(content_pick) != 0:
            print("巡检有如下异常信息：")
            print(content_pick)
