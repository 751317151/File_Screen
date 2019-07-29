#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author: 华豪
@Date: 2019-07-29 17:41:29
@E-Mail: hh751317151@163.com
@LastEditors: 华豪
@LastEditTime: 2019-07-29 20:35:50
'''
import string
import os
import hashlib
import time

drive_list = []  # 存放磁盘分区列表

for c in string.ascii_uppercase:
    drive = c + ":\\"
    if os.path.isdir(drive):
        drive_list.append(drive)

print(drive_list)

m_set = {0}
re_list = []
unuse_list = []
for d in drive_list:
    for root, dirs, files in os.walk(d):
        for f in files:
            # if f[-4:].lower() == ".mp3":
                msl1 = len(m_set)
                dest_file_path = os.path.join(root, f)

                m = hashlib.md5()
                with open(dest_file_path, "rb") as f:
                        data = f.read()        
                m.update(data)

                md5_value = m.hexdigest()  # 消息散列
                m_set.add(md5_value)
                msl2 = len(m_set)
                if msl2 == msl1:  # 判断重复
                        re_list.append(dest_file_path)
                print(dest_file_path, md5_value)

                info = os.stat(dest_file_path)  # 判断最后使用时间
                if time.time()-info.st_mtime > 60*60*24*30:
                    unuse_list.append(dest_file_path)

if len(re_list) > 0:
    print(re_list)
    qr = input("您电脑中有以上重复的文件，是否删除(y/n)？:")
    if qr == 'y' or qr == 'Y':
        for l in range(len(re_list)):
            os.remove(re_list[0])
            re_list.pop(0)
        print("删除成功！")

print(unuse_list)
if len(unuse_list) > 0:
    print(unuse_list)
    qr = input("您电脑中有以上文件已超过一个月没有使用过了，是否删除(y/n)？:")
    if qr == 'y' or qr == 'Y':
        for l in range(len(unuse_list)):
            os.remove(unuse_list[0])
            unuse_list.pop(0)
        print("删除成功！")