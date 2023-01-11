import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

win = tk.Tk()
win.title("无人机重命名软件V0.3.1 Code by LYC")
win.geometry('770x200+500+200')
win.iconphoto(False, tk.PhotoImage(file='UAV.png'))
frame = tk.Frame(win)
# 杆塔号输入控件
label_1 = tk.Label(win, text="1.请输入杆塔号")
label_1.grid(row=0, column=0)
text_v = tk.StringVar()
entry_1 = tk.Entry(win, textvariable=text_v, width=30)
entry_1.grid(row=1, column=0)


# 下拉菜单1.命名模板
def show_num_of_model(event):
    model_cwd = os.getcwd() + "\\无人机精飞照片命名\\" + Select_com_001.get()
    with open(model_cwd, encoding="utf-8") as f:
        new_name = f.read().splitlines()
    varLabel_1.set(str(len(new_name)))


model_dir_list = os.listdir('无人机精飞照片命名')
model_dir_list.sort(key=lambda x: int(x.split('.')[0]))
xVariable_2 = tk.StringVar()
label_2 = tk.Label(win, text="2.请选择命名模板")
label_2.grid(row=0, column=1)
Select_com_001 = tk.ttk.Combobox(win, textvariable=xVariable_2, values=model_dir_list, width=30)
Select_com_001.bind('<<ComboboxSelected>>', show_num_of_model)
Select_com_001.grid(row=1, column=1)
varLabel_1 = tk.StringVar()
label_5 = tk.Label(win, textvariable=varLabel_1)
label_5.grid(row=2, column=1)


# 下拉菜单2.选择需要处理的文件夹
def show_num_of_photo(event):
    work_cwd = os.getcwd() + '\\未处理照片\\' + Select_com_002.get()
    photo_dir_list = os.listdir(work_cwd)
    varLabel_2.set(str(len(photo_dir_list)))


file_dir_list = os.listdir('未处理照片')
xVariable_3 = tk.StringVar()
label_3 = tk.Label(win, text="3.请选择需要命名的杆塔照片")
label_3.grid(row=0, column=2)
Select_com_002 = tk.ttk.Combobox(win, textvariable=xVariable_3, values=file_dir_list, width=30)
Select_com_002.bind('<<ComboboxSelected>>', show_num_of_photo)
Select_com_002.grid(row=1, column=2)
varLabel_2 = tk.StringVar()
label_6 = tk.Label(win, textvariable=varLabel_2)
label_6.grid(row=2, column=2)


# 开始按钮功能，重命名函数
def pic_Rename():
    work_cwd = os.getcwd() + '\\未处理照片\\' + Select_com_002.get()
    model_cwd = os.getcwd() + "\\无人机精飞照片命名\\" + Select_com_001.get()
    num_of_tower = entry_1.get()

    # 读取命名模板
    with open(model_cwd, encoding="utf-8") as f:
        new_name = f.read().splitlines()
        print(new_name)

    # 创建收录文件夹
    if os.path.exists(os.path.abspath('已处理照片') + "\\" + num_of_tower):
        print('路径已经存在，请重新输入名称。')
        showwarning('警告', '路径已经存在，请重新输入名称，或删除已处理照片文件夹中的同名文件夹。')
    else:
        # 重命名以及收录过程
        photo_dir_list = os.listdir(work_cwd)
        if len(photo_dir_list) == len(new_name):
            print("照片数量等于模板数量，开始转换")
            showinfo('提示', '照片数量等于模板数量，开始转换')
            os.makedirs(os.path.abspath('已处理照片') + "\\" + num_of_tower)
            for i in range(len(photo_dir_list)):
                os.rename(work_cwd + '\\' + photo_dir_list[i],
                          os.path.abspath("已处理照片" + "\\" + num_of_tower) + '\\' + num_of_tower + new_name[
                              i] + ".jpg")
            print("转换完成。")
            showinfo('提示', '转换完成')
            shutil.rmtree(work_cwd)
        elif len(photo_dir_list) > len(new_name):
            print("照片数量多于模板数量，仅修改模板数量照片")
            showinfo('提示', '照片数量多于模板数量，仅修改模板数量照片')
            os.makedirs(os.path.abspath('已处理照片') + "\\" + num_of_tower)
            for i in range(len(photo_dir_list)):
                if i < len(new_name):
                    os.rename(work_cwd + '\\' + photo_dir_list[i],
                              os.path.abspath("已处理照片" + "\\" + num_of_tower) + '\\' + num_of_tower + new_name[
                                  i] + ".jpg")
                else:
                    os.rename(work_cwd + '\\' + photo_dir_list[i],
                              os.path.abspath("已处理照片" + "\\" + num_of_tower) + '\\' + photo_dir_list[i])
            print("转换完成。")
            showinfo('提示', '转换完成')
            shutil.rmtree(work_cwd)
        else:
            print("不满足转换条件，未进行转换，请检查照片是否完整。")
            showwarning('警告', '不满足转换条件，未进行转换，请检查照片是否完整。')
        update_model_dir_list = os.listdir(os.getcwd() + '\\未处理照片\\')
        Select_com_001['values'] = update_model_dir_list
        update_file_dir_list = os.listdir(os.getcwd() + '\\未处理照片\\')
        Select_com_002['values'] = update_file_dir_list


label_4 = tk.Label(win, text="4.请点击开始")
label_4.grid(row=0, column=3)
Start_button = tk.Button(win, text='开始执行转换', command=pic_Rename)
Start_button.grid(row=1, column=3)

win.mainloop()
