# -*- coding: UTF-8 -*-

import os

import _thread
import threading
from tkinter import messagebox
from tkinter import filedialog as fd
import tkinter as tk
import subprocess

class MyThread(threading.Thread):
    def __init__(self, func, server, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.server = server
        self.running = threading.Event()  # 用于终止线程的标识
        self.running.set()  # 设置为True

    def run(self):
        self.func(self.server, self.running)

    def stop(self):
        self.running.clear()  # 将线程终止


def createfile(path):  # 创建文件

    fd = open(path, mode="w", encoding="utf-8")
    fd.close()
    return fd


def deletefile(filepath):  # 删除文件

    if os.path.exists(filepath):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(filepath)
    else:
        print("ERROR: No this file!\n")


# 浏览
def viewfile(path, text_con):
    if not os.path.exists(path):
        print("ERROR: No this file!\n")
        message = messagebox.showwarning(title="warning", message="ERROR: No this file!")
        pass

    fp = open(path, "r", encoding="utf-8")
    contents = fp.read()
    fp.close()
    # print(contents)
    text_con.insert(tk.END, contents + "\n")
    return contents


# 上传/下载
def upload(destpath, srcpath):
    if not os.path.exists(srcpath):
        print("ERROR: No this file!\n")
        message = messagebox.showwarning(title="warning", message="ERROR: No this file!")
        pass
    sfp = open(srcpath, "r", encoding="utf-8")
    contents = sfp.read()
    sfp.close()

    createfile(destpath)
    fd = open(destpath, mode="w", encoding="utf-8")
    fd.write(contents)
    fd.close()


# 执行文件
def exfile(path,text_con):
    if not os.path.exists(path):
        print("ERROR: No this file!\n")
        message = messagebox.showwarning(title="warning", message="ERROR: No this file!")
        pass
    ret, out = subprocess.getstatusoutput(path)
    text_con.insert(tk.END, out)
    text_con.insert(tk.END, "\n")
    text_con.insert(tk.END, ret)
    text_con.insert(tk.END, "\n")


def save_path(path):
    path_ = fd.askdirectory()
    path.set(path_)


def begin_create(clientlist):
    if len(clientlist) > 0 and "create" not in clientlist:
        clientlist.append("create")
        clientlist[0].send("create".encode("utf-8"))


def thread_create(serverlist, threaddic, path):
    if len(serverlist) > 0 and "create" not in threaddic:
        create_thread = MyThread(createfile(path), serverlist[1], createfile.__name__)
        create_thread.start()
        threaddic["create"] = create_thread


def begin_delete(clientlist):
    if len(clientlist) > 0 and "delete" not in clientlist:
        clientlist.append("delete")
        clientlist[0].send("delete".encode("utf-8"))


def thread_delete(serverlist, threaddic, path):
    if len(serverlist) > 0 and "delete" not in threaddic:
        delete_thread = MyThread(deletefile(path), serverlist[1], deletefile.__name__)
        delete_thread.start()
        threaddic["delete"] = delete_thread


def begin_view(clientlist):
    if len(clientlist) > 0 and "view" not in clientlist:
        clientlist.append("view")
        clientlist[0].send("view".encode("utf-8"))


def thread_view(serverlist, threaddic, path, text_con):
    if len(serverlist) > 0 and "view" not in threaddic:
        view_thread = MyThread(viewfile(path, text_con), serverlist[1], viewfile.__name__)
        view_thread.start()
        threaddic["view"] = view_thread


def begin_load(clientlist):
    if len(clientlist) > 0 and "load" not in clientlist:
        clientlist.append("load")
        clientlist[0].send("load".encode("utf-8"))


def thread_load(serverlist, threaddic, destpath, srcpath):
    if len(serverlist) > 0 and "load" not in threaddic:
        load_thread = MyThread(upload(destpath, srcpath), serverlist[1], upload.__name__)
        load_thread.start()
        threaddic["load"] = load_thread


def begin_ex(clientlist):
    if len(clientlist) > 0 and "ex" not in clientlist:
        clientlist.append("ex")
        clientlist[0].send("ex".encode("utf-8"))


def thread_ex(serverlist, threaddic, path):
    if len(serverlist) > 0 and "ex" not in threaddic:
        ex_thread = MyThread(exfile(path), serverlist[1], exfile.__name__)
        ex_thread.start()
        threaddic["delete"] = ex_thread


def close_ex(thread):
    thread.stop()
    del thread


def thread_close_ex(threaddic):
    if "ex" in threaddic:
        _thread.start_new_thread(close_ex, (threaddic["ex"],))
        threaddic.pop("ex")