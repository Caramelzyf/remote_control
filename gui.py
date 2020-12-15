# -*- coding: UTF-8 -*-
import tkinter as tk
import checkerror
import sys
import link
import key
import shot
import information
import process
import file_manage

def showframe(fra):
       global pre_port
       for each in frame:
              if each != fra:
                    each.grid_remove()
       fra.grid(row = 1, column = 1, rowspan = 2, columnspan = 2)
       pre_port = int(v_func.get())

def showclient():
       radiobutton_link.config(state = "disabled")
       radiobutton_file.config(state = "disabled")
       radiobutton_screen_shot.config(state = "disabled")
       radiobutton_key.config(state = "disabled")
       radiobutton_screen_contral.config(state = "disabled")
       frame[pre_port - 1].grid_remove()
       frame_client.grid(row = 1, column = 1, rowspan = 2, columnspan = 2)

def showserver():
       frame_client.grid_remove()
       radiobutton_link.config(state = "active")
       radiobutton_file.config(state = "active")
       radiobutton_screen_shot.config(state = "active")
       radiobutton_key.config(state = "active")
       radiobutton_screen_contral.config(state = "active")
       frame[pre_port - 1].grid(row = 1, column = 1, rowspan = 2, columnspan = 2)
       v_func.set(pre_port)

frame = []
clientlist = []
serverlist = []
hostvarlist = []
disklist = []
prodic = {}
nextprodic = {}
pre_port = 1
sys.path.append("D:\\SS\\remote_control")

if __name__=="__main__":
       root = tk.Tk()
       root.title("远程管理软件")
       root.geometry('900x500')
       root.resizable(width = False, height = False)

      
       frame_func = tk.Frame(root)
       frame_func.grid(row = 1, column = 0, padx = 20)
       v_func = tk.IntVar()
       v_func.set(1)
       radiobutton_link = tk.Radiobutton(frame_func, text = '连接服务端', variable = v_func, value = 1, indicatoron = False, padx = 50, command = lambda:showframe(frame_server_link))
       radiobutton_link.pack(fill = tk.X, padx = 20, pady = 10)

       radiobutton_file = tk.Radiobutton(frame_func, text='文件管理', variable=v_func, value=2, indicatoron=False, padx=50,
                                         command=lambda: showframe(frame_file))
       radiobutton_file.pack(fill=tk.X, padx=20, pady=10)

       radiobutton_file = tk.Radiobutton(frame_func, text = '进程管理', variable = v_func, value = 3, indicatoron = False, padx = 50, command = lambda:showframe(frame_process))
       radiobutton_file.pack(fill = tk.X, padx = 20, pady = 10)
       radiobutton_screen_shot = tk.Radiobutton(frame_func, text = '屏幕监控', variable = v_func, value = 4, indicatoron = False, padx = 50, command = lambda:showframe(frame_screen_shot))
       radiobutton_screen_shot.pack(fill = tk.X, padx = 20, pady = 10)
       radiobutton_key = tk.Radiobutton(frame_func, text = '键盘监控', variable = v_func, value = 5, indicatoron = False, padx = 50, command = lambda:showframe(frame_key))
       radiobutton_key.pack(fill = tk.X, padx = 20, pady = 10)
       radiobutton_screen_contral = tk.Radiobutton(frame_func, text = '主机信息', variable = v_func, value = 6, indicatoron = False, padx = 50, command = lambda:showframe(frame_screen_info))
       radiobutton_screen_contral.pack(fill = tk.X, padx = 20, pady = 10)
       frame_port = tk.Frame(root)
       frame_port.grid(row = 0, column = 1, columnspan = 2, pady = 30)
       v_port = tk.IntVar()
       v_port.set(1)

       radiobutton_server = tk.Radiobutton(frame_port, text = '客户端', variable = v_port, value = 1, indicatoron = False, padx = 80, command = showserver)
       radiobutton_server.pack(fill = tk.X, padx = 20, pady = 5, side = tk.LEFT)
       radiobutton_client = tk.Radiobutton(frame_port, text = '服务端', variable = v_port, value = 2, indicatoron = False, padx = 80, command = showclient)       
       radiobutton_client.pack(fill = tk.X, padx = 20, pady = 5, side = tk.LEFT)

       
       frame_server_link = tk.LabelFrame(root, width = 620, height = 370, borderwidth = 5, relief = tk.SUNKEN)
       frame_server_link.grid(row = 1, column = 1, rowspan = 2, columnspan = 2)
       frame.append(frame_server_link)
       w_server_link = tk.Canvas(frame_server_link, width = 620, height = 370)
       w_server_link.grid(row = 0, column = 0, rowspan = 10, columnspan = 10)
       w_server_link.create_rectangle(0, 0, 650, 400)
       label_ip = tk.Label(frame_server_link, text = "IP地址:")
       label_ip.grid(row = 0,column = 0, padx = 10, pady = 5)
       ip_link = tk.StringVar()
       entry_ip = tk.Entry(frame_server_link, textvariable = ip_link)
       entry_ip.grid(row = 0, column = 1, sticky = tk.W)
       label_port = tk.Label(frame_server_link, text = "端口号:")
       label_port.grid(row = 1, column = 0, padx = 10, pady = 5)
       port_link = tk.StringVar()
       entry_port = tk.Entry(frame_server_link, textvariable = port_link)
       entry_port.grid(row = 1, column = 1, pady = 5, sticky = tk.W)
       button_link = tk.Button(frame_server_link, text = "连接", width = 10, command = lambda:link.thread_client_link(ip_link.get(), port_link.get(), clientlist, text_key, entry_screen_shot_str, listbox_process, nextprodic, prodic, hostvarlist))
       button_link.grid(row = 2, column = 0, padx = 20, pady = 5)
       button_unlink = tk.Button(frame_server_link, text = "断开", width = 10, command = lambda:link.thread_close_link_client(clientlist, nextprodic, prodic, hostvarlist))
       button_unlink.grid(row = 2, column = 1, padx = 20, pady = 5)

       # 文件管理
       frame_file = tk.LabelFrame(root, width=620, height=370, borderwidth=5, relief=tk.SUNKEN)
       frame_file.grid(row=1, column=1, rowspan=2, columnspan=2)
       frame.append(frame_file)
       w_file = tk.Canvas(frame_file, width=620, height=370)
       w_file.grid(row=0, column=0, rowspan=10, columnspan=10)
       w_file.create_rectangle(0, 0, 650, 400)

       fraL = tk.Frame(frame_file)
       fraL.grid(row=0, column=0)
       fraR = tk.Frame(frame_file)
       fraR.grid(row=0, column=1)

       label_dest = tk.Label(fraL, text="目标文件的地址（含文件名）：")
       label_dest.grid(row=0, column=0, padx=10, pady=5)
       dest_file = tk.StringVar()
       entry_dest = tk.Entry(fraL, textvariable=dest_file)
       entry_dest.grid(row=0, column=1, sticky=tk.W)

       label_src = tk.Label(fraL, text="源文件的地址（含文件名）：")
       label_src.grid(row=1, column=0, padx=10, pady=5)
       src_file = tk.StringVar()
       entry_src = tk.Entry(fraL, textvariable=src_file)
       entry_src.grid(row=1, column=1, sticky=tk.W)

       frame_con = tk.Frame(fraL, height=20, width=20)
       frame_con.grid(row=3, column=0, rowspan=10, columnspan=2, sticky=tk.W)
       sb_con = tk.Scrollbar(frame_con)
       sb_con.pack(side=tk.RIGHT, fill=tk.Y)
       text_con = tk.Text(frame_con, height=20, width=60, yscrollcommand=sb_con.set)
       text_con.pack(side=tk.LEFT, fill=tk.BOTH)
       sb_con.config(command=text_con.yview)

       button_create = tk.Button(fraR, text="创建文件", width=20,
                                 command=lambda: file_manage.createfile(entry_dest.get()))  ##
       button_create.grid(row=1, column=0, pady=15)

       button_delete = tk.Button(fraR, text="删除文件", width=20,
                                 command=lambda: file_manage.deletefile(entry_dest.get()))  ##
       button_delete.grid(row=2, column=0, pady=15)

       button_view = tk.Button(fraR, text="浏览文件", width=20,
                               command=lambda: file_manage.viewfile(entry_dest.get(), text_con))  ##
       button_view.grid(row=3, column=0, pady=15)

       button_load = tk.Button(fraR, text="上传下载", width=20,
                               command=lambda: file_manage.upload(entry_dest.get(), entry_src.get()))  ##
       button_load.grid(row=4, column=0, pady=15)

       button_ex = tk.Button(fraR, text="运行文件", width=20,
                             command=lambda: file_manage.exfile(entry_dest.get(),text_con))  ##
       button_ex.grid(row=5, column=0, pady=15)

       frame_process = tk.LabelFrame(root, width = 620, height = 370, borderwidth = 5, relief = tk.SUNKEN)
       frame.append(frame_process)
       w_process = tk.Canvas(frame_process, width = 620, height = 370)
       w_process.grid(row = 0, column = 0, rowspan = 10, columnspan = 10)
       w_process.create_rectangle(0, 0, 650, 400)
       frame_lb_process = tk.Frame(frame_process, height = 29, width = 60)
       frame_lb_process.grid(row = 0, column = 0, rowspan = 6, columnspan = 2,sticky = tk.W)
       sb_process = tk.Scrollbar(frame_lb_process)
       sb_process.pack(side = tk.RIGHT, fill = tk.Y)
       listbox_process = tk.Listbox(frame_lb_process,  height = 21, width = 50, yscrollcommand = sb_process.set)
       listbox_process.pack(side = tk.LEFT, fill = tk.BOTH)
       sb_process.config(command = listbox_process.yview)
       button_process_contral = tk.Button(frame_process, text = "开始管理", width = 30, command = lambda:process.begin_key(clientlist, listbox_process))
       button_process_contral.grid(row = 1, column = 2, padx = 5)
       button_process_contral_end = tk.Button(frame_process, text = "停止管理", width = 30, command = lambda:process.end_key(clientlist, nextprodic))
       button_process_contral_end.grid(row = 2, column = 2, padx = 5)
       button_process_contral_info = tk.Button(frame_process, text = "详细信息", width = 30, command = lambda:process.show_proinfo(prodic, listbox_process))
       button_process_contral_info.grid(row = 3, column = 2, padx = 5)
       button_process_contral_endpro = tk.Button(frame_process, text = "结束进程", width = 30, command = lambda:process.thread_client_end_process(clientlist, prodic, listbox_process, nextprodic))
       button_process_contral_endpro.grid(row = 4, column = 2, padx = 5)
       button_process_contral_clear = tk.Button(frame_process, text = "清空", width = 30, command = lambda:process.clear_lb(listbox_process, prodic, nextprodic))
       button_process_contral_clear.grid(row = 5, column = 2, padx = 5)
       
       

       frame_screen_shot = tk.LabelFrame(root, width = 620, height = 370, borderwidth = 5, relief = tk.SUNKEN)
       frame.append(frame_screen_shot)
       w_screen_shot = tk.Canvas(frame_screen_shot, width = 620, height = 370)
       w_screen_shot.grid(row = 0, column = 1,rowspan = 10, columnspan = 10)
       w_screen_shot.create_rectangle(0, 0, 650, 400)
       label_screen_shot = tk.Label(frame_screen_shot, text = "保存图片路径:")
       label_screen_shot.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 20)
       entry_screen_shot_str = tk.StringVar()
       entry_screen_shot = tk.Entry(frame_screen_shot, width = 30,textvariable = entry_screen_shot_str)
       entry_screen_shot.grid(row = 0, column = 2, columnspan = 2, pady = 20)
       button_photo_save = tk.Button(frame_screen_shot, text = "浏览", width = 15, command = lambda:shot.save_path(entry_screen_shot_str))
       button_photo_save.grid(row = 0, column = 4, pady = 20)
       label_fre = tk.Label(frame_screen_shot, text = "截屏频率:")
       label_fre.grid(row = 1, column = 0, columnspan = 2, pady = 8, sticky = tk.N)
       fre_str = tk.StringVar()
       fre_str.set("屏幕变化")
       menu_fre = tk.OptionMenu(frame_screen_shot, fre_str, "屏幕变化", "1s", "2s", "5s", "10s", "30s")
       menu_fre.grid(row = 1, column = 2, sticky = tk.NW)
       label_last = tk.Label(frame_screen_shot, text = "持续时长:")
       label_last.grid(row = 1, column = 3, columnspan = 2, padx = 20, pady = 8, sticky = tk.N)
       fre_last = tk.StringVar()
       fre_last.set("不限")
       menu_last = tk.OptionMenu(frame_screen_shot, fre_last, "不限", "1min", "5min", "10min", "30min", "1h", "12h", "24h")
       menu_last.grid(row = 1, column = 4, columnspan = 6, sticky = tk.N)
       button_screen_shot_begin = tk.Button(frame_screen_shot, text = "开始监控", width = 20, command = lambda:shot.begin_screen(clientlist, fre_str.get(),fre_last.get()))
       button_screen_shot_begin.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 8)
       button_screen_shot_end = tk.Button(frame_screen_shot, text = "停止监控", width = 28, command = lambda:shot.end_key(clientlist))
       button_screen_shot_end.grid(row = 4, column = 3, columnspan = 2, padx = 20, pady = 8)
       

       frame_key = tk.LabelFrame(root, width = 620, height = 370, borderwidth = 5, relief = tk.SUNKEN)
       frame.append(frame_key)
       w_key = tk.Canvas(frame_key, width = 620, height = 370)
       w_key.grid(row = 0, column = 1,rowspan = 10, columnspan = 10)
       w_key.create_rectangle(0, 0, 650, 400)
       frame_sb_key = tk.Frame(frame_key, height = 29, width = 60)
       frame_sb_key.grid(row = 0, column = 0, rowspan = 6, columnspan = 2,sticky = tk.W)
       sb_key = tk.Scrollbar(frame_sb_key)
       sb_key.pack(side = tk.RIGHT, fill = tk.Y)
       text_key = tk.Text(frame_sb_key, height = 28, width = 50, yscrollcommand = sb_key.set)
       text_key.pack(side = tk.LEFT, fill = tk.BOTH)
       sb_key.config(command = text_key.yview)
       button_key_contral = tk.Button(frame_key, text = "开始监控", width = 30, command = lambda:key.begin_key(clientlist))
       button_key_contral.grid(row = 1, column = 2, padx = 5)
       button_key_contral_end = tk.Button(frame_key, text = "停止监控", width = 30, command = lambda:key.end_key(clientlist))
       button_key_contral_end.grid(row = 2, column = 2, padx = 5)

       frame_screen_info = tk.LabelFrame(root, width = 620, height = 370, borderwidth = 5, relief = tk.SUNKEN)
       frame.append(frame_screen_info)
       w_screen_info = tk.Canvas(frame_screen_info, width = 620, height = 370)
       w_screen_info.grid(row = 0, column = 1,rowspan = 10, columnspan = 10)
       w_screen_info.create_rectangle(0, 0, 650, 400)
       label_hostname = tk.Label(frame_screen_info, text = "本机电脑名:")
       label_hostname.grid(row = 0, column = 0, columnspan = 2, sticky = tk.W, padx = 5)
       label_hostname_text = tk.StringVar()
       hostvarlist.append(label_hostname_text)
       label_hostname_show = tk.Label(frame_screen_info, textvariable = label_hostname_text)
       label_hostname_show.grid(row = 0, column = 2, columnspan = 2, sticky = tk.W)
       label_hostaddr = tk.Label(frame_screen_info, text = "本机IP:")
       label_hostaddr.grid(row = 1, column = 0, columnspan = 2, sticky = tk.W, padx = 5)
       label_hostaddr_text = tk.StringVar()
       hostvarlist.append(label_hostaddr_text)
       label_hostaddr_show = tk.Label(frame_screen_info, textvariable = label_hostaddr_text)
       label_hostaddr_show.grid(row = 1, column = 2, columnspan = 2, sticky = tk.W)
       label_hostmac = tk.Label(frame_screen_info, text = "MAC地址:")
       label_hostmac.grid(row = 2, column = 0, columnspan = 2, sticky = tk.W, padx = 5)
       label_hostmac_text = tk.StringVar()
       hostvarlist.append(label_hostmac_text)
       label_hostmac_show = tk.Label(frame_screen_info, textvariable = label_hostmac_text)
       label_hostmac_show.grid(row = 2, column = 2, columnspan = 2, sticky = tk.W)       
       label_hostarch = tk.Label(frame_screen_info, text = "操作系统架构:")
       label_hostarch.grid(row = 3, column = 0, columnspan = 2, sticky = tk.W, padx = 5)
       label_hostarch_text = tk.StringVar()
       hostvarlist.append(label_hostarch_text)
       label_hostarch_show = tk.Label(frame_screen_info, textvariable = label_hostarch_text)
       label_hostarch_show.grid(row = 3, column = 2, columnspan = 2, sticky = tk.W)
       label_hostsys = tk.Label(frame_screen_info, text = "操作系统:")
       label_hostsys.grid(row = 4, column = 0, columnspan = 2, sticky = tk.W, padx = 5)
       label_hostsys_text = tk.StringVar()
       hostvarlist.append(label_hostsys_text)
       label_hostsys_show = tk.Label(frame_screen_info, textvariable = label_hostsys_text)
       label_hostsys_show.grid(row = 4, column = 2, columnspan = 2, sticky = tk.W)
       label_hostuser = tk.Label(frame_screen_info, text = "用户名:")
       label_hostuser.grid(row = 5, column = 0, columnspan = 2, sticky = tk.W, padx = 5)
       label_hostuser_text = tk.StringVar()
       hostvarlist.append(label_hostuser_text)
       label_hostuser_show = tk.Label(frame_screen_info, textvariable = label_hostuser_text)
       label_hostuser_show.grid(row = 5, column = 2, columnspan = 2, sticky = tk.W)
       label_totalnc = tk.Label(frame_screen_info, text = "总内存:")
       label_totalnc.grid(row = 0, column = 5, columnspan = 2, sticky = tk.W)
       label_totalnc_text = tk.StringVar()
       hostvarlist.append(label_totalnc_text)
       label_totalnc_show = tk.Label(frame_screen_info, textvariable = label_totalnc_text)
       label_totalnc_show.grid(row = 0, column = 6, columnspan = 1, sticky = tk.E)       
       label_usednc = tk.Label(frame_screen_info, text = "已用内存:")
       label_usednc.grid(row = 1, column = 5, columnspan = 2, sticky = tk.W)
       label_usednc_text = tk.StringVar()
       hostvarlist.append(label_usednc_text)
       label_usednc_show = tk.Label(frame_screen_info, textvariable = label_usednc_text)
       label_usednc_show.grid(row = 1, column = 6, columnspan = 1, sticky = tk.E)
       label_freenc = tk.Label(frame_screen_info, text = "空闲内存:")
       label_freenc.grid(row = 2, column = 5, columnspan = 2, sticky = tk.W)
       label_freenc_text = tk.StringVar()
       hostvarlist.append(label_freenc_text)
       label_freenc_show = tk.Label(frame_screen_info, textvariable = label_freenc_text)
       label_freenc_show.grid(row = 2, column = 6, columnspan = 1, sticky = tk.E)
       label_sylnc = tk.Label(frame_screen_info, text = "内存使用率:")
       label_sylnc.grid(row = 3, column = 5, columnspan = 2, sticky = tk.W)
       label_sylnc_text = tk.StringVar()
       hostvarlist.append(label_sylnc_text)
       label_sylnc_show = tk.Label(frame_screen_info, textvariable = label_sylnc_text)
       label_sylnc_show.grid(row = 3, column = 6, columnspan = 1, sticky = tk.E)
       label_sylcpu = tk.Label(frame_screen_info, text = "CPU使用率:")
       label_sylcpu.grid(row = 4, column = 5, columnspan = 2, sticky = tk.W)
       label_sylcpu_text = tk.StringVar()
       hostvarlist.append(label_sylcpu_text)
       label_sylcpu_show = tk.Label(frame_screen_info, textvariable = label_sylcpu_text)
       label_sylcpu_show.grid(row = 4, column = 6, columnspan = 1, sticky = tk.E)
       gain_button = tk.Button(frame_screen_info, text = "获取信息", width = 20, command = lambda:information.begin_key(clientlist))
       gain_button.grid(row = 6, column = 0, columnspan = 3, padx = 10)
       clean_button = tk.Button(frame_screen_info, text = "清除信息", width = 20, command = lambda:information.end_key(clientlist, hostvarlist))
       clean_button.grid(row = 6, column = 4, columnspan = 3, padx = 5)
       cpu_button = tk.Button(frame_screen_info, text = "磁盘信息", width = 20, command = lambda:information.show_disk(disklist))
       cpu_button.grid(row = 6, column = 8, columnspan = 3, padx = 10)
       hostvarlist.append(disklist)


       
       frame_client = tk.LabelFrame(root, width = 620, height = 370, borderwidth = 5, relief = tk.SUNKEN)       
       w_client = tk.Canvas(frame_client, width = 620, height = 370)
       w_client.grid(row = 0, column = 1,rowspan = 10, columnspan = 10)
       w_client.create_rectangle(0, 0, 650, 400)
       label_client_port = tk.Label(frame_client, text = "端口:")
       label_client_port.grid(row = 0, column = 0, padx = 20, pady = 10, columnspan = 2)
       client_port = tk.StringVar()
       entry_client_port = tk.Entry(frame_client, textvariable = client_port)
       entry_client_port.grid(row = 0, column = 2, padx = 10, pady = 10, columnspan = 2)
       button_open_port = tk.Button(frame_client, width = 12, text = "打开端口", command = lambda:link.thread_server_link(client_port.get(), link_state, server_ip, server_port, client_ip, client_port_label, serverlist))
       button_open_port.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = tk.W, columnspan = 2)
       button_close_port = tk.Button(frame_client, width = 12, text = "关闭端口", command = lambda:link.thread_close_link_server(serverlist))
       button_close_port.grid(row = 1, column = 2, padx = 30, pady = 10, columnspan = 2, stick = tk.E)
       label_state = tk.Label(frame_client, text = "状态:")
       label_state.grid(row = 2, column = 0, padx = 20, columnspan = 2)
       link_state = tk.StringVar()
       link_state.set("未连接")
       label_link_state = tk.Label(frame_client, textvariable = link_state)
       label_link_state.grid(row = 2, column = 2, sticky = tk.W, columnspan = 2)
       label_server_ip = tk.Label(frame_client, text = "客户端IP:")
       label_server_ip.grid(row = 3, column = 0, padx = 20, columnspan = 2)
       server_ip = tk.StringVar()
       label_server_link_ip = tk.Label(frame_client, textvariable = server_ip)
       label_server_link_ip.grid(row = 3, column = 2, sticky = tk.W, columnspan = 2)
       label_server_port = tk.Label(frame_client, text = "客户端端口:")
       label_server_port.grid(row = 4, column = 0, padx = 20, columnspan = 2)
       server_port = tk.StringVar()
       label_server_link_port = tk.Label(frame_client, textvariable = server_port)
       label_server_link_port.grid(row = 4, column = 2, sticky = tk.W, columnspan = 2)
       label_client_ip = tk.Label(frame_client, text = "本地IP:")
       label_client_ip.grid(row = 5, column = 0, padx = 20, columnspan = 2)
       client_ip = tk.StringVar()
       label_client_link_ip = tk.Label(frame_client, textvariable = client_ip)
       label_client_link_ip.grid(row = 5, column = 2, sticky = tk.W, columnspan = 2)
       label_client_port = tk.Label(frame_client, text = "本地端口:")
       label_client_port.grid(row = 6, column = 0, padx = 20, columnspan = 2)
       client_port_label = tk.StringVar()
       label_client_link_port = tk.Label(frame_client, textvariable = client_port_label)
       label_client_link_port.grid(row = 6, column = 2, sticky = tk.W, columnspan = 2)
       
       
       root.mainloop()
