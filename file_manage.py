# -*- coding: UTF-8 -*-

import os


def createfile(path, filename):  # 创建文件
    if not os.path.isdir(path):  # 无文件夹时创建
        os.makedirs(path)

    if not os.path.isfile(filename):  # 无文件时创建
        fd = open(path+"/"+filename, mode="w", encoding="utf-8")
        fd.close()
        return fd
    else:
        pass


def deletefile(filepath):  # 删除文件

    if os.path.exists(filepath):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(filepath)
    else:
        print("ERROR: No this file!\n")


# 浏览
def viewfile(path):
    if not os.path.exists(path):
        print("ERROR: No this file!\n")
        pass

    fp = open(path, "r", encoding="utf-8")
    contents = fp.read()
    fp.close()
    #print(contents)
    return contents


# 上传/下载
def upload(destdir,name,srcpath):
    if not os.path.exists(srcpath):
        print("ERROR: No this file!\n")
        pass
    contents = viewfile(srcpath)
    createfile(destdir, name)
    fd = open(destdir + "/" + name, mode="w", encoding="utf-8")
    fd.write(contents)
    fd.close()


# 执行文件
def exfile(path):
    if not os.path.exists(path):
        print("ERROR: No this file!\n")
        pass

